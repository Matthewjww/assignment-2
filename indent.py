def fix_indent(input_file):
    output_file = ""  
    current_indent = 0  # Tracking indentation level 

    # Splits the lines into substrings so each line can be evaluated 
    # https://www.w3schools.com/python/ref_string_split.asp
    lines = input_file.split('\n')

    # For loop with if else statements check each line
    # https://www.almabetter.com/bytes/tutorials/python/indentation-in-python
    for line in lines:
        # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/strip/python-string-strip/
        strip_line = line.strip()  # Remove leading and trailing whitespace
        leading_spaces = len(line) - len(strip_line)  # Calculating the leading spaces 
        # Python uses four spaces as default indentation spaces
        # https://www.scaler.com/topics/python/indentation-in-python/
        if strip_line:
            # Indentation level increases
            if strip_line[0] in ['def', 'class', 'for', 'while', 'if', 'elif', 'else', 'try', 'except', 'finally']:
                output_file += ' ' * current_indent + strip_line + '\n'
                current_indent += 4
            # # Indentation level stays the same 
            elif strip_line[0] in ['return', 'pass', 'break', 'continue']:
                output_file += ' ' * current_indent + strip_line + '\n'
            # Indentation level decreases
            elif strip_line[0] == 'else':
                current_indent -= 4
                output_file += ' ' * current_indent + strip_line + '\n'
                current_indent += 4
            # Keeps the indentation level the same for other lines
            else:
                output_file += ' ' * current_indent + strip_line + '\n'
        # If the line is empty, just add it to the fixed program
        else:
            output_file += '\n'
    # returns output 
    return output_file
