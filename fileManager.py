import tkinter as tk
from tkinter import filedialog


def selectfile():
    # create a root window
    root = tk.Tk()
    root.withdraw()

    # open the file dialog box
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Python files", "*.py*"), ("all files", "*.*")))

    return file_path


class FileManager:
    file = ""
    file_path = ""

    def __init__(self, name: str):
        self.name = name

    def openfile(self):
        self.file = open(self.name, "a")

    def closefile(self):
        self.file.close()

    def writefile(self, text):
        self.file.write(text)

    def count(self, text: str):
        self.closefile()
        read = open(self.name, "r")
        count: int = 0
        for line in read:
            if text in line:
                count += 1
        read.close()
        return count

    def selectfile(self):

        # create a root window
        root = tk.Tk()
        root.withdraw()

        # open the file dialog box
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                    filetypes=(("Python files", "*.py*"), ("all files", "*.*")))

        return self.file_path
