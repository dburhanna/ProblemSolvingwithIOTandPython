# Test 2 question

grid = [[113,4,8],[5,9,112],[109,1,5],[-12,108,107],[202,99,239]]

def max_in_row_and_grid(grid):
    new_grid=[]
    max_in_grid = 0
    for row in grid:
        max_col_in_row = 0
        for col in row:
            if col > max_col_in_row:
                max_col_in_row=col
        new_grid.append(max_col_in_row)
        if max_col_in_row > max_in_grid:
            max_in_grid = max_col_in_row
    new_grid.append(max_in_grid)
    return new_grid

print(max_in_row_and_grid(grid))
