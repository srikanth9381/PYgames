import random
def full_grid_generator():
        board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
        ]
        for i in range(0,3) :
            choise = [1,2,3,4,5,6,7,8,9]
            for j in range(0,9) :
                temp = random.choice(choise)
                board[i*3+(j)//3][i*3+(j)%3] = temp
                choise.remove(temp)
        solve(board)
        return board

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def rsolve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in reversed(range(1,10)):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

def numbers_remover(bo):
    choise = [0,1,2,3,4,5,6,7,8]
    while True:
        x = random.choice(choise)
        y = random.choice(choise)
        if bo[x][y] != 0:
            temp = bo[x][y]
            bo[x][y] = 0
            dum1 = bo
            dum2 = bo
            dum1 = solve(dum1)
            dum2 = rsolve(dum2)
            if dum1 != dum2 :
                bo[x][y] = temp
                return
    return
board =full_grid_generator()
print_board(board)
numbers_remover(board)
print("___________________")
print_board(board)