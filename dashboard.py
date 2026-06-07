import tkinter as tk
from tkinter import ttk

class DashboardWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber-Attack Simulator - Dashboard")
        self.root.geometry("900x650")
        
        # Hacker-style Dark Background Color
        self.root.configure(bg="#0d1117")
        
        # Main Title Label
        self.title_label = tk.Label(
            root, 
            text="SECURITY OFFICER DASHBOARD", 
            font=("Courier", 20, "bold"), 
            fg="#58a6ff", 
            bg="#0d1117"
        )
        self.title_label.pack(pady=20)

# Yeh code file ko direct run karne ke liye hai
if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardWindow(root)
    root.mainloop()