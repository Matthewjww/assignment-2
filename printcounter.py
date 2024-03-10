
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
