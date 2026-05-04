"""
textreplacement.py — Text Replacement cog.
Listens for typed trigger phrases via evdev and replaces them using ydotool.
Requires: evdev, ydotool, and user in the 'input' group.
"""

import subprocess
import threading
import time
from typing import Optional
from core.base_cog import BaseCog

try:
    import evdev
    from evdev import InputDevice, categorize, ecodes
    EVDEV_AVAILABLE = True
except ImportError:
    EVDEV_AVAILABLE = False

# Map evdev key codes to characters (US QWERTY, unshifted + shifted)
_KEY_MAP: dict[str, tuple[str, str]] = {
    "KEY_A": ("a", "A"), "KEY_B": ("b", "B"), "KEY_C": ("c", "C"),
    "KEY_D": ("d", "D"), "KEY_E": ("e", "E"), "KEY_F": ("f", "F"),
    "KEY_G": ("g", "G"), "KEY_H": ("h", "H"), "KEY_I": ("i", "I"),
    "KEY_J": ("j", "J"), "KEY_K": ("k", "K"), "KEY_L": ("l", "L"),
    "KEY_M": ("m", "M"), "KEY_N": ("n", "N"), "KEY_O": ("o", "O"),
    "KEY_P": ("p", "P"), "KEY_Q": ("q", "Q"), "KEY_R": ("r", "R"),
    "KEY_S": ("s", "S"), "KEY_T": ("t", "T"), "KEY_U": ("u", "U"),
    "KEY_V": ("v", "V"), "KEY_W": ("w", "W"), "KEY_X": ("x", "X"),
    "KEY_Y": ("y", "Y"), "KEY_Z": ("z", "Z"),
    "KEY_1": ("1", "!"), "KEY_2": ("2", "@"), "KEY_3": ("3", "#"),
    "KEY_4": ("4", "$"), "KEY_5": ("5", "%"), "KEY_6": ("6", "^"),
    "KEY_7": ("7", "&"), "KEY_8": ("8", "*"), "KEY_9": ("9", "("),
    "KEY_0": ("0", ")"),
    "KEY_SPACE": (" ", " "), "KEY_COMMA": (",", "<"),
    "KEY_DOT": (".", ">"), "KEY_SLASH": ("/", "?"),
    "KEY_SEMICOLON": (";", ":"), "KEY_APOSTROPHE": ("'", '"'),
    "KEY_MINUS": ("-", "_"), "KEY_EQUAL": ("=", "+"),
}


class TextReplacementCog(BaseCog):
    name = "textreplacement"
    description = "Replaces typed trigger phrases with configured replacement text in real time."

    def __init__(self):
        super().__init__()
        self._replacements: dict[str, str] = {}
        self._buffer: str = ""
        self._thread: Optional[threading.Thread] = None
        self._device: Optional["evdev.InputDevice"] = None
        self._shift_held: bool = False

    # ------------------------------------------------------------------ #
    #  Public API                                                          #
    # ------------------------------------------------------------------ #

    def add_replacement(self, trigger: str, replacement: str):
        """Register a trigger → replacement pair."""
        self._replacements[trigger] = replacement

    def remove_replacement(self, trigger: str):
        """Remove a trigger phrase."""
        self._replacements.pop(trigger, None)

    def clear_replacements(self):
        self._replacements.clear()

    @property
    def replacements(self) -> dict[str, str]:
        return dict(self._replacements)

    # ------------------------------------------------------------------ #
    #  BaseCog interface                                                   #
    # ------------------------------------------------------------------ #

    def run(self, replacements: Optional[dict[str, str]] = None, **kwargs):
        """
        Start listening for trigger phrases.

        Args:
            replacements: Optional dict of {trigger: replacement} to load.
        """
        if not EVDEV_AVAILABLE:
            self._set_error("evdev not installed. Run: pip install evdev")
            return

        if self._running:
            return

        if replacements:
            self._replacements.update(replacements)

        device_path = self._find_keyboard()
        if not device_path:
            self._set_error(
                "No keyboard input device found. "
                "Make sure you're in the 'input' group: sudo usermod -aG input $USER"
            )
            return

        try:
            self._device = InputDevice(device_path)
            self._device.grab()   # exclusive grab so we can intercept
        except PermissionError:
            self._set_error("Permission denied on input device. Add user to 'input' group.")
            return

        self._running = True
        self._clear_error()
        self._buffer = ""

        self._thread = threading.Thread(target=self._listen_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False
        if self._device:
            try:
                self._device.ungrab()
            except Exception:
                pass
            self._device = None
        if self._thread:
            self._thread.join(timeout=2)
            self._thread = None

    def status(self) -> str:
        if self._error:
            return f"Error: {self._error}"
        state = "Listening" if self._running else "Stopped"
        rules = len(self._replacements)
        return f"{state} — {rules} replacement rule(s) active"

    # ------------------------------------------------------------------ #
    #  Internal                                                            #
    # ------------------------------------------------------------------ #

    def _listen_loop(self):
        try:
            for event in self._device.read_loop():
                if not self._running:
                    break
                if event.type != ecodes.EV_KEY:
                    continue

                key_event = categorize(event)
                key_name = key_event.keycode if isinstance(key_event.keycode, str) \
                    else key_event.keycode[0]

                # Track shift state
                if key_name in ("KEY_LEFTSHIFT", "KEY_RIGHTSHIFT"):
                    self._shift_held = key_event.keystate == key_event.key_down
                    continue

                if key_event.keystate != key_event.key_down:
                    continue

                # Backspace shrinks buffer
                if key_name == "KEY_BACKSPACE":
                    self._buffer = self._buffer[:-1]
                    self._type_key("KEY_BACKSPACE")
                    continue

                # Space / enter clear buffer after forwarding
                if key_name in ("KEY_ENTER", "KEY_SPACE"):
                    self._buffer = ""
                    self._type_key(key_name)
                    continue

                char = self._resolve_char(key_name)
                if char:
                    self._buffer += char
                    self._type_key(key_name, shifted=self._shift_held)
                    self._check_replacements()
                else:
                    # Unknown key — pass through and clear buffer
                    self._buffer = ""

        except Exception as e:
            self._set_error(str(e))

    def _check_replacements(self):
        for trigger, replacement in self._replacements.items():
            if self._buffer.endswith(trigger):
                # Delete the trigger text
                for _ in trigger:
                    self._send_backspace()

                # Type the replacement
                self._type_string(replacement)

                # Trim buffer
                self._buffer = self._buffer[: -len(trigger)] + replacement
                break

    def _resolve_char(self, key_name: str) -> Optional[str]:
        pair = _KEY_MAP.get(key_name)
        if not pair:
            return None
        return pair[1] if self._shift_held else pair[0]

    def _type_key(self, key_name: str, shifted: bool = False):
        """Forward a single key press via ydotool."""
        try:
            if shifted:
                subprocess.run(
                    ["ydotool", "key", "shift+" + key_name.replace("KEY_", "").lower()],
                    capture_output=True,
                )
            else:
                subprocess.run(
                    ["ydotool", "key", key_name.replace("KEY_", "").lower()],
                    capture_output=True,
                )
        except FileNotFoundError:
            self._set_error("ydotool not found.")

    def _send_backspace(self):
        try:
            subprocess.run(["ydotool", "key", "backspace"], capture_output=True)
            time.sleep(0.01)
        except FileNotFoundError:
            pass

    def _type_string(self, text: str):
        try:
            subprocess.run(["ydotool", "type", "--", text], capture_output=True)
        except FileNotFoundError:
            self._set_error("ydotool not found.")

    @staticmethod
    def _find_keyboard() -> Optional[str]:
        """Find the first keyboard input device via evdev."""
        if not EVDEV_AVAILABLE:
            return None
        try:
            devices = [InputDevice(path) for path in evdev.list_devices()]
            for dev in devices:
                caps = dev.capabilities()
                if ecodes.EV_KEY in caps and ecodes.KEY_A in caps[ecodes.EV_KEY]:
                    return dev.path
        except Exception:
            pass
        return None
