from matrix import *
import random


def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###

def set_arrayBlk(locate, num):
    if num == 1:
        arrayBlk = [[[1, 1], [1, 1]],
                    [[1, 1], [1, 1]],
                    [[1, 1], [1, 1]],
                    [[1, 1], [1, 1]]]
    elif num == 2:
        arrayBlk = [[[1, 0, 0], [1, 1, 0], [0, 1, 0]],
                    [[0, 1, 1], [1, 1, 0], [0, 0, 0]],
                    [[0, 1, 0], [0, 1, 1], [0, 0, 1]],
                    [[0, 0, 0], [0, 1, 1], [1, 1, 0]]]
    elif num == 3:
        arrayBlk = [[[1, 0, 0], [1, 1, 1], [0, 0, 0]],
                    [[0, 1, 1], [0, 1, 0], [0, 1, 0]],
                    [[0, 0, 0], [1, 1, 1], [0, 0, 1]],
                    [[0, 1, 0], [0, 1, 0], [1, 1, 0]]]

    elif num == 4:
        arrayBlk = [[[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
                    [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]],
                    [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]]
    elif num == 5:
        arrayBlk = [[[0, 0, 1], [1, 1, 1], [0, 0, 0]],
                    [[0, 1, 0], [0, 1, 0], [0, 1, 1]],
                    [[0, 0, 0], [1, 1, 1], [1, 0, 0]],
                    [[1, 1, 0], [0, 1, 0], [0, 1, 0]]]
    elif num == 6:
        arrayBlk = [[[0, 1, 0], [1, 1, 0], [1, 0, 0]],
                    [[1, 1, 0], [0, 1, 1], [0, 0, 0]],
                    [[0, 0, 1], [0, 1, 1], [0, 1, 0]],
                    [[0, 0, 0], [1, 1, 0], [0, 1, 1]]]
    elif num == 7:
        arrayBlk = [[[0, 1, 0], [1, 1, 1], [0, 0, 0]],
                    [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
                    [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
                    [[0, 1, 0], [1, 1, 0], [0, 1, 0]]]
    return arrayBlk[locate]


### integer variables: must always0 be integer!

iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx // 2 - 2
locate = 0

newBlockNeeded = False

arrayScreen = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

###
### prepare the initial screen output
###

iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
num = random.randint(1, 7)
currBlk = Matrix(set_arrayBlk(locate, num))
tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen);
print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a':  # move left
        left -= 1
    elif key == 'd':  # move right
        left += 1
    elif key == 's':  # move down
        top += 1
    elif key == 'w':  # rotate the block clockwise
        locate += 1
        if locate == 4:
            locate = 0
        currBlk = Matrix(set_arrayBlk(locate, num))
    elif key == ' ':  # drop the block
        while (tempBlk.anyGreaterThan(1) != 1):
            top += 1
            tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
            tempBlk = tempBlk + currBlk
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a':  # undo: move right
            left += 1
        elif key == 'd':  # undo: move left
            left -= 1
        elif key == 's':  # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w':  # undo: rotate the block counter-clockwise
            rotate -= 1
            if rotate == -1:
                rotate = 3
            currBlk = Matrix(set_arrayBlk(locate, num))
        elif key == ' ':  # undo: move up
            top -= 1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen);
    print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx // 2 - 2
        locate = 0
        newBlockNeeded = False
        num = random.randint(1, 7)
        currBlk = Matrix(set_arrayBlk(locate, num))
        tempBlk = iScreen.clip(top, left, top + currBlk.get_dy(), left + currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break

        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen);
        print()

###
### end of the loop
###

