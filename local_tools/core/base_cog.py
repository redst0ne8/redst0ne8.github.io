"""
base_cog.py — Base class for all cogs in local_tools.
Every cog must inherit from BaseCog and implement the required interface.
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseCog(ABC):
    """
    Abstract base class for all tool cogs.

    Each cog represents a self-contained tool (autoclicker, timer, etc.)
    and must define:
      - name:        short identifier used by CLI/GUI routing
      - description: one-line human-readable summary
      - run():       core logic entry point
      - stop():      graceful shutdown
      - status():    current state string
    """

    # --- Subclasses must set these as class-level attributes ---
    name: str = "base"
    description: str = "Base cog — do not use directly."

    def __init__(self):
        self._running: bool = False
        self._error: Optional[str] = None

    # ------------------------------------------------------------------ #
    #  Abstract interface — every cog must implement these                 #
    # ------------------------------------------------------------------ #

    @abstractmethod
    def run(self, **kwargs):
        """Start or execute the cog's primary function."""
        ...

    @abstractmethod
    def stop(self):
        """Gracefully stop/cancel the cog's operation."""
        ...

    @abstractmethod
    def status(self) -> str:
        """Return a human-readable string describing current state."""
        ...

    # ------------------------------------------------------------------ #
    #  Shared helpers available to all cogs                                #
    # ------------------------------------------------------------------ #

    @property
    def is_running(self) -> bool:
        return self._running

    @property
    def last_error(self) -> Optional[str]:
        return self._error

    def _set_error(self, message: str):
        self._error = message
        self._running = False

    def _clear_error(self):
        self._error = None

    def get_info(self) -> dict:
        """Return a dict summary of this cog — used by CLI/GUI routers."""
        return {
            "name": self.name,
            "description": self.description,
            "running": self._running,
            "error": self._error,
            "status": self.status(),
        }

    def __repr__(self) -> str:
        return f"<Cog:{self.name} running={self._running}>"
