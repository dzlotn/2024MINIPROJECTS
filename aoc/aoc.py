def count_xmas_occurrences(grid):
    word = "XMAS"
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Directions: (dx, dy) pairs for 8 possible directions
    directions = [
        (1, 0),   # right
        (-1, 0),  # left
        (0, 1),   # down
        (0, -1),  # up
        (1, 1),   # down-right
        (-1, -1), # up-left
        (1, -1),  # down-left
        (-1, 1),  # up-right
    ]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                found = True
                for k in range(word_length):
                    x = i + k * dx
                    y = j + k * dy
                    if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[k]:
                        found = False
                        break
                if found:
                    count += 1

    return count



def count_xmas_occurrences(grid):
    count = 0
    rows = len(grid)
    print(rows)
    cols = len(grid[0]) if rows > 0 else 0
    print(cols)
    for i in range(rows - 2):  # Stop at rows - 2 to avoid index out of range
        for j in range(1, cols - 3):  # Start at 1 and stop at cols - 1
            # Check for the X-MAS pattern
            print(i,",",j)
            if (grid[i][j] == 'S' and
                grid[i][j - 1] == 'M' and
                grid[i][j + 1] == 'S' and
                grid[i + 1][j] == 'A' and
                grid[i + 2][j] == 'M' and
                grid[i + 2][j + 1] == 'S'):
                count += 1

    return count

# Open the file for reading
l1 = []
with open('aoc/aoc2.txt', 'r') as file:
    for line in file:
        l1.append(line.strip())  # Strip newline characters

# Count occurrences of "X-MAS"
result = count_xmas_occurrences(l1)
print("The pattern 'X-MAS' appears", result, "times.")

# # Open the file for reading
# l1 = []
# with open('aoc/aoc.txt', 'r') as file:
#     for line in file:
#         l1.append(str(line.strip()))
# print(l1)
# # Count occurrences of "XMAS"
# result = count_xmas_occurrences(l1)
# print("The word 'XMAS' appears", result, "times.")
