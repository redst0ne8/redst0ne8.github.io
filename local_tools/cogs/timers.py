"""
timers.py — Countdown Timer cog.
Supports multiple named timers running concurrently.
"""

import threading
import time
from typing import Callable, Optional
from core.base_cog import BaseCog


class _Timer:
    """A single countdown timer instance."""

    def __init__(
        self,
        name: str,
        duration: float,
        on_finish: Optional[Callable[[str], None]] = None,
    ):
        self.name = name
        self.duration = duration
        self.remaining = duration
        self.on_finish = on_finish
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self):
        self._thread.start()

    def cancel(self):
        self._stop_event.set()

    def _run(self):
        end = time.monotonic() + self.duration
        while not self._stop_event.is_set():
            self.remaining = max(0.0, end - time.monotonic())
            if self.remaining <= 0:
                if self.on_finish:
                    self.on_finish(self.name)
                break
            time.sleep(0.1)

    @property
    def is_alive(self) -> bool:
        return self._thread.is_alive()


class TimerCog(BaseCog):
    name = "timer"
    description = "Countdown timer system — supports multiple named concurrent timers."

    def __init__(self):
        super().__init__()
        self._timers: dict[str, _Timer] = {}
        self._finished: list[str] = []

    # ------------------------------------------------------------------ #

    def run(
        self,
        duration: float = 60.0,
        label: str = "timer",
        on_finish: Optional[Callable[[str], None]] = None,
        **kwargs,
    ):
        """
        Start a countdown timer.

        Args:
            duration:  Seconds to count down from.
            label:     Unique name for this timer instance.
            on_finish: Optional callback called with label when timer completes.
        """
        if label in self._timers and self._timers[label].is_alive:
            return  # already running under this label

        def _default_finish(name: str):
            self._finished.append(name)
            del self._timers[name]

        callback = on_finish or _default_finish
        t = _Timer(label, duration, on_finish=callback)
        self._timers[label] = t
        t.start()
        self._running = bool(self._timers)
        self._clear_error()

    def stop(self, label: Optional[str] = None):
        """
        Cancel a timer by label, or all timers if label is None.
        """
        if label:
            if label in self._timers:
                self._timers[label].cancel()
                del self._timers[label]
        else:
            for t in self._timers.values():
                t.cancel()
            self._timers.clear()
        self._running = bool(self._timers)

    def status(self) -> str:
        if not self._timers:
            finished_note = f" | Finished: {self._finished}" if self._finished else ""
            return f"No active timers{finished_note}"
        lines = []
        for name, t in self._timers.items():
            m = int(t.remaining // 60)
            s = t.remaining % 60
            lines.append(f"  [{name}] {m:02}:{s:05.2f} remaining")
        return "Active timers:\n" + "\n".join(lines)

    # ------------------------------------------------------------------ #

    def get_remaining(self, label: str) -> Optional[float]:
        """Return seconds remaining for a named timer, or None if not found."""
        t = self._timers.get(label)
        return t.remaining if t else None

    @property
    def active_timers(self) -> list[str]:
        return list(self._timers.keys())
