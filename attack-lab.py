import tkinter as tk
import theme as T


class AttackLabWindow(tk.Frame):
    def __init__(self, master, attack_data, round_num, total_rounds,
                 difficulty_settings, on_open_defense, on_breach):
        super().__init__(master, bg=T.BG_DARK)
        self.atk          = attack_data
        self.round_num    = round_num
        self.total_rounds = total_rounds
        self.diff         = difficulty_settings
        self.on_open_defense = on_open_defense
        self.on_breach    = on_breach

        self.time_left  = difficulty_settings["time"]
        self._timer_job = None
        self._log_job   = None
        self._log_lines = self._parse_logs()
        self._log_idx   = 0
        self._breached  = False

        self._build()
        self._start_log_animation()
        self._start_timer()

    # ── Log parsing ────────────────────────────────────────────────────────────

    def _parse_logs(self):
        raw = self.atk.get("logs", "")
        return [l.strip() for l in raw.split("|") if l.strip()]

    # ── Build UI ───────────────────────────────────────────────────────────────

    def _build(self):
        self.pack(fill="both", expand=True)

        atype = self.atk["attack_type"]
        cfg   = T.ATTACK_COLORS.get(atype, {"fg": T.TEXT})
        label = T.ATTACK_LABELS.get(atype, atype.upper())
        title = self.atk.get("title", label)
        
        # ── Top bar ────────────────────────────────────────────────────────
        top = tk.Frame(self, bg=T.BG_PANEL,
                       highlightthickness=1, highlightbackground=T.BORDER_PANEL)
        top.pack(fill="x", padx=16, pady=(16, 0))

        tk.Label(top, text=f"{label}  —  {title}",
                 bg=T.BG_PANEL, fg=cfg["fg"],
                 font=("Courier New", 12, "bold")).pack(side="left", padx=12, pady=8)

        tk.Label(top, text=f"Round {self.round_num}/{self.total_rounds}",
                 bg=T.BG_PANEL, fg=T.MUTED,
                 font=("Courier New", 10)).pack(side="right", padx=12)

        # ── Timer bar ──────────────────────────────────────────────────────
        timer_bg = tk.Frame(self, bg=T.BORDER_PANEL, height=4)
        timer_bg.pack(fill="x", padx=16, pady=(6, 0))
        self.timer_fill = tk.Frame(timer_bg, bg=T.GREEN, height=4)
        self.timer_fill.place(x=0, y=0, relwidth=1.0, height=4)

        self.timer_lbl = tk.Label(self, text=f"[T]  {self.time_left}s",
                                  bg=T.BG_DARK, fg=T.GREEN,
                                  font=("Courier New", 10, "bold"))
        self.timer_lbl.pack(anchor="e", padx=20)

        # ── Terminal box ───────────────────────────────────────────────────
        T.section_header(self, "  SYSTEM LOG — REAL-TIME THREAT FEED").pack(
            anchor="w", padx=20, pady=(6, 4))

        term_outer = tk.Frame(self, bg="#060a12",
                              highlightthickness=1,
                              highlightbackground=T.BORDER_GREEN)
        term_outer.pack(fill="x", padx=16, ipady=4)

        self.terminal = tk.Text(
            term_outer, bg="#060a12", fg=T.GREEN,
            font=("Courier New", 10), height=8,
            state="disabled", relief="flat", bd=0,
            insertbackground=T.GREEN, wrap="word")
        self.terminal.pack(fill="x", padx=8, pady=4)

        for tag, color in [("green", T.GREEN), ("red", T.RED),
                           ("amber", T.AMBER), ("cyan", T.CYAN),
                           ("muted", T.MUTED)]:
            self.terminal.tag_config(tag, foreground=color)