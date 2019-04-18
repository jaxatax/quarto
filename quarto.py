#unfinished
from random import *
import pyttsx3
engine = pyttsx3.init()

print('''Key:
TWSS = Tall White Square Solid
TWSH = Tall White Square Hollow
TWCS = Tall White Circular Solid
TWCH = Tall White Circular Hollow
TBSS = Tall Black Square Solid
TBSH = Tall Black Square Hollow
TBCS = Tall Black Circular Solid
TBSS = Tall Black Circular Hollow
SWSS = Short White Square Solid
SWSH = Short White Square Hollow
SWCS = Short White Circular Solid
SWCH = Short White Circular Hollow
SBSS = Short Black Square Solid
SBSH = Short Black Square Hollow
SBCS = Short Black Circular Solid
SBCH = Short Black Circular Hollow
''')

TWSS = ["Tall", "White", "Square", "Solid"]
TWSH = ["Tall", "White", "Square", "Hollow"]
TWCS = ["Tall", "White", "Circular", "Solid"]
TWCH = ["Tall", "White", "Circular", "Hollow"]
TBSS = ["Tall", "Black", "Square", "Solid"]
TBSH = ["Tall", "Black", "Square", "Hollow"]
TBCS = ["Tall", "Black", "Circular", "Solid"]
TBSS = ["Tall", "Black", "Circular", "Hollow"]
SWSS = ["Short", "White", "Square", "Solid"]
SWSH = ["Short", "White", "Square", "Hollow"]
SWCS = ["Short", "White", "Circular", "Solid"]
SWCH = ["Short", "White", "Circular", "Hollow"]
SBSS = ["Short", "Black", "Square", "Solid"]
SBSH = ["Short", "Black", "Square", "Hollow"]
SBCS = ["Short", "Black", "Circular", "Solid"]
SBCH = ["Short", "Black", "Circular", "Hollow"]

emptySpace = "    "

pieces = [TWSS, TWSH, TWCS, TWCH, TBSS, TBSH, TBCS, TBSS, SWSS, SWSH, SWCS, SBSS, SBSH, SBCS, SBCH]

#board looks like this:
'''
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
'''

board = [emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace, emptySpace]

rowOne = [board[0], board[1], board[2], board[3]]
rowTwo = [board[4], board[5], board[6], board[7]]
rowThree = [board[8], board[9], board[10], board[11]]
rowFour = [board[12], board[13], board[14], board[15]]

columnOne = [board[0], board[4], board[8], board[12]]
columnTwo = [board[1], board[5], board[9], board[13]]
columnThree = [board[2], board[6], board[10], board[14]]
columnFour = [board[3], board[7], board[11], board[15]]

leftToRightDiagonal = [board[0], board[5], board[10], board[15]]
rightToLeftDiagonal = [board[3], board[6], board[9], board[12]]

lines = [rowOne, rowTwo, rowThree, rowFour, columnOne, columnTwo, columnThree, columnFour, leftToRightDiagonal, rightToLeftDiagonal]

print("Coordinate system works like this:")
engine.say("Coordinate system works like this,")
engine.runAndWait()

print('''
   a     b      c      d
1     |      |      |     
2     |      |      |     
3     |      |      |     
4     |      |      |     
''')

print("For instance, if you wanted to put a TWSS piece in the top right, you would type \"TWSS d1\".")
engine.say("For instance, if you wanted to put a TWSS piece in the top right, you would type TWSS d1.")
engine.runAndWait()
visualBoard = board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + "\n" + board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] + "\n" + board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11] + "\n" + board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15]

won = False

def checkForWin():
    if rowOne[0] != emptySpace and rowOne[1] != emptySpace and rowOne[2] != emptySpace and rowOne[3] != emptySpace:
        if rowOne[0[0]] == rowOne[0[1]] == rowOne[0[2]] == rowOne[0[3]]:
            print("There is a win in row one.")
            engine.say("There is a win in row one.")
            engine.runAndWait()
            won = True
        elif rowOne[1[0]] == rowOne[1[1]] == rowOne[1[2]] == rowOne[1[3]]:
            print("There is a win in row one.")
            engine.say("There is a win in row one.")
            engine.runAndWait()
            won = True
        elif rowOne[2[0]] == rowOne[2[1]] == rowOne[2[2]] == rowOne[2[3]]:
            print("There is a win in row one.")
            engine.say("There is a win in row one.")
            engine.runAndWait()
            won = True
        elif rowOne[3[0]] == rowOne[3[1]] == rowOne[3[2]] == rowOne[3[3]]:
            print("There is a win in row one.")
            engine.say("There is a win in row one.")
            engine.runAndWait()
            won = True
    if rowTwo[0] != emptySpace and rowTwo[1] != emptySpace and rowTwo[2] != emptySpace and rowTwo[3] != emptySpace:
        if rowTwo[0[0]] == rowTwo[0[1]] == rowTwo[0[2]] == rowTwo[0[3]]:
            print("There is a win in row two.")
            engine.say("There is a win in row two.")
            engine.runAndWait()
            won = True
        elif rowTwo[1[0]] == rowTwo[1[1]] == rowTwo[1[2]] == rowTwo[1[3]]:
            print("There is a win in row two.")
            engine.say("There is a win in row two.")
            engine.runAndWait()
            won = True
        elif rowTwo[2[0]] == rowTwo[2[1]] == rowTwo[2[2]] == rowTwo[2[3]]:
            print("There is a win in row two.")
            engine.say("There is a win in row two.")
            engine.runAndWait()
            won = True
        elif rowTwo[3[0]] == rowTwo[3[1]] == rowTwo[3[2]] == rowTwo[3[3]]:
            print("There is a win in row two.")
            engine.say("There is a win in row two.")
            engine.runAndWait()
            won = True
    if rowThree[0] != emptySpace and rowThree[1] != emptySpace and rowThree[2] != emptySpace and rowThree[3] != emptySpace:
        if rowThree[0[0]] == rowThree[0[1]] == rowThree[0[2]] == rowThree[0[3]]:
            print("There is a win in row three.")
            engine.say("There is a win in row three.")
            engine.runAndWait()
            won = True
        elif rowThree[1[0]] == rowThree[1[1]] == rowThree[1[2]] == rowThree[1[3]]:
            print("There is a win in row three.")
            engine.say("There is a win in row three.")
            engine.runAndWait()
            won = True
        elif rowThree[2[0]] == rowThree[2[1]] == rowThree[2[2]] == rowThree[2[3]]:
            print("There is a win in row three.")
            engine.say("There is a win in row three.")
            engine.runAndWait()
            won = True
        elif rowThree[3[0]] == rowThree[3[1]] == rowThree[3[2]] == rowThree[3[3]]:
            print("There is a win in row three.")
            engine.say("There is a win in row three.")
            engine.runAndWait()
            won = True
    if rowFour[0] != emptySpace and rowFour[1] != emptySpace and rowFour[2] != emptySpace and rowFour[3] != emptySpace:
        if rowFour[0[0]] == rowFour[0[1]] == rowFour[0[2]] == rowFour[0[3]]:
            print("There is a win in row four.")
            engine.say("There is a win in row four.")
            engine.runAndWait()
            won = True
        elif rowFour[1[0]] == rowFour[1[1]] == rowFour[1[2]] == rowFour[1[3]]:
            print("There is a win in row four.")
            engine.say("There is a win in row four.")
            engine.runAndWait()
            won = True
        elif rowFour[2[0]] == rowFour[2[1]] == rowFour[2[2]] == rowFour[2[3]]:
            print("There is a win in row four.")
            engine.say("There is a win in row four.")
            engine.runAndWait()
            won = True
        elif rowFour[3[0]] == rowFour[3[1]] == rowFour[3[2]] == rowFour[3[3]]:
            print("There is a win in row four.")
            engine.say("There is a win in row four.")
            engine.runAndWait()
            won = True
    if columnOne[0] != emptySpace and columnOne[1] != emptySpace and columnOne[2] != emptySpace and columnOne[3] != emptySpace:
        if columnOne[0[0]] == columnOne[0[1]] == columnOne[0[2]] == columnOne[0[3]]:
            print("There is a win in column one.")
            engine.say("There is a win in column one.")
            engine.runAndWait()
            won = True
        elif columnOne[1[0]] == columnOne[1[1]] == columnOne[1[2]] == columnOne[1[3]]:
            print("There is a win in column one.")
            engine.say("There is a win in column one.")
            engine.runAndWait()
            won = True
        elif columnOne[2[0]] == columnOne[2[1]] == columnOne[2[2]] == columnOne[2[3]]:
            print("There is a win in column one.")
            engine.say("There is a win in column one.")
            engine.runAndWait()
            won = True
        elif columnOne[3[0]] == columnOne[3[1]] == columnOne[3[2]] == columnOne[3[3]]:
            print("There is a win in column one.")
            engine.say("There is a win in column one.")
            engine.runAndWait()
            won = True
    if columnTwo[0] != emptySpace and columnTwo[1] != emptySpace and columnTwo[2] != emptySpace and columnTwo[3] != emptySpace:
        if columnTwo[0[0]] == columnTwo[0[1]] == columnTwo[0[2]] == columnTwo[0[3]]:
            print("There is a win in column two.")
            engine.say("There is a win in column two.")
            engine.runAndWait()
            won = True
        elif columnTwo[1[0]] == columnTwo[1[1]] == columnTwo[1[2]] == columnTwo[1[3]]:
            print("There is a win in column two.")
            engine.say("There is a win in column two.")
            engine.runAndWait()
            won = True
        elif columnTwo[2[0]] == columnTwo[2[1]] == columnTwo[2[2]] == columnTwo[2[3]]:
            print("There is a win in column two.")
            engine.say("There is a win in column two.")
            engine.runAndWait()
            won = True
        elif columnTwo[3[0]] == columnTwo[3[1]] == columnTwo[3[2]] == columnTwo[3[3]]:
            print("There is a win in column two.")
            engine.say("There is a win in column two.")
            engine.runAndWait()
            won = True
    if columnThree[0] != emptySpace and columnThree[1] != emptySpace and columnThree[2] != emptySpace and columnThree[3] != emptySpace:
        if columnThree[0[0]] == columnThree[0[1]] == columnThree[0[2]] == columnThree[0[3]]:
            print("There is a win in column three.")
            engine.say("There is a win in column three.")
            engine.runAndWait()
            won = True
        elif columnThree[1[0]] == columnThree[1[1]] == columnThree[1[2]] == columnThree[1[3]]:
            print("There is a win in column three.")
            engine.say("There is a win in column three.")
            engine.runAndWait()
            won = True
        elif columnThree[2[0]] == columnThree[2[1]] == columnThree[2[2]] == columnThree[2[3]]:
            print("There is a win in column three.")
            engine.say("There is a win in column three.")
            engine.runAndWait()
            won = True
        elif columnThree[3[0]] == columnThree[3[1]] == columnThree[3[2]] == columnThree[3[3]]:
            print("There is a win in column three.")
            engine.say("There is a win in column three.")
            engine.runAndWait()
            won = True
    if columnFour[0] != emptySpace and columnFour[1] != emptySpace and columnFour[2] != emptySpace and columnFour[3] != emptySpace:
        if columnFour[0[0]] == columnFour[0[1]] == columnFour[0[2]] == columnFour[0[3]]:
            print("There is a win in column four.")
            engine.say("There is a win in column four.")
            engine.runAndWait()
            won = True
        elif columnFour[1[0]] == columnFour[1[1]] == columnFour[1[2]] == columnFour[1[3]]:
            print("There is a win in column four.")
            engine.say("There is a win in column four.")
            engine.runAndWait()
            won = True
        elif columnFour[2[0]] == columnFour[2[1]] == columnFour[2[2]] == columnFour[2[3]]:
            print("There is a win in column four.")
            engine.say("There is a win in column four.")
            engine.runAndWait()
            won = True
        elif columnFour[3[0]] == columnFour[3[1]] == columnFour[3[2]] == columnFour[3[3]]:
            print("There is a win in column four.")
            engine.say("There is a win in column four.")
            engine.runAndWait()
            won = True
    if leftToRightDiagonal[0] != emptySpace and leftToRightDiagonal[1] != emptySpace and leftToRightDiagonal[2] != emptySpace and leftToRightDiagonal[3] != emptySpace:
        if leftToRightDiagonal[0[0]] == leftToRightDiagonal[0[1]] == leftToRightDiagonal[0[2]] == leftToRightDiagonal[0[3]]:
            print("There is a win in the left to right diagonal.")
            engine.say("There is a win in left to right diagonal.")
            engine.runAndWait()
            won = True
        elif leftToRightDiagonal[1[0]] == leftToRightDiagonal[1[1]] == leftToRightDiagonal[1[2]] == leftToRightDiagonal[1[3]]:
            print("There is a win in left to right diagonal.")
            engine.say("There is a win in left to right diagonal.")
            engine.runAndWait()
            won = True
        elif leftToRightDiagonal[2[0]] == leftToRightDiagonal[2[1]] == leftToRightDiagonal[2[2]] == leftToRightDiagonal[2[3]]:
            print("There is a win in left to right diagonal.")
            engine.say("There is a win in left to right diagonal.")
            engine.runAndWait()
            won = True
        elif leftToRightDiagonal[3[0]] == leftToRightDiagonal[3[1]] == leftToRightDiagonal[3[2]] == leftToRightDiagonal[3[3]]:
            print("There is a win in left to right diagonal.")
            engine.say("There is a win in left to right diagonal.")
            engine.runAndWait()
            won = True
    if rightToLeftDiagonal[0] != emptySpace and rightToLeftDiagonal[1] != emptySpace and rightToLeftDiagonal[2] != emptySpace and rightToLeftDiagonal[3] != emptySpace:
        if rightToLeftDiagonal[0[0]] == rightToLeftDiagonal[0[1]] == rightToLeftDiagonal[0[2]] == rightToLeftDiagonal[0[3]]:
            print("There is a win in right to left diagonal.")
            engine.say("There is a win in right to left diagonal.")
            engine.runAndWait()
            won = True
        elif rightToLeftDiagonal[1[0]] == rightToLeftDiagonal[1[1]] == rightToLeftDiagonal[1[2]] == rightToLeftDiagonal[1[3]]:
            print("There is a win in right to left diagonal.")
            engine.say("There is a win in right to left diagonal.")
            engine.runAndWait()
            won = True
        elif rightToLeftDiagonal[2[0]] == rightToLeftDiagonal[2[1]] == rightToLeftDiagonal[2[2]] == rightToLeftDiagonal[2[3]]:
            print("There is a win in right to left diagonal.")
            engine.say("There is a win in right to left diagonal.")
            engine.runAndWait()
            won = True
        elif rightToLeftDiagonal[3[0]] == rightToLeftDiagonal[3[1]] == rightToLeftDiagonal[3[2]] == rightToLeftDiagonal[3[3]]:
            print("There is a win in right to left diagonal.")
            engine.say("There is a win in right to left diagonal.")
            engine.runAndWait()
            won = True

checkForWin()
