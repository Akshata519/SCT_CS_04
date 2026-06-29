import tkinter as tk
from datetime import datetime

LOG_FILE = "key_log.txt"

def log_key(event):
    key = event.keysym
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} - {key}\n")

root = tk.Tk()
root.title("Keyboard Event Logger")
root.geometry("500x250")

label = tk.Label(
    root,
    text="Click inside this window and type.\nOnly keys pressed in this window will be logged.",
    font=("Arial", 12),
)
label.pack(pady=20)

text = tk.Text(root, width=50, height=6)
text.pack()

text.bind("<Key>", log_key)
text.focus_set()

root.mainloop()
