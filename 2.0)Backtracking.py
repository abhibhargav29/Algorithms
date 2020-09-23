from math import sqrt

def printMatrix(Mat):
    for i in range(len(Mat)):
        print(" ".join(map(str, Mat[i])))

#Rat in a maze------------------------------------------------------------------------------------
n = int(input("Enter rows: "))
Maze = []
print("Draw Maze: ")
for i in range(n):
    Maze.append(list(map(int, input().split())))

def checkCell(i, j, Maze, n):
    if(i<n and j<n and Maze[i][j]==1):
        return True
    return False

def SolveMaze(Maze, n):
    solution = [[0 for i in range(n)] for j in range(n)]
    if(SolveMazeUtil(0, 0, solution, n, Maze)==False):
        return False
    else:
        printMatrix(solution)
        return True

def SolveMazeUtil(i, j, solution, n, Maze):
    if(i==n-1 and j==n-1 and checkCell(i,j,Maze,n)):
        solution[i][j] = 1
        return True
    if(checkCell(i,j,Maze,n)):
        solution[i][j]=1
        if(SolveMazeUtil(i+1, j, solution, n, Maze)):
            return True
        elif(SolveMazeUtil(i, j+1, solution, n, Maze)):
            return True
        solution[i][j]=0
    return False

print()
if(SolveMaze(Maze, n)):
    print("Yes, the rat can solve the maze with the above path")
else:
    print("Rat can not solve the maze")


#N Queen Problem----------------------------------------------------------------------------------
N = int(input("Enter N for N queen: "))
board = [[0 for i in range(0,N)] for j in range(0,N)]

def checkQueen(row, col, board):
    N=len(board)
    i=0
    while(i<col):
        if(board[row][i]==1):
            return False
        i+=1
    i=row
    j=col
    while(i>=0 and j>=0):
        if(board[i][j]==1):
            return False
        i-=1
        j-=1
    i=row
    j=col
    while(i<N and j>=0):
        if(board[i][j]==1):
            return False
        i+=1
        j-=1

    return True

def placeQueen(N, board):
    if(placeQueenUtil(0, board, N)==False):
        return False
    else:
        printMatrix(board)
        return True

def placeQueenUtil(col, board, N):
    if(col==N):
        return True
    for i in range(0,N):
        if(checkQueen(i,col, board)):
            board[i][col]=1
            if(placeQueenUtil(col+1, board, N)):
                return True
            board[i][col]=0
    return False

if(placeQueen(N, board)):
    print("The queens can be placed as above")
else:
    print("Queens can not be placed")


#Sudoku Problem----------------------------------------------------------------------------------
size = int(input("Enter grid size: "))
print("Enter grid(Zero for empty spots): ")
Grid = []
for i in range(size):
    Grid.append(list(map(int, input().split())))

def checkNum(row, col, num, Grid):
    n = len(Grid)
    for i in range(n):
        if(Grid[i][col]==num or Grid[row][i]==num):
            return False
    s = int(sqrt(n))
    isquare = row-(row%s)
    jsquare = col-(col%s)
    for i in range(0,s):
        for j in range(0,s):
            if(Grid[isquare+i][jsquare+j]==num):
                return False
    return True

def fillSudoku(Grid):
    n = len(Grid)
    i = 0
    while(i<n):
        j=0
        while(j<n):
            if(Grid[i][j]==0):
                break
            j+=1
        if(j!=n):
            break
        i+=1
    if(i==n and j==n):
        return True

    for num in range(1,n+1):
        if(checkNum(i,j,num,Grid)==True):
            Grid[i][j]=num
            if(fillSudoku(Grid)):
                return True
            Grid[i][j]=0
    return False

print()
if(fillSudoku(Grid)):
    print("Solved grid: ")
    printMatrix(Grid)
else:
    print("Grid can not be solved")
    printMatrix(Grid)
