# Pattern Drawing using while loops and nested for loops

size = int(input("Enter the size of the pattern: "))  # Get user input
row = 0  # Initialize row counter

while row < size:  # Outer loop for rows
    for _ in range(size):  # Inner loop for columns
        print("*", end="")  # Print asterisk without a newline
    print()  # Print a newline after finishing a row
    row += 1  # Increment row counter
