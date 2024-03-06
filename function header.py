def fix_function_headers(code):
    corrected_lines = []
    # List of common misspellings of 'def'
    misspellings = ["deff", "defi", "dfe", "df"]

    for line in code.split("\n"):
        stripped_line = line.strip()

        # Check for and correct common misspellings of 'def'
        for misspelling in misspellings:
            if stripped_line.startswith(misspelling + " "):
                line = line.replace(misspelling, "def", 1)
                break

        # Detect missing parentheses and colons
        """ This code was written with help from OpenAI's ChatGPT https://chat.openai.com/ """
        if stripped_line.startswith("def "):
            if ":" in stripped_line and "(" not in stripped_line:
                colon_index = line.find(":")
                line = line[:colon_index] + "()" + line[colon_index:]
            elif ":" not in stripped_line and "(" not in stripped_line:
                func_name_end = stripped_line.find(" ", 4)
                if func_name_end == -1:
                    func_name_end = len(stripped_line)
                line = line[:func_name_end] + "()" + line[func_name_end:] + ":"
            elif stripped_line.endswith(")") and ":" not in stripped_line:
                line += ":"
        """ This code was written with help from OpenAI's ChatGPT https://chat.openai.com/ """

        corrected_lines.append(line)

    corrected_code = "\n".join(corrected_lines)
    return corrected_code


def process_file(input_file_path):
    # https://www.w3schools.com/python/python_file_open.asp
    with open(input_file_path, 'r') as file:
        input_code = file.read()

    corrected_code = fix_function_headers(input_code)

    # https://www.w3schools.com/python/python_file_write.asp
    # Generate output file path by appending '_corrected' before the file extension
    output_file_path = input_file_path.rsplit('.', 1)[0] + '_corrected.' + input_file_path.rsplit('.', 1)[1]

    with open(output_file_path, 'w') as file:
        file.write(corrected_code)

    print(f"Corrected code has been written to {output_file_path}")


if __name__ == "__main__":
    input_file_path = input("Enter the path to the input Python file: ")
    process_file(input_file_path)
