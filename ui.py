import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk
import functionHeader
import indent
import printcounter
import time
import os.path
import subprocess
import platform


class MenuWindow:
    def __init__(self, parent):
        self.output_label = None
        self.file_path = None
        self.display_button = None
        self.parent = parent
        self.parent.title("Python Checker")
        self.parent.geometry("500x400")

        self.menu_frame = ttk.Frame(self.parent)
        self.menu_frame.pack(expand=True)

        self.title_label = ttk.Label(self.menu_frame, text="Python Checker", font=("Helvetica", 18))
        self.title_label.pack(pady=10, anchor="center")
        self.instruction_label = tk.Label(self.menu_frame, text="Select a python file to check,"
                                                                " and correct, the indentation and method heading,"
                                                                " and check how many times you used print()",
                                          font=("Helvetica", 14), wraplength=200)
        self.instruction_label.pack(pady=10, anchor="center")

        self.button = ttk.Button(self.menu_frame, text="Select .py File", command=self.file_button_clicked)
        self.button.pack(pady=5, anchor="center")

        self.file_label = ttk.Label(self.menu_frame, text="", wraplength=300)
        self.file_label.pack(pady=5, anchor="center")

    def file_button_clicked(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if self.file_path:
            self.file_label.config(text="Selected file: " + self.file_path)
            self.display_button = ttk.Button(self.menu_frame, text="Run PyCheck", command=self.check_file)
            self.display_button.pack(pady=5, anchor="center")

    def open_file(self, file_path):
        if platform.system() == "Darwin":  # Check if running on macOS
            subprocess.Popen(["open", "-a", "TextEdit", file_path])
        else:
            subprocess.Popen(["open", file_path])

    def check_file(self):
        # Instantiate needed variables
        timestr = time.strftime("%Y%m%d-%H%M%S")
        output_code_path = "correctedCode.py"
        input_code_path = self.file_path

        # Process the original code file
        functionHeader.process_file(input_code_path, output_code_path)
        indent.process_file(output_code_path, output_code_path)
        count = printcounter.count_print_keywords(output_code_path)

        # Create .txt file for result
        txt = open(f"PyCheck_Output_{timestr}.txt", 'w')

        txt.write("#Original Code: \n \n")

        # Copy original file into .txt
        with open(input_code_path, 'r') as file:
            for line in file:
                txt.write(line)

        txt.write("\n \n#Corrected Code: \n \n")

        # Copy correctedCode (after methods ran to .txt)
        with open(output_code_path, 'r') as file:
            for line in file:
                txt.write(line)

        txt.write(f"\n \n #Print keyword was used {count} times! \n")

        # Update GUI with where the file is, and open the .txt file
        if txt:
            self.output_label = ttk.Label(self.menu_frame, text="", wraplength=300)
            txt_path = os.path.abspath(txt.name)
            self.output_label.config(text="Output file is here: " + txt_path)
            self.output_label.pack(pady=5, anchor="center")
            txt.close()
            self.open_file(txt_path)
        else:
            print("Error creating .txt output!!!")

# Runs menu window on loop (until closed)
def main():
    root = tk.Tk()
    app = MenuWindow(root)
    root.mainloop()
