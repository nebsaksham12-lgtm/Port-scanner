import tkinter as tk

BG_COLOR = "#121212"
FG_COLOR = "#FFFFFF"
ACCENT_COLOR = "#1DB954"
FONT = ("Helvetica", 10)

mainwindow = tk.Tk()
mainwindow.title("Music GUI")
mainwindow.configure(bg=BG_COLOR)
mainwindow.geometry("300x200")
name_label = tk.Label(mainwindow, text="Song Name", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 12, "bold"))
name_label.pack(pady=10)
controls_frame = tk.Frame(mainwindow, bg=BG_COLOR)
controls_frame.pack(pady=5)

play_button = tk.Button(controls_frame, text="▶", bg=ACCENT_COLOR, fg=FG_COLOR, font=FONT, width=5)
play_button.grid(row=0, column=0, padx=5)

pause_button = tk.Button(controls_frame, text="⏸", bg=ACCENT_COLOR, fg=FG_COLOR, font=FONT, width=5)
pause_button.grid(row=0, column=1, padx=5)

forward_button = tk.Button(controls_frame, text="⏭", bg=ACCENT_COLOR, fg=FG_COLOR, font=FONT, width=5)
forward_button.grid(row=0, column=2, padx=5)

volume_slider = tk.Scale(mainwindow, from_=0, to=100, orient=tk.HORIZONTAL, bg=BG_COLOR, fg=FG_COLOR,
                         highlightbackground=BG_COLOR, troughcolor="#404040", font=FONT, label="Volume")
volume_slider.pack(fill="x", padx=20)

progress_bar = tk.Scale(mainwindow, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=0, bg=BG_COLOR, fg=FG_COLOR,
                        highlightbackground=BG_COLOR, troughcolor="#404040", font=FONT)
progress_bar.pack(fill="x", padx=20)

time_label = tk.Label(mainwindow, text="0:00", bg=BG_COLOR, fg=FG_COLOR, font=FONT)
time_label.pack(pady=5)

mainwindow.mainloop()
