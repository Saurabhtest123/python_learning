# Number of rows in the pattern
num_rows = 10

# Outer loop for each row
for i in range(1, num_rows + 1):
    # Inner loop for each column in the current row
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()
