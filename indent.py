def fix_indent(input_file):
    output_file = []
    # Tracking indentation level 
    current_indent = 0 
    # Words that should have indentation afterwards 
    keywords = ['def', 'class', 'for', 'while', 'if', 'elif', 'else', 'try', 'except', 'finally']
    
    # Splits the lines into substrings so each line can be evaluated 
    # https://www.w3schools.com/python/ref_string_split.asp
    for line in input_file.split('\n'):
        # For loop checks each line
        # https://www.almabetter.com/bytes/tutorials/python/indentation-in-python
        # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/strip/python-string-strip/
        line = line.strip()
        # Indentation level increases
        if any(line.startswith(keyword) for keyword in keywords):
            output_file.append(' ' * current_indent + line)
            current_indent += 4  # Python uses four spaces as default indentation spaces
        # Indentation level decreases
        else:
            output_file.append(' ' * current_indent + line)
            if line.endswith(')') or line.endswith(']'):
                current_indent -= 4
            if current_indent < 0:
                current_indent -= 0 # Indentation doesn't go negative 
    # joins the lines
    return '\n'.join(output_file)

# Example usage: TAKE OUT FOR PROJECT 
if __name__ == "__main__":
    input_file = """
def example_function():
if True:
print("This line is indented correctly.")
else:
("This line should be indented further.")
"""
    output_file = fix_indent(input_file)
    print(output_file)
