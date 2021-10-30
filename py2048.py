import random
blockSize = 5

gridSize = 4

#for i in range(gridSize):
#   for j in range(gridSize):
#       print("*"*blockSize, end=" ")
#    print("")

# Use W A S D to play the Game!

grid =  {(i,j):0 for i in range(gridSize) for j in range(gridSize) }

def printGrid():
    for i in range(gridSize):
        for j in range(gridSize):      
            lenofNum = len(str(grid[i,j]))
            print(grid[i,j], (blockSize-lenofNum)*"*",sep = "",end =" ")
        print("") 

grid[random.randint(0,gridSize-1) , random.randint(0,gridSize-1)] = 2

printGrid()

while True:
    inp = input("W A S or D : ")
    
    if inp.lower() == "w":
        print("hi")
        