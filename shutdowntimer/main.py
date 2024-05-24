import tkinter as tk
import time
import threading
import os


class ShutdownTimer:
    def __init__(self, root, test=False, time_options=(1, 5, 10, 20, 30, 40, 60, 120)):
        self.test = test
        self.root = root
        self.root.title("Shutdown Timer")

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.timer_label.pack(expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.time_options = time_options
        self.create_buttons()

        self.time_left = 600  # Initial timer set to 10 minutes (600 seconds)
        self.running = True

        self.update_timer()
        self.start_shutdown_thread()

    def create_buttons(self):
        for minutes in self.time_options:
            button = tk.Button(
                self.button_frame,
                text=f"{minutes} mins",
                command=lambda m=minutes: self.reset_timer(m),
            )
            button.pack(side=tk.LEFT, padx=5)

    def reset_timer(self, minutes):
        self.time_left = minutes * 60  # Convert minutes to seconds

    def update_timer(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            remaining = f"{minutes:02}:{seconds:02}"
            self.timer_label.config(text=remaining)
            print(remaining)
            self.time_left -= 1

            if self.time_left == 30:
                self.root.lift()
                self.root.attributes("-topmost", True)
                self.root.after_idle(self.root.attributes, "-topmost", False)

        else:
            self.timer_label.config(text="Shutting down...")
            self.shutdown()

        if self.running:
            self.root.after(1000, self.update_timer)

    def shutdown(self):
        if self.test:
            print(os.system("ls"))
        else:
            print(os.system("shutdown /s /t 1"))

    def start_shutdown_thread(self):
        thread = threading.Thread(target=self.shutdown_after_timer)
        thread.start()

    def shutdown_after_timer(self):
        while self.time_left > 0:
            time.sleep(1)
        self.shutdown()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x200")  # Adjusted window size to accommodate buttons
    root.eval("tk::PlaceWindow . center")  # Center window
    app = ShutdownTimer(root, test=True)
    root.mainloop()
