def print_diamond(rows):
    for i in range(1, rows + 1, 2):
        spaces = (rows - i) // 2
        print(" " * spaces + "*" * i + " " * spaces)



# Example: To print a diamond with 5 rows
print_diamond(5)
