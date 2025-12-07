"""
Validates sudoku rows.
"""
# Import literal_eval library to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
board = literal_eval(input())

def validate_sudoku_rows(board):
    # Write your code here
  result=[]
  for rows in board:
    repeat=False
    if len(rows)!=9:
      return 'Invalid board'
    for digit in rows:
      if rows.count(digit)>1:
        repeat= True
        break
    if repeat:
      result.append(False)
    else:
      result.append(True)
  return result


# Print the output
print(validate_sudoku_rows(board))
