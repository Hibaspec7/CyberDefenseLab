"""
home_screen.py - Main menu with difficulty, daily challenge, stats preview, achievements
Cyber-Attack Simulator & Defense Lab  v3
"""
import tkinter as tk
import datetime
import database as db
import theme as T


class HomeScreen(tk.Frame):
    def __init__(self, master, user, on_start_game, on_view_dashboard, on_logout):
        super().__init__(master, bg=T.BG_DARK)
        self.user = user
        self.on_start_game = on_start_game
        self.on_view_dashboard = on_view_dashboard
        self.on_logout = on_logout
        self.selected_diff = tk.StringVar(value="beginner")
        self._build()

    def _build(self):
        self.pack(fill="both", expand=True)

        top = tk.Frame(
            self,
            bg=T.BG_PANEL,
            highlightthickness=1,
            highlightbackground=T.BORDER_PANEL
        )

        top.pack(fill="x", padx=12, pady=(12,0))

        tk.Label(
            top,
            text="[*] CYBER-ATTACK SIMULATOR & DEFENSE LAB",
            bg=T.BG_PANEL,
            fg=T.GREEN,
            font=("Courier New",12,"bold")
        ).pack(side="left", padx=12, pady=8)