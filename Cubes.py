
numberOfTest = int(input())

for _ in range(numberOfTest):
    noOfCubes = int(input())
    inputList = list(map(int, input().split(" ")))
    left = 0
    right = len(inputList)-1
    pickedTile = 0
    leftTile = False
    rightTile = False
    notPossible = False
    while left != right:
        if inputList[left] > inputList[right]:
            blockSize = inputList[left]
            left = left + 1
            newBlockSize = inputList[left]
            if newBlockSize > blockSize:
                notPossible = True
                break
        elif inputList[left] < inputList[right]:
            blockSize = inputList[right]
            right = right - 1
            newBlockSize = inputList[right]
            if newBlockSize > blockSize:
                notPossible = True
                break
        elif inputList[left] == inputList[right]:
            left = left + 1
        else:
            notPossible = True
            break
    if notPossible:
        print(False)
    else:
        print(True)