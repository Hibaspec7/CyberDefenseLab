"""
attack_lab.py - Window 1: Attack Lab with live terminal, timer bar, threat brief, streak HUD
Cyber-Attack Simulator & Defense Lab  v3
"""
import tkinter as tk
import theme as T


class AttackLabWindow(tk.Frame):
    def __init__(self, master, attack_data, round_num, total_rounds,
                 difficulty_settings, on_open_defense, on_breach,
                 current_streak=0, session_score=0):
        super().__init__(master, bg=T.BG_DARK)
        self.atk          = attack_data
        self.round_num    = round_num
        self.total_rounds = total_rounds
        self.diff         = difficulty_settings
        self.on_open_defense = on_open_defense
        self.on_breach    = on_breach
        self.streak       = current_streak
        self.session_score= session_score

        self.time_left   = difficulty_settings["time"]
        self._timer_job  = None
        self._log_job    = None
        self._log_lines  = self.atk.get("logs","").split("|")
        self._log_idx    = 0
        self._breached   = False
        self._build()
        self._start_log()
        self._tick()

    def _build(self):
        self.pack(fill="both", expand=True)

        # ── Header strip ────────────────────────────────────────────────────
        top = tk.Frame(self, bg=T.BG_PANEL,
                       highlightthickness=1, highlightbackground=T.BORDER_PANEL)
        top.pack(fill="x", padx=12, pady=(12,0))

        atype = self.atk["attack_type"]
        cfg   = T.ATTACK_COLORS.get(atype, {"fg":T.TEXT})
        lbl   = T.ATTACK_LABELS.get(atype, atype.upper())
        title = self.atk.get("title","")
        full_lbl = f"{lbl}  —  {title}" if title else lbl

        tk.Label(top, text=full_lbl, bg=T.BG_PANEL, fg=cfg["fg"],
                 font=("Courier New",12,"bold")).pack(side="left",padx=12,pady=8)

        # Round indicator
        dots = ""
        for i in range(self.total_rounds):
            dots += ("[*] " if i < self.round_num else "[ ] ")
        tk.Label(top, text=dots.strip(), bg=T.BG_PANEL, fg=T.MUTED,
                 font=("Courier New",9)).pack(side="right",padx=12)