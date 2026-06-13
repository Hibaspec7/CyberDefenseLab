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