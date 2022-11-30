import numpy as np 

def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None,None

def is_valid(puzzle,guess,row,col):
    #check rows
    r_val=puzzle[row]
    if guess in r_val:
        return False

    #check cols
    c_val=[]
    for i in range(9):
        c_val.append(puzzle[i][col])
    if guess in c_val:
        return False

    #check the little squares
    #and iterate over the 3 values in row and col
    row_start=(row // 3) * 3
    col_start=(col // 3) * 3

    for r in range(row_start,row_start+3):
        for c in range (col_start,col_start+3):
            if puzzle[r][c] == guess:
                return False    
    
    #if we've reached here , return true
    return True

def solve_sudoku(puzzle):

    #1 choose somewhere on the puzzle to make a guess
    row,col= find_next_empty(puzzle)

    #1.1 if there is no place left
    if row is None:
        return True

    #2 if there is a place left then we make a guess and check if it is valid
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            #3.1 if its valid, then place the guess on the puzzle
            puzzle[row][col]=guess
            #4 using recursion 
            if solve_sudoku(puzzle):
                return True
        
        #5 if not valid  or guess does not solve
        puzzle[row][col] = 0 #reset

    #6 if none of the numbers that we try worked
    return False
    
def print_matrix(puzzle):
    for i in range(9):
        for j in range(9):
            print (puzzle[i][j],end=" ")
        print()

puzzle=[]
print("\nPlease use 0 in place of blank spaces")
for i in range(9):
    row=list(map(int, input().split()))
    puzzle.append(row)
print("\nThe Unsolved puzzle is as follows: ")
print_matrix(puzzle)

print("--------------------------------")

if solve_sudoku(puzzle)== True:
    print("SOLUTION EXISTS! Its is as follows: ")
    print_matrix(puzzle)
else:
    print("Solving failed.")

    
    
    