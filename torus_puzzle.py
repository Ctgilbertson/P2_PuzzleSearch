import copy


def print_succ(state):
    print("print_succ started")

    matrix = stateToMatrix(state)

    x = 0
    y = 0

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                x = i
                y = j

    left = y - 1
    right = y + 1
    top = x - 1
    bottom = x + 1

    if left < 0:
        left = 2

    if right > 2:
        right = 0

    if top < 0:
        top = 2

    if bottom > 2:
        bottom = 0

    ## TODO try to find a better way than deep copies
    nextStateLeft = copy.deepcopy(matrix)
    stateList = []

    nextStateLeft[x][y] = nextStateLeft[x][left]
    nextStateLeft[x][left] = 0
    stateList.append(matrixToState(nextStateLeft))

    nextStateRight = copy.deepcopy(matrix)

    nextStateRight[x][y] = nextStateRight[x][right]
    nextStateRight[x][right] = 0
    stateList.append(matrixToState(nextStateRight))

    nextStateTop = copy.deepcopy(matrix)

    nextStateTop[x][y] = nextStateTop[top][y]
    nextStateTop[top][y] = 0
    stateList.append(matrixToState(nextStateTop))

    nextStateBottom = copy.deepcopy(matrix)

    nextStateBottom[x][y] = nextStateBottom[bottom][y]
    nextStateBottom[bottom][y] = 0
    stateList.append(matrixToState(nextStateBottom))

    stateList = sorted(stateList)
    ## TODO remove space after h=
    for i in stateList:
        print(i, "h=", calculateHeuristic(i))


def solve(state):
    print("solve started")




def stateToMatrix(state):
    matrix = [[state[0], state[1], state[2]],
              [state[3], state[4], state[5]],
              [state[6], state[7], state[8]]]

    return matrix


def matrixToState(matrix):
    stateMTS = [matrix[0][0], matrix[0][1], matrix[0][2],
                matrix[1][0], matrix[1][1], matrix[1][2],
                matrix[2][0], matrix[2][1], matrix[2][2]]

    return stateMTS


def calculateHeuristic(stateH):
    h = 0
    solution = [1, 2, 3, 4, 5, 6, 7, 8]

    for i in range(len(stateH)-1):
        if stateH[i] != solution[i]:
            h += 1

    return h


state = [1, 2, 3, 4, 5, 0, 6, 7, 8]
print_succ(state)
