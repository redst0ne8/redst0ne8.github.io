"""
gui_router.py — Redesigned GUI with a clean dark utilitarian aesthetic.
"""

import customtkinter as ctk
from typing import Optional

# ── Theme constants ──────────────────────────────────────────────────────
BG_BASE      = "#0f1117"
BG_PANEL     = "#161b27"
BG_CARD      = "#1c2333"
BG_INPUT     = "#111827"
ACCENT       = "#00d4aa"
ACCENT_DIM   = "#00a882"
TEXT_PRIMARY = "#e8eaf0"
TEXT_DIM     = "#6b7280"
TEXT_MUTED   = "#374151"
DANGER       = "#ef4444"
DANGER_DIM   = "#b91c1c"
BORDER       = "#1f2d3d"

FONT_MONO    = ("Courier New", 11)
FONT_MONO_LG = ("Courier New", 32, "bold")
FONT_MONO_SM = ("Courier New", 9)
FONT_UI      = ("Helvetica", 11)
FONT_UI_SM   = ("Helvetica", 9)
FONT_TITLE   = ("Helvetica", 13, "bold")
FONT_NAV     = ("Courier New", 10)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ── Shared widget helpers ────────────────────────────────────────────────

def _card(parent, **kwargs) -> ctk.CTkFrame:
    return ctk.CTkFrame(
        parent, fg_color=BG_CARD, corner_radius=6,
        border_width=1, border_color=BORDER, **kwargs,
    )

def _label(parent, text, font=None, color=TEXT_PRIMARY, **kwargs) -> ctk.CTkLabel:
    return ctk.CTkLabel(parent, text=text, font=font or FONT_UI,
                        text_color=color, **kwargs)

def _btn(parent, text, command, color=ACCENT, text_color=BG_BASE,
         width=110, **kwargs) -> ctk.CTkButton:
    return ctk.CTkButton(
        parent, text=text, command=command,
        fg_color=color, hover_color=ACCENT_DIM,
        text_color=text_color, font=FONT_NAV,
        corner_radius=4, width=width, height=32, **kwargs,
    )

def _ghost_btn(parent, text, command, width=110, **kwargs) -> ctk.CTkButton:
    return ctk.CTkButton(
        parent, text=text, command=command,
        fg_color=BG_INPUT, hover_color=BG_CARD,
        text_color=TEXT_DIM, font=FONT_NAV,
        corner_radius=4, width=width, height=32,
        border_width=1, border_color=BORDER, **kwargs,
    )

def _danger_btn(parent, text, command, width=110, **kwargs) -> ctk.CTkButton:
    return ctk.CTkButton(
        parent, text=text, command=command,
        fg_color=DANGER, hover_color=DANGER_DIM,
        text_color="#ffffff", font=FONT_NAV,
        corner_radius=4, width=width, height=32, **kwargs,
    )

def _entry(parent, textvariable=None, width=140, placeholder="") -> ctk.CTkEntry:
    return ctk.CTkEntry(
        parent, textvariable=textvariable, placeholder_text=placeholder,
        fg_color=BG_INPUT, border_color=BORDER,
        text_color=TEXT_PRIMARY, placeholder_text_color=TEXT_MUTED,
        font=FONT_MONO, corner_radius=4, width=width, height=32,
    )

def _section_header(parent, text: str) -> ctk.CTkFrame:
    f = ctk.CTkFrame(parent, fg_color="transparent")
    _label(f, text, font=FONT_MONO_SM, color=ACCENT).pack(side="left")
    ctk.CTkFrame(f, fg_color=BORDER, height=1, corner_radius=0).pack(
        side="left", fill="x", expand=True, padx=(8, 0), pady=1)
    return f


# ── Main App ─────────────────────────────────────────────────────────────

class LocalToolsApp(ctk.CTk):
    def __init__(self, cog_registry: dict):
        super().__init__()
        self.cog_registry = cog_registry
        self.configure(fg_color=BG_BASE)
        self.title("local_tools")
        self.geometry("920x620")
        self.minsize(720, 480)
        self._build()

    def _build(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ── Sidebar ────────────────────────────────────────────────────
        sidebar = ctk.CTkFrame(self, fg_color=BG_PANEL, corner_radius=0, width=180)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        sidebar.grid_rowconfigure(20, weight=1)
        sidebar.grid_columnconfigure(0, weight=1)

        logo_f = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_f.grid(row=0, column=0, padx=16, pady=(20, 4), sticky="w")
        _label(logo_f, "⬡ local_tools", font=("Courier New", 12, "bold"),
               color=ACCENT).pack(anchor="w")
        _label(logo_f, "power user toolkit", font=FONT_MONO_SM,
               color=TEXT_DIM).pack(anchor="w")

        ctk.CTkFrame(sidebar, fg_color=BORDER, height=1, corner_radius=0).grid(
            row=1, column=0, sticky="ew", padx=12, pady=(8, 12))

        nav_items = [
            ("autoclicker",     "01  AUTOCLICKER"),
            ("stopwatch",       "02  STOPWATCH"),
            ("timer",           "03  TIMER"),
            ("textreplacement", "04  TEXT REPLACE"),
        ]

        self._nav_btns = {}
        self._frames   = {}

        for i, (key, label) in enumerate(nav_items, start=2):
            btn = ctk.CTkButton(
                sidebar, text=label, command=lambda k=key: self._show(k),
                fg_color="transparent", hover_color=BG_CARD,
                text_color=TEXT_DIM, font=("Courier New", 10),
                anchor="w", corner_radius=4, height=36,
            )
            btn.grid(row=i, column=0, padx=8, pady=2, sticky="ew")
            self._nav_btns[key] = btn

        _label(sidebar, "v0.1.0", font=FONT_MONO_SM, color=TEXT_MUTED).grid(
            row=21, column=0, padx=16, pady=(0, 14), sticky="w")

        # ── Main area ──────────────────────────────────────────────────
        main = ctk.CTkFrame(self, fg_color=BG_BASE, corner_radius=0)
        main.grid(row=0, column=1, sticky="nsew")
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(0, weight=1)

        self._frames["autoclicker"]     = AutoClickerFrame(main, self.cog_registry.get("autoclicker"))
        self._frames["stopwatch"]       = StopwatchFrame(main, self.cog_registry.get("stopwatch"))
        self._frames["timer"]           = TimerFrame(main, self.cog_registry.get("timer"))
        self._frames["textreplacement"] = TextReplaceFrame(main, self.cog_registry.get("textreplacement"))

        for f in self._frames.values():
            f.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)

        self._show("autoclicker")

    def _show(self, key: str):
        for k, btn in self._nav_btns.items():
            btn.configure(
                fg_color=BG_CARD if k == key else "transparent",
                text_color=ACCENT if k == key else TEXT_DIM,
            )
        self._frames[key].tkraise()


# ── Base Frame ───────────────────────────────────────────────────────────

class _CogFrame(ctk.CTkFrame):
    def __init__(self, parent, cog):
        super().__init__(parent, fg_color="transparent", corner_radius=0)
        self.cog = cog
        self.grid_columnconfigure(0, weight=1)
        self._build()

    def _build(self):
        raise NotImplementedError

    def _page_title(self, text: str, subtitle: str = "") -> ctk.CTkFrame:
        f = ctk.CTkFrame(self, fg_color="transparent")
        _label(f, text, font=FONT_TITLE, color=TEXT_PRIMARY).pack(anchor="w")
        if subtitle:
            _label(f, subtitle, font=FONT_UI_SM, color=TEXT_DIM).pack(anchor="w", pady=(2, 0))
        return f


# ── AutoClicker ──────────────────────────────────────────────────────────

class AutoClickerFrame(_CogFrame):
    def _build(self):
        self._page_title("AutoClicker", "Simulate repeated mouse clicks").grid(
            row=0, column=0, sticky="w", pady=(0, 16))

        card = _card(self)
        card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        card.grid_columnconfigure((0, 1), weight=1)

        _label(card, "INTERVAL (seconds)", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=0, padx=16, pady=(16, 4), sticky="w")
        self.interval_var = ctk.StringVar(value="1.0")
        _entry(card, self.interval_var, width=120).grid(
            row=1, column=0, padx=16, pady=(0, 16), sticky="w")

        _label(card, "BUTTON", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=1, padx=16, pady=(16, 4), sticky="w")
        self.button_var = ctk.StringVar(value="Left")
        ctk.CTkOptionMenu(
            card, variable=self.button_var, values=["Left", "Middle", "Right"],
            fg_color=BG_INPUT, button_color=ACCENT, button_hover_color=ACCENT_DIM,
            text_color=TEXT_PRIMARY, font=FONT_NAV, corner_radius=4, width=120,
        ).grid(row=1, column=1, padx=16, pady=(0, 16), sticky="w")

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.grid(row=2, column=0, sticky="w", pady=(0, 12))
        _btn(btn_row, "▶  START", self._start).pack(side="left", padx=(0, 8))
        _ghost_btn(btn_row, "■  STOP", self._stop).pack(side="left")

        status_card = _card(self)
        status_card.grid(row=3, column=0, sticky="ew")
        self.status_lbl = _label(status_card, "Stopped", font=FONT_MONO, color=TEXT_DIM)
        self.status_lbl.pack(padx=16, pady=12, anchor="w")

    def _start(self):
        if not self.cog: return
        btn_map = {"Left": 1, "Middle": 2, "Right": 3}
        try: interval = float(self.interval_var.get())
        except ValueError: interval = 1.0
        self.cog.run(interval=interval, button=btn_map[self.button_var.get()])
        self.status_lbl.configure(text=self.cog.status(), text_color=ACCENT)

    def _stop(self):
        if self.cog: self.cog.stop()
        self.status_lbl.configure(
            text=self.cog.status() if self.cog else "Stopped", text_color=TEXT_DIM)


# ── Stopwatch ────────────────────────────────────────────────────────────

class StopwatchFrame(_CogFrame):
    def _build(self):
        self._page_title("Stopwatch", "Precision timer with lap tracking").grid(
            row=0, column=0, sticky="w", pady=(0, 16))

        clock_card = _card(self)
        clock_card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        clock_card.grid_columnconfigure(0, weight=1)

        self.time_lbl = _label(clock_card, "00:00.00", font=FONT_MONO_LG)
        self.time_lbl.grid(row=0, column=0, pady=(24, 4))

        self.state_lbl = _label(clock_card, "STOPPED", font=FONT_MONO_SM, color=TEXT_DIM)
        self.state_lbl.grid(row=1, column=0, pady=(0, 20))

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.grid(row=2, column=0, sticky="w", pady=(0, 12))
        _btn(btn_row, "▶  START",  self._start, width=100).pack(side="left", padx=(0, 6))
        _ghost_btn(btn_row, "⏸  PAUSE",  self._stop,  width=100).pack(side="left", padx=(0, 6))
        _ghost_btn(btn_row, "◉  LAP",    self._lap,   width=100).pack(side="left", padx=(0, 6))
        _danger_btn(btn_row, "↺  RESET", self._reset, width=100).pack(side="left")

        _section_header(self, "LAPS").grid(row=3, column=0, sticky="ew", pady=(0, 6))

        lap_card = _card(self)
        lap_card.grid(row=4, column=0, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.laps_box = ctk.CTkTextbox(
            lap_card, fg_color="transparent", text_color=TEXT_PRIMARY,
            font=FONT_MONO, border_width=0, height=160,
        )
        self.laps_box.pack(fill="both", expand=True, padx=12, pady=8)
        self._tick()

    def _tick(self):
        if self.cog:
            e = self.cog.elapsed
            m, s = int(e // 60), e % 60
            self.time_lbl.configure(text=f"{m:02}:{s:05.2f}")
            if self.cog.is_running:
                self.state_lbl.configure(text="● RUNNING", text_color=ACCENT)
            else:
                self.state_lbl.configure(text="STOPPED", text_color=TEXT_DIM)
        self.after(80, self._tick)

    def _start(self):
        if self.cog: self.cog.run()

    def _stop(self):
        if self.cog: self.cog.stop()

    def _lap(self):
        if not self.cog: return
        t = self.cog.lap()
        n = len(self.cog.laps)
        m, s = int(t // 60), t % 60
        self.laps_box.insert("end", f"  LAP {n:02}    {m:02}:{s:05.2f}\n")
        self.laps_box.see("end")

    def _reset(self):
        if self.cog: self.cog.reset()
        self.laps_box.delete("1.0", "end")
        self.time_lbl.configure(text="00:00.00")


# ── Timer ────────────────────────────────────────────────────────────────

class TimerFrame(_CogFrame):
    def _build(self):
        self._page_title("Timer", "Multiple named countdown timers").grid(
            row=0, column=0, sticky="w", pady=(0, 16))

        config_card = _card(self)
        config_card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        config_card.grid_columnconfigure((0, 1), weight=1)

        _label(config_card, "DURATION (seconds)", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=0, padx=16, pady=(16, 4), sticky="w")
        self.duration_var = ctk.StringVar(value="60")
        _entry(config_card, self.duration_var, width=140).grid(
            row=1, column=0, padx=16, pady=(0, 16), sticky="w")

        _label(config_card, "LABEL", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=1, padx=16, pady=(16, 4), sticky="w")
        self.label_var = ctk.StringVar(value="timer")
        _entry(config_card, self.label_var, width=140).grid(
            row=1, column=1, padx=16, pady=(0, 16), sticky="w")

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.grid(row=2, column=0, sticky="w", pady=(0, 12))
        _btn(btn_row, "▶  START", self._start).pack(side="left", padx=(0, 8))
        _danger_btn(btn_row, "■  STOP ALL", self._stop_all, width=120).pack(side="left")

        _section_header(self, "ACTIVE TIMERS").grid(
            row=3, column=0, sticky="ew", pady=(0, 6))

        status_card = _card(self)
        status_card.grid(row=4, column=0, sticky="ew")
        self.status_lbl = _label(status_card, "No active timers",
                                  font=FONT_MONO, color=TEXT_DIM)
        self.status_lbl.pack(padx=16, pady=16, anchor="w")
        self._tick()

    def _tick(self):
        if self.cog:
            self.status_lbl.configure(
                text=self.cog.status(),
                text_color=ACCENT if self.cog.active_timers else TEXT_DIM,
            )
        self.after(500, self._tick)

    def _start(self):
        if not self.cog: return
        try: duration = float(self.duration_var.get())
        except ValueError: duration = 60.0
        self.cog.run(duration=duration, label=self.label_var.get() or "timer")

    def _stop_all(self):
        if self.cog: self.cog.stop()


# ── Text Replacement ─────────────────────────────────────────────────────

class TextReplaceFrame(_CogFrame):
    def _build(self):
        self._page_title("Text Replacement",
                          "Type a trigger phrase — it gets replaced automatically").grid(
            row=0, column=0, sticky="w", pady=(0, 16))

        add_card = _card(self)
        add_card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        add_card.grid_columnconfigure((0, 1), weight=1)

        _label(add_card, "TRIGGER PHRASE", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=0, padx=16, pady=(16, 4), sticky="w")
        self.trigger_var = ctk.StringVar()
        _entry(add_card, self.trigger_var, placeholder="e.g.  brb").grid(
            row=1, column=0, padx=16, pady=(0, 16), sticky="ew")

        _label(add_card, "REPLACEMENT TEXT", font=FONT_MONO_SM, color=TEXT_DIM).grid(
            row=0, column=1, padx=16, pady=(16, 4), sticky="w")
        self.replacement_var = ctk.StringVar()
        _entry(add_card, self.replacement_var, placeholder="e.g.  be right back").grid(
            row=1, column=1, padx=16, pady=(0, 16), sticky="ew")

        _btn(add_card, "+ ADD RULE", self._add, width=140).grid(
            row=2, column=0, columnspan=2, padx=16, pady=(0, 16), sticky="w")

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.grid(row=2, column=0, sticky="w", pady=(0, 12))
        _btn(btn_row, "▶  START", self._start).pack(side="left", padx=(0, 8))
        _ghost_btn(btn_row, "■  STOP", self._stop).pack(side="left")

        _section_header(self, "ACTIVE RULES").grid(
            row=3, column=0, sticky="ew", pady=(0, 6))

        rules_card = _card(self)
        rules_card.grid(row=4, column=0, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.rules_box = ctk.CTkTextbox(
            rules_card, fg_color="transparent", text_color=TEXT_PRIMARY,
            font=FONT_MONO, border_width=0, height=160,
        )
        self.rules_box.pack(fill="both", expand=True, padx=12, pady=8)

        self.status_lbl = _label(self, "", font=FONT_MONO_SM, color=TEXT_DIM)
        self.status_lbl.grid(row=5, column=0, sticky="w", pady=(8, 0))

    def _add(self):
        if not self.cog: return
        t = self.trigger_var.get().strip()
        r = self.replacement_var.get()
        if not t: return
        self.cog.add_replacement(t, r)
        self.trigger_var.set("")
        self.replacement_var.set("")
        self._refresh_rules()

    def _refresh_rules(self):
        self.rules_box.delete("1.0", "end")
        for t, r in self.cog.replacements.items():
            self.rules_box.insert("end", f"  {t!r:<20} →  {r!r}\n")

    def _start(self):
        if self.cog: self.cog.run()
        self.status_lbl.configure(
            text=self.cog.status() if self.cog else "", text_color=ACCENT)

    def _stop(self):
        if self.cog: self.cog.stop()
        self.status_lbl.configure(
            text=self.cog.status() if self.cog else "", text_color=TEXT_DIM)


# ── Entry ────────────────────────────────────────────────────────────────

def launch_gui(cog_registry: dict):
    app = LocalToolsApp(cog_registry)
    app.mainloop()