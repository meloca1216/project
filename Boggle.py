#   Boggle.py
#
#   Megan Cahill  mcahill
#
#   15-110 Term Project
#
#   Fall 2010 
#

from Tkinter import *
import random
import Draw
import Test
import Menu
import Help
import GameOver


def createBoard(canvas):
    dice = Test.whichGameDice(canvas)
    # get random letters and locations of dice
    boardLetters = []
    # one random letter for each die
    for die in xrange(len(dice)):
        dieSide = random.randint(0,5)
        dieLetter = dice[die][dieSide]
        boardLetters.append(dieLetter)
    # "shuffle dice"
    random.shuffle(boardLetters)
    # turn letters into square board
    rows = int(len(boardLetters)**(.5))
    cols = int(len(boardLetters)**(.5))
    squareBoard = []
    for row in xrange(rows):
        squareBoard += [[0]*cols]
        for col in xrange(cols):
            squareBoard[row][col] = boardLetters[row*rows + col]
    canvas.data["board"] = squareBoard

def mousePressed(event):
    canvas = event.widget.canvas
    if canvas.data["menuScreen"]:
        mousePressedMenu(event)
    elif canvas.data["help"]:
        mousePressedHelp(event)
    elif canvas.data["gameScreen"]:
        mousePressedGame(event)
    elif canvas.data["gameOver"]:
        mousePressedGameOver(event)
    redrawAll(canvas)


def mousePressedGameOver(event):
    canvas = event.widget.canvas
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    if (((width/2.0 - 50)<event.x<(width/2.0+50)) and
        ((height*3/4.0)<event.y<(height*3/4.0+50))):
        init(canvas)

def mousePressedMenu(event):
    canvas = event.widget.canvas
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    if (height/2.0 < event.y < height/2.0+25):
        if (width/3.0 < event.x < width/3.0+25):
            canvas.data["fourByFour"] = True
            canvas.data["fiveByFive"] = False
        elif (width*2/3.0-25 < event.x < width*2/3.0):
            canvas.data["fourByFour"] = False
            canvas.data["fiveByFive"] = True        
    elif (height*2/3.0-50 < event.y < height*2/3.0-24):
        canvas.data["challengeCube"] = not canvas.data["challengeCube"]
    elif (width/2.0 - 50 < event.x < width/2.0+50):
        if (height*3/4.0-25 < event.y < height*3/4.0+25):
            if (canvas.data["fourByFour"]) or (canvas.data["fiveByFive"]):
                canvas.data["menuScreen"] = False
                canvas.data["gameScreen"] = True
                canvas.data["challengeLetter"] = challengeCube[random.randint(0,5)]
                createBoard(canvas)
                timerFired(canvas)
            else:
                pass
        if (height*3/4.0 + 50 < event.y < height*3/4.0+100):
            canvas.data["menuScreen"] = False
            canvas.data["help"] = True
    redrawAll(canvas)
            
    

def mousePressedHelp(event):
    canvas = event.widget.canvas
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    if (width - 160 < event.x < width - 60) and (height - 110 < event.y < height- 60):
        canvas.data["help"] = False
        canvas.data["menuScreen"] = True
    else: pass

def doBoardMove(canvas, x, y):
    cellSize = canvas.data["cellSize"]
    clicked = canvas.data["clicked"]
    board = canvas.data["board"]
    word = canvas.data["currentWord"]
    challengeLetter = canvas.data["challengeLetter"]
    row = (y-100)/cellSize
    col = (x-50)/cellSize
    if clicked == []:
        clicked += [(row, col)]
        if board[row][col] == "*":
            canvas.data["currentWord"] += challengeLetter
        else:
            canvas.data["currentWord"] += board[row][col]
    ## don't need to test whether it's a valid row or col
    ## is taken care of in outer if statement
    elif (((row,col) not in clicked) and
          Test.validMove(canvas, row, col)):
        clicked += [(row, col)]
        if board[row][col] == "*":
            canvas.data["currentWord"] += challengeLetter
        else:
            canvas.data["currentWord"] += board[row][col]
    elif ((row, col) == clicked[-1]):
        clicked.remove((row,col))
        if board[row][col] == "*":
        ## special case for "Qu"
            if challengeLetter == "Qu":
                word = word[0 : len(word)-2]
            else:
                word = word[0 : len(word)-1]
        elif board[row][col] == "Qu":
            word = word[0 : len(word)-2]
        else:
            word = word[0 : len(word)-1] 
        canvas.data["currentWord"] = word
        

def mousePressedGame(event):
    canvas = event.widget.canvas
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    (left, top, right, bottom) = canvas.data["boardPos"]
    x = event.x
    y = event.y
    if (left < x < right) and (top < y < bottom):
        doBoardMove(canvas, x, y)
        redrawAll(canvas)
    elif (width - 220 < x < width - 120) and (height - 100 < y < height- 50):
        init(canvas)


def keyPressed(event):
    canvas = event.widget.canvas
    if event.keysym == "Return" :
        word = canvas.data["currentWord"]
        Test.submitWord(canvas, word)
    else:
        pass
    redrawAll(canvas)
        





### according to newer version:
### http://www.had2know.com/entertainment/play-boggle-word-search-game.html
fourByFourDice = [["A","A","E","E","G","N"], ["E","L","R","T","T","Y"],
                  ["A","O","O","T","T","W"], ["A","B","B","J","O","O"],
                  ["E","H","R","T","V","W"], ["C","I","M","O","T","U"],
                  ["D","I","S","T","T","Y"], ["E","I","O","S","S","T"],
                  ["D","E","L","R","V","Y"], ["A","C","H","O","P","S"],
                  ["H","I","M","N","Qu","U"], ["E","E","I","N","S","U"],
                  ["E","E","G","H","N","W"], ["A","F","F","K","P","S"],
                  ["H","L","N","N","R","Z"], ["D","E","L","I","R","X"]]

fiveByFiveDice = [["A","A","A","F","R","S"], ["A","A","E","E","E","E"],
                  ["A","A","F","I","R","S"], ["A","D","E","N","N","N"],
                  ["A","E","E","E","E","M"], ["A","E","E","G","M","U"],
                  ["A","E","G","M","N","N"], ["A","F","I","R","S","Y"],
                  ["B","J","K","Qu","X","Z"], ["C","C","N","S","T","W"],
                  ["C","E","I","I","L","T"], ["C","E","I","L","P","T"],
                  ["C","E","I","P","S","T"], ["D","D","L","N","O","R"],
                  ["D","H","H","L","O","R"], ["D","H","H","N","O","T"],
                  ["D","H","L","N","O","R"], ["E","I","I","I","T","T"], 
                  ["E","M","O","T","T","T"], ["E","N","S","S","S","U"],
                  ["F","I","P","R","S","Y"], ["G","O","R","R","V","W"],
                  ["H","I","P","R","R","Y"], ["N","O","O","T","U","W"],
                  ["O","O","O","T","T","U"]]

fourChallenge = [["A","A","E","E","G","N"], ["E","L","R","T","T","Y"],
                  ["A","O","O","T","T","W"], ["A","B","B","J","O","O"],
                  ["E","H","R","T","V","W"], ["C","I","M","O","T","U"],
                  ["D","I","S","T","T","Y"], ["E","I","O","S","S","T"],
                  ["D","E","L","R","V","Y"], ["A","C","H","O","P","S"],
                  ["*","*","*","*","*","*"], ["E","E","I","N","S","U"],
                  ["E","E","G","H","N","W"], ["A","F","F","K","P","S"],
                  ["H","L","N","N","R","Z"], ["D","E","L","I","R","X"]]

fiveChallenge = [["A","A","A","F","R","S"], ["A","A","E","E","E","E"],
                  ["A","A","F","I","R","S"], ["A","D","E","N","N","N"],
                  ["A","E","E","E","E","M"], ["A","E","E","G","M","U"],
                  ["A","E","G","M","N","N"], ["A","F","I","R","S","Y"],
                  ["*","*","*","*","*","*"], ["C","C","N","S","T","W"],
                  ["C","E","I","I","L","T"], ["C","E","I","L","P","T"],
                  ["C","E","I","P","S","T"], ["D","D","L","N","O","R"],
                  ["D","H","H","L","O","R"], ["D","H","H","N","O","T"],
                  ["D","H","L","N","O","R"], ["E","I","I","I","T","T"], 
                  ["E","M","O","T","T","T"], ["E","N","S","S","S","U"],
                  ["F","I","P","R","S","Y"], ["G","O","R","R","V","W"],
                  ["H","I","P","R","R","Y"], ["N","O","O","T","U","W"],
                  ["O","O","O","T","T","U"]]

challengeCube = ["I","K","L","M","Qu","U"]


def redrawAll(canvas):
    canvas.delete(ALL)
    if canvas.data["gameOver"]:
        canvas.data["menuScreen"] = False
        canvas.data["help"] = False
        canvas.data["gameScreen"] = False
        GameOver.drawGameOver(canvas)
    else:
        if canvas.data["menuScreen"]:
            Menu.drawMenu(canvas)
        elif canvas.data["help"]:
            Help.drawHelpScreen(canvas)
        elif canvas.data["gameScreen"]:
            Draw.drawGame(canvas)

def timerFired(canvas):
    time = canvas.data["time"]
    if time == 0:
        canvas.data["gameOver"] = True
        redrawAll(canvas)
    else:
        canvas.data["time"] -= 1
        delay = 1000
        redrawAll(canvas)
        canvas.after(delay, timerFired, canvas)
    


### image found at http://idisk.mac.com/blikum1/Public/pix/Boggle.jpg###
        
def init(canvas):
    canvas.data["menuScreen"] = True
    canvas.data["help"] = False
    canvas.data["gameScreen"] = False
    canvas.data["wordsAndPoints"] = {}
    canvas.data["currentWord"] = ""
    canvas.data["clicked"] = []
    canvas.data["wordsList"] = []
    canvas.data["diceSets"] = {"fourByFour": fourByFourDice, "fiveByFive": fiveByFiveDice,
                               "fourChallenge": fourChallenge, "fiveChallenge": fiveChallenge}
    canvas.data["fourByFour"] = False
    canvas.data["fiveByFive"] = False
    canvas.data["challengeCube"] = False
    canvas.data["challengeRowCol"] = None
    canvas.data["gameOver"] = False
    canvas.data["time"] = 180 #seconds or 3 mins
    image = PhotoImage(file="BoggleLogo.gif")
    thirdImage = image.subsample(3,3)
    canvas.data["image"] = image
    canvas.data["thirdImage"] = thirdImage
    Menu.drawMenu(canvas)


def run():
    # create the root and the canvas
    root = Tk()
    global canvas
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=800, height=675, bg = "Darkorange3")
    canvas.pack(fill=BOTH, expand=YES)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    canvas.data["boardPos"] = (50, 100, 430, 480)
    canvas.data["canvasH"] = 675
    canvas.data["canvasW"] = 800
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    #timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
