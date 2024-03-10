import tkinter as tk
from tkinter import filedialog
import functionHeader
import indent
import printcounter
import time
import os.path

class MenuWindow:
    def __init__(self, parent):
        self.output_label = None
        self.file_path = None
        self.display_button = None
        self.parent = parent
        self.parent.title("Python Checker")
        self.parent.geometry("500x400")

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
        self.file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if self.file_path:
            self.file_label.config(text="Selected file: " + self.file_path)
            self.display_button = tk.Button(self.menu_frame, text="Run PyCheck", command=self.check_file)
            self.display_button.pack(pady=5, anchor="center")

    def check_file(self):
        # instantiate needed variables
        timestr = time.strftime("%Y%m%d-%H%M%S")
        output_code_path = "correctedCode.py"
        input_code_path = self.file_path

        # Process the original code file
        functionHeader.process_file(input_code_path, output_code_path)
        indent.process_file(output_code_path, output_code_path)
        count = printcounter.count_print_keywords(output_code_path)

        txt = open(f"PyCheck_Output_{timestr}.txt", 'w')

        with open(input_code_path, 'r') as file:
            for line in file:
                txt.write(line)

        txt.write("\n")

        with open(output_code_path, 'r') as file:
            for line in file:
                txt.write(line)

        txt.write("\n")

        txt.write(f"\n # Print keyword was used {count} times!")

        if txt:
            self.output_label = tk.Label(self.menu_frame, text="", wraplength=300)
            self.output_label.config(text="Output file is here: " + os.path.abspath(txt.name))
            self.output_label.pack(pady=5, anchor="center")
            txt.close()
        else:
            print("Error creating .txt output!!!")


def main():
    root = tk.Tk()
    app = MenuWindow(root)
    root.mainloop()