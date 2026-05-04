"""
stopwatch.py — Stopwatch cog.
Tracks elapsed time with lap support.
"""

import time
from core.base_cog import BaseCog


class StopwatchCog(BaseCog):
    name = "stopwatch"
    description = "Stopwatch with lap tracking and pause/resume support."

    def __init__(self):
        super().__init__()
        self._start_time: float | None = None
        self._elapsed: float = 0.0          # accumulated time before pause
        self._laps: list[float] = []

    # ------------------------------------------------------------------ #

    def run(self, **kwargs):
        """Start or resume the stopwatch."""
        if self._running:
            return
        self._start_time = time.monotonic()
        self._running = True
        self._clear_error()

    def stop(self):
        """Pause the stopwatch (preserves elapsed time)."""
        if not self._running:
            return
        self._elapsed += time.monotonic() - self._start_time
        self._start_time = None
        self._running = False

    def reset(self):
        """Fully reset the stopwatch."""
        self._running = False
        self._start_time = None
        self._elapsed = 0.0
        self._laps.clear()

    def lap(self) -> float:
        """Record a lap and return the current elapsed time."""
        t = self.elapsed
        self._laps.append(t)
        return t

    def status(self) -> str:
        elapsed = self.elapsed
        formatted = self._format(elapsed)
        state = "Running" if self._running else "Paused"
        lap_info = f" | Laps: {len(self._laps)}" if self._laps else ""
        return f"{state} — {formatted}{lap_info}"

    # ------------------------------------------------------------------ #

    @property
    def elapsed(self) -> float:
        """Current elapsed seconds (works while running or paused)."""
        if self._running and self._start_time is not None:
            return self._elapsed + (time.monotonic() - self._start_time)
        return self._elapsed

    @property
    def laps(self) -> list[float]:
        return list(self._laps)

    @staticmethod
    def _format(seconds: float) -> str:
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = seconds % 60
        if h:
            return f"{h:02}:{m:02}:{s:05.2f}"
        return f"{m:02}:{s:05.2f}"
