"""
defense_screen.py - Window 2: Defense Terminal  v3
Dynamic widgets per attack type, combo display, streak feedback.
"""
import tkinter as tk
import random
import theme as T


class DefenseScreen(tk.Frame):
    def __init__(self, master, attack_data, game_controller, on_submit, on_next_round):
        super().__init__(master, bg=T.BG_DARK)
        self.atk           = attack_data
        self.gc            = game_controller
        self.on_submit     = on_submit
        self.on_next_round = on_next_round
        self._answered     = False
        self._ddos_decisions   = {}
        self._ddos_entry_vars  = {}
        self._build()

    def _build(self):
        self.pack(fill="both", expand=True)
        atype = self.atk["attack_type"]
        cfg   = T.ATTACK_COLORS.get(atype, {"fg": T.TEXT})

        top = tk.Frame(self, bg=T.BG_PANEL,
                       highlightthickness=1, highlightbackground=T.BORDER_AMBER)
        top.pack(fill="x", padx=12, pady=(12,0))

        tk.Label(top, text="// DEFENSE TERMINAL",
                 bg=T.BG_PANEL, fg=T.AMBER,
                 font=("Courier New",12,"bold")).pack(side="left",padx=12,pady=8)

        title = self.atk.get("title", T.ATTACK_LABELS.get(atype, atype))

        tk.Label(top, text=title,
                 bg=T.BG_PANEL,
                 fg=cfg["fg"],
                 font=("Courier New",10,"bold")).pack(side="right",padx=12)
        
                hud = tk.Frame(self, bg=T.BG_DARK)
        hud.pack(fill="x", padx=14, pady=(4,0))

        streak = self.gc.score_mgr.current_streak

        from score_manager import COMBO_MULTIPLIERS

        mult   = COMBO_MULTIPLIERS.get(min(streak+1, 5), 2.0)
        sc_col = T.GREEN if streak == 0 else (T.AMBER if streak < 3 else T.RED)

        tk.Label(hud,
                 text=f"Current Streak: {streak}",
                 bg=T.BG_DARK,
                 fg=sc_col,
                 font=("Courier New",9,"bold")).pack(side="left")

        tk.Label(hud,
                 text=f"   Next answer multiplier: x{mult:.1f}",
                 bg=T.BG_DARK,
                 fg=T.PURPLE,
                 font=("Courier New",9)).pack(side="left")

        hints     = self.gc.score_mgr.hints_remaining
        hint_cost = self.gc.score_mgr.settings["hint_cost"]

        self.hint_count_var = tk.StringVar(value=f"Hints: {hints}")

        tk.Label(hud,
                 textvariable=self.hint_count_var,
                 bg=T.BG_DARK,
                 fg=T.MUTED,
                 font=("Courier New",9)).pack(side="right", padx=4)

        self.hint_btn = T.styled_button(
            hud,
            f"HINT (-{hint_cost}pts)",
            self._use_hint,
            color=T.AMBER,
            font=("Courier New",9,"bold"),
            padx=8,
            pady=3)

        if self.gc.difficulty in ("expert",) or hints == 0:
            self.hint_btn.config(state="disabled", fg=T.MUTED)

        self.hint_btn.pack(side="right")