import ast


def count_print_keywords(file_path):
    try:
        with open(file_path, 'r') as file:
            count = 0
            for line in file:
                if line.count("print(") > 0:
                    count += 1
        return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1

# Printing the count:
#     input_file_path = file_path  # replace with where you want it to print
#     print_count = count_print_keywords(file_path)
#     if print_count >= 0:
#         print(f"The keyword 'print' is used {print_count} times in the file.")