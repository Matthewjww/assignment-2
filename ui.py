import tkinter as tk
from tkinter import filedialog


class MenuWindow:
    def __init__(self, parent):
        self.display_button = None
        self.parent = parent
        self.parent.title("Python Checker")
        self.parent.geometry("400x300")

        self.menu_frame = tk.Frame(self.parent)
        self.menu_frame.pack(expand=True)

        self.title_label = tk.Label(self.menu_frame, text="Python Checker", font=("Helvetica", 16))
        self.title_label.pack(pady=10, anchor="center")
        self.instruction_label = tk.Label(self.menu_frame, text="Select a python file to check,"
                                                                " and correct, the indentation and method heading,"
                                                                " and check how many times you used print()",
                                          font=("Helvetica", 12), wraplength=200)
        self.instruction_label.pack(pady=10, anchor="center")

        self.button = tk.Button(self.menu_frame, text="Select .py File", command=self.file_button_clicked)
        self.button.pack(pady=5, anchor="center")

        self.file_label = tk.Label(self.menu_frame, text="", wraplength=300)
        self.file_label.pack(pady=5, anchor="center")

    def file_button_clicked(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            self.file_label.config(text="Selected file: " + file_path)
            self.display_button = tk.Button(self.menu_frame, text="Run PyCheck", command=self.check_file)
            self.display_button.pack(pady=5, anchor="center")

    def check_file(self):
        # Placeholder function to demonstrate button functionality
        print("Displaying file...")
        # Add code from others
        # Add write to .txt file


def main():
    root = tk.Tk()
    app = MenuWindow(root)
    root.mainloop()