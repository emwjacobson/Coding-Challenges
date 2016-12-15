import numpy as np

puzzle = np.array([             #This is an easy puzzle, and can be solved easily.
    [5,3,0,  0,7,0,  0,0,0],    #There is always at least 1 100% guaranteed move every turn
    [6,0,0,  1,9,5,  0,0,0],
    [0,9,8,  0,0,0,  0,6,0],

    [8,0,0,  0,6,0,  0,0,3],
    [4,0,0,  8,0,3,  0,0,1],
    [7,0,0,  0,2,0,  0,0,6],

    [0,6,0,  0,0,0,  2,8,0],
    [0,0,0,  4,1,9,  0,0,5],
    [0,0,0,  0,8,0,  0,7,9]])

# puzzle = np.array([           #You need to make assumptions for this puzzle, so it can
#     [6,0,2,0,0,0,5,0,0],      #not be solved by this program
#     [0,0,0,0,0,7,6,2,0],      #this could be solved by creating another array that contains
#     [0,0,7,0,0,1,0,8,0],      #an array of possible values for each position, and if
#     [0,0,0,0,0,8,0,0,9],      #a value ony appears once in a row,col,and pod, it can be assumed
#     [0,3,0,0,4,0,0,7,0],      #that that is the correct value
#     [4,0,0,1,0,0,0,0,0],
#     [0,6,0,5,0,0,7,0,0],
#     [0,7,5,3,0,0,0,0,0],
#     [0,0,3,0,0,0,4,0,2]
# ])

def isSolved():
    for row in puzzle:
        for col in row:
            if col == 0:
                return False
    return True

if __name__ == "__main__":
    while not isSolved():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    possible = [1,2,3,4,5,6,7,8,9]
                    for scan_col in range(9):           #This scans horiziontally and removes already used numbers
                        if puzzle[row][scan_col] in possible:
                            possible.remove(puzzle[row][scan_col])
                    for scan_row in range(9):           #This scans vertically and removes already used numbers
                        if puzzle[scan_row][col] in possible:
                            possible.remove(puzzle[scan_row][col])

                    #Here, I need to determine which "pod" the current number is in.  A "pod" being the 3x3 areas separeting the board
                    pod = int(col/3)+(3*int(row/3))
                    pod_nums = puzzle[3*int(pod/3):(3*int(pod/3))+3,3*(pod%3):(3*(pod%3))+3].reshape(9) #This gets all of the numbers in the respective pod
                    for num in pod_nums:
                        if num in possible:
                            possible.remove(num)
                    if len(possible) == 1:
                        puzzle[row][col] = possible[0]
    print(puzzle)
