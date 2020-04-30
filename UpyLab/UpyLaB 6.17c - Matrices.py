def check_regions(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])
         if len(temp) != len(set(temp)): # On vérifie si une valeur se répète.
             return False
  return True



print(check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8], # retourne True
              [1, 7, 8, 3, 2, 5, 6, 4, 9],
              [2, 5, 4, 6, 8, 9, 7, 3, 1],
              [8, 2, 1, 4, 3, 7, 5, 9, 6],
              [4, 9, 6, 8, 5, 2, 3, 1, 7],
              [7, 3, 5, 9, 6, 1, 8, 2, 4],
              [5, 8, 9, 7, 1, 3, 4, 6, 2],
              [3, 1, 7, 2, 4, 6, 9, 8, 5],
              [6, 4, 2, 5, 9, 8, 1, 7, 3]]))