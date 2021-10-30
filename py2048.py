import random
blockSize = 5

gridSize = 4

#for i in range(gridSize):
#   for j in range(gridSize):
#       print("*"*blockSize, end=" ")
#    print("")

grid =  [[0]*gridSize]*gridSize

def printGrid():
    for i in range(gridSize):
        for j in range(gridSize):      
            lenofNum = len(str(grid[i][j]))
            print(grid[i][j], (blockSize-lenofNum)*"*",sep = "",end =" ")
        print("") 

grid[random.randint(0,gridSize-1)][random.randint(0,gridSize-1)] = 2

printGrid()