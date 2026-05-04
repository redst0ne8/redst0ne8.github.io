#!/usr/bin/env python3
"""
main.py — local_tools entry point.

Usage:
  python main.py gui              Launch the GUI
  python main.py cli <command>    Run a CLI command
  python main.py cli --help       List all CLI commands
"""

import sys
from cogs import AutoClickerCog, StopwatchCog, TimerCog, TextReplacementCog


def build_registry() -> dict:
    """
    Instantiate all cogs and return them keyed by their name.
    Add new cogs here — the CLI and GUI routers pick them up automatically.
    """
    cogs = [
        AutoClickerCog(),
        StopwatchCog(),
        TimerCog(),
        TextReplacementCog(),
    ]
    return {cog.name: cog for cog in cogs}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        _print_help()
        return

    mode = sys.argv[1].lower()

    if mode == "gui":
        _launch_gui()

    elif mode == "cli":
        _launch_cli()

    else:
        print(f"Unknown mode: '{mode}'. Use 'gui' or 'cli'.")
        _print_help()
        sys.exit(1)


def _launch_gui():
    from gui import launch_gui
    registry = build_registry()
    launch_gui(registry)


def _launch_cli():
    from cli import build_cli
    registry = build_registry()
    cli = build_cli(registry)

    # Strip 'cli' from argv so Click sees the sub-commands cleanly
    sys.argv = [sys.argv[0]] + sys.argv[2:]
    cli(standalone_mode=True)


def _print_help():
    print(
        "\n"
        "  local_tools\n"
        "  ──────────────────────────────────\n"
        "  python main.py gui            → Launch GUI\n"
        "  python main.py cli --help     → CLI command list\n"
        "  python main.py cli status     → Status of all cogs\n"
        "\n"
        "  CLI examples:\n"
        "    python main.py cli autoclicker start --interval 0.5\n"
        "    python main.py cli stopwatch start\n"
        "    python main.py cli timer start 30 --label coffee\n"
        "    python main.py cli textrep add 'brb' 'be right back'\n"
    )


if __name__ == "__main__":
    main()
