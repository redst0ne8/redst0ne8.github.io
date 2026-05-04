"""
autoclicker.py — AutoClicker cog.
Uses ydotool for Wayland-native mouse click simulation.
"""

import threading
import time
import subprocess
from core.base_cog import BaseCog


class AutoClickerCog(BaseCog):
    name = "autoclicker"
    description = "Simulates repeated mouse clicks at a configurable interval."

    def __init__(self):
        super().__init__()
        self._thread: threading.Thread | None = None
        self._interval: float = 1.0      # seconds between clicks
        self._click_count: int = 0
        self._button: int = 1            # 1=left, 2=middle, 3=right

    # ------------------------------------------------------------------ #

    def run(self, interval: float = 1.0, button: int = 1, **kwargs):
        """
        Start the autoclicker.

        Args:
            interval: Seconds between each click (default 1.0).
            button:   Mouse button to click — 1=left, 2=middle, 3=right.
        """
        if self._running:
            return

        self._interval = max(0.05, interval)   # floor at 50 ms
        self._button = button
        self._click_count = 0
        self._running = True
        self._clear_error()

        self._thread = threading.Thread(target=self._click_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the autoclicker."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=2)
            self._thread = None

    def status(self) -> str:
        if self._error:
            return f"Error: {self._error}"
        if self._running:
            return f"Running — {self._click_count} clicks @ {self._interval}s interval"
        return f"Stopped — last session: {self._click_count} clicks"

    # ------------------------------------------------------------------ #
    #  Internal                                                            #
    # ------------------------------------------------------------------ #

    def _click_loop(self):
        while self._running:
            try:
                # ydotool click: button flags 0x00=left, 0x01=right, 0x02=middle
                button_flag = {1: "0x00", 2: "0x02", 3: "0x01"}.get(self._button, "0x00")
                subprocess.run(
                    ["ydotool", "click", button_flag],
                    check=True,
                    capture_output=True,
                )
                self._click_count += 1
            except FileNotFoundError:
                self._set_error("ydotool not found — is it installed and in PATH?")
                return
            except subprocess.CalledProcessError as e:
                self._set_error(f"ydotool error: {e.stderr.decode().strip()}")
                return

            time.sleep(self._interval)

    @property
    def click_count(self) -> int:
        return self._click_count

    @property
    def interval(self) -> float:
        return self._interval
