import numpy as np

grid=[[1,0,4,2,0,7,9,8,0],
       [0,8,0,0,0,0,6,0,2],
       [6,0,0,8,0,3,0,0,7],
       [0,0,0,9,4,1,0,6,0],
       [3,0,0,0,0,0,0,0,9],
       [0,7,0,6,3,5,0,0,0],
       [4,0,0,5,0,2,0,0,1],
       [2,0,7,0,0,0,0,9,0],
       [0,5,9,1,0,4,3,0,6]]
def possible(row,column,number):
    global grid
    #checks the row
    for i in range(0,9):
        if grid[row][i]==number:
            return False
    #checks the column
    for i in range(0,9):
        if grid[i][column]==number:
            return False
    row=row//3
    column=column//3
    if row==1:
        row=3
    elif row==2:
        row=6
    if column==1:
        column=3
    elif column==2:
        column=6
    #checks 3X3 square grid
    for i in range(row,row+3):
        for j in range(column,column+3):
            if grid[i][j]==number:
                return False
    
    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column]==0:
                for number in range(1,10):
                    if possible(row,column,number):
                        grid[row][column]=number
                        solve()
                        grid[row][column]=0
                return 
    print(np.matrix(grid))
    

solve()



            

        
    