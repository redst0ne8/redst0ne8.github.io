"""
cli_router.py — Wires all cogs into a Click-based CLI.
Entry point: called by main.py when launched in CLI mode.
"""

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()


def build_cli(cog_registry: dict):
    """
    Dynamically build a Click group from the cog registry.

    Args:
        cog_registry: dict mapping cog name → cog instance
    """

    @click.group()
    def cli():
        """local_tools — a modular toolkit for power users."""
        pass

    # ── status ─────────────────────────────────────────────────────────
    @cli.command()
    def status():
        """Show status of all loaded cogs."""
        table = Table(title="Cog Status", box=box.ROUNDED, highlight=True)
        table.add_column("Cog", style="cyan bold")
        table.add_column("Description", style="white")
        table.add_column("Status", style="green")

        for name, cog in cog_registry.items():
            table.add_row(name, cog.description, cog.status())

        console.print(table)

    # ── autoclicker ─────────────────────────────────────────────────────
    if "autoclicker" in cog_registry:
        cog = cog_registry["autoclicker"]

        @cli.group(name="autoclicker")
        def autoclicker_group():
            """AutoClicker controls."""
            pass

        @autoclicker_group.command("start")
        @click.option("--interval", "-i", default=1.0, show_default=True,
                      help="Seconds between clicks.")
        @click.option("--button", "-b", default=1, show_default=True,
                      type=click.Choice(["1", "2", "3"]),
                      help="Mouse button: 1=left 2=middle 3=right.")
        def ac_start(interval, button):
            """Start the autoclicker."""
            cog.run(interval=interval, button=int(button))
            console.print(Panel(f"[green]AutoClicker started[/] — {interval}s interval", expand=False))

        @autoclicker_group.command("stop")
        def ac_stop():
            """Stop the autoclicker."""
            cog.stop()
            console.print(Panel("[yellow]AutoClicker stopped[/]", expand=False))

        @autoclicker_group.command("status")
        def ac_status():
            """Show autoclicker status."""
            console.print(cog.status())

    # ── stopwatch ───────────────────────────────────────────────────────
    if "stopwatch" in cog_registry:
        cog = cog_registry["stopwatch"]

        @cli.group(name="stopwatch")
        def stopwatch_group():
            """Stopwatch controls."""
            pass

        @stopwatch_group.command("start")
        def sw_start():
            """Start or resume the stopwatch."""
            cog.run()
            console.print("[green]Stopwatch started.[/]")

        @stopwatch_group.command("stop")
        def sw_stop():
            """Pause the stopwatch."""
            cog.stop()
            console.print(f"[yellow]Stopwatch paused.[/] Elapsed: {cog.elapsed:.2f}s")

        @stopwatch_group.command("lap")
        def sw_lap():
            """Record a lap."""
            t = cog.lap()
            console.print(f"[cyan]Lap {len(cog.laps)}:[/] {t:.2f}s")

        @stopwatch_group.command("reset")
        def sw_reset():
            """Reset the stopwatch."""
            cog.reset()
            console.print("[red]Stopwatch reset.[/]")

        @stopwatch_group.command("status")
        def sw_status():
            """Show stopwatch status."""
            console.print(cog.status())

    # ── timer ────────────────────────────────────────────────────────────
    if "timer" in cog_registry:
        cog = cog_registry["timer"]

        @cli.group(name="timer")
        def timer_group():
            """Countdown timer controls."""
            pass

        @timer_group.command("start")
        @click.argument("duration", type=float)
        @click.option("--label", "-l", default="timer", show_default=True,
                      help="Name for this timer instance.")
        def t_start(duration, label):
            """Start a countdown timer for DURATION seconds."""
            def on_done(name):
                console.print(f"\n[bold green]⏰ Timer '{name}' finished![/]")

            cog.run(duration=duration, label=label, on_finish=on_done)
            console.print(f"[green]Timer '{label}' started[/] — {duration}s")

        @timer_group.command("stop")
        @click.option("--label", "-l", default=None,
                      help="Label of timer to stop (omit to stop all).")
        def t_stop(label):
            """Stop a timer (or all timers)."""
            cog.stop(label=label)
            console.print("[yellow]Timer(s) stopped.[/]")

        @timer_group.command("status")
        def t_status():
            """Show all active timers."""
            console.print(cog.status())

    # ── textreplacement ─────────────────────────────────────────────────
    if "textreplacement" in cog_registry:
        cog = cog_registry["textreplacement"]

        @cli.group(name="textrep")
        def textrep_group():
            """Text replacement controls."""
            pass

        @textrep_group.command("add")
        @click.argument("trigger")
        @click.argument("replacement")
        def tr_add(trigger, replacement):
            """Add a TRIGGER → REPLACEMENT rule."""
            cog.add_replacement(trigger, replacement)
            console.print(f"[green]Added:[/] '{trigger}' → '{replacement}'")

        @textrep_group.command("remove")
        @click.argument("trigger")
        def tr_remove(trigger):
            """Remove a trigger rule."""
            cog.remove_replacement(trigger)
            console.print(f"[yellow]Removed:[/] '{trigger}'")

        @textrep_group.command("list")
        def tr_list():
            """List all active replacement rules."""
            rules = cog.replacements
            if not rules:
                console.print("[dim]No replacement rules configured.[/]")
                return
            table = Table(box=box.SIMPLE)
            table.add_column("Trigger", style="cyan")
            table.add_column("Replacement", style="green")
            for trigger, rep in rules.items():
                table.add_row(trigger, rep)
            console.print(table)

        @textrep_group.command("start")
        def tr_start():
            """Start listening for trigger phrases."""
            cog.run()
            console.print("[green]Text replacement listener started.[/]")

        @textrep_group.command("stop")
        def tr_stop():
            """Stop the text replacement listener."""
            cog.stop()
            console.print("[yellow]Text replacement listener stopped.[/]")

        @textrep_group.command("status")
        def tr_status():
            """Show text replacement status."""
            console.print(cog.status())

    return cli
