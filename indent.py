def fix_indent(input_file):
    output_file = []
    current_indent = 0

    for line in input_file.split('\n'):
        line = line.strip()
        if line.startswith(('pass', 'print', 'return')):
            output_file.append(' ' * (current_indent + 4) + line)
        else:
            line.startswith('def')
            output_file.append(line) 
    return '\n'.join(output_file)

def process_file(input_file_path, output_file_path):
    # https://www.w3schools.com/python/python_file_open.asp
    with open(input_file_path, 'r') as file:
        input_code = file.read()

    corrected_code = fix_indent(input_code)

    # https://www.w3schools.com/python/python_file_write.asp
    # Generate output file path by appending '_corrected' before the file extension

    with open(output_file_path, 'w') as file:
        file.write(corrected_code)
