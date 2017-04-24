#################################
### Draw functions for Boggle ###
#################################

# Megan Cahill
# mcahill

from Tkinter import *

def drawBoard(canvas):
    board = canvas.data["board"]
    canvas.data["cellSize"] = cellSize = 380/(len(board))
    rows = len(board)
    cols = len(board[0])
    (left, top, right, bottom) = canvas.data["boardPos"]
    ## creates a background for the dice
    canvas.create_rectangle(left-2, top-2, right+2, bottom+2, fill = "navy")
    challengeLetter = canvas.data["challengeLetter"]
    for row in xrange(rows):
        for col in xrange(cols):
            w1 = 3 + left + cellSize*col
            w2 = -3 + left + cellSize*(col+1)
            h1 = 3 + top + cellSize*row
            h2 = -3 +top + cellSize*(row+1)
            shading(canvas,w1,w2,h1,h2)
            canvas.create_oval( w1 + 2, h1 + 2, w2 - 2, h2 - 2,
                                fill = "#%02x%02x%02x" % (250, 250, 250), width = 0)
            if selectedLetters(canvas, row, col):
                #### look into the transparent rectangles ####
                ## highlights the selected letters
                canvas.create_rectangle( w1 + 2, h1 + 2, w2 - 2, h2 - 2,
                                fill = "yellow", width = 0)
            if board[row][col] == "*":
                canvas.create_text( (w1 + w2)/2.0, (h1 + h2)/2.0,
                                text = challengeLetter, fill = "red",
                                font = ("Comic Sans MS Bold", "38"))
                canvas.data["challengeRowCol"] = (row, col)
            else:
                canvas.create_text( (w1 + w2)/2.0, (h1 + h2)/2.0,
                                text = board[row][col], fill = "Cadetblue3",
                                font = ("Comic Sans MS Bold", "38"))
    drawConnects(canvas)

def shading(canvas, w1,w2,h1,h2):
    canvas.create_rectangle( w1, h1, (w1+w2)/2.0, (h1+h2)/2.0,
                             fill = "#%02x%02x%02x" % (245, 245, 245), width = 0)
    canvas.create_rectangle( (w1+w2)/2.0, h1, w2, (h1+h2)/2.0,
                             fill = "#%02x%02x%02x" % (240, 240, 240), width = 0)
    canvas.create_rectangle( w1, (h1+h2)/2.0, w2, h2,
                             fill = "#%02x%02x%02x" % (235, 235, 235), width = 0)
    canvas.create_rectangle( (w1+w2)/2.0, (h1+h2)/2.0, w2, h2,
                             fill = "#%02x%02x%02x" % (230, 230, 230), width = 0)


def selectedLetters(canvas, row, col):
    clicked = canvas.data["clicked"]
    if (row, col) in clicked:
        return True
    else: return False

def drawConnects(canvas):
    clicked = canvas.data["clicked"]
    (left, top, right, bottom) = canvas.data["boardPos"]
    cellSize = canvas.data["cellSize"]
    if len(clicked) <= 1:
        pass
    else:
        for i in xrange(1, len(clicked)):
            (rowA, colA) = clicked[i]
            (rowB, colB) = clicked[i-1]
            (drow, dcol) = (rowA-rowB, colA-colB)
            w1 = left + cellSize*(colB + 1/2.0 + dcol/4.0)
            w2 = left + cellSize*(colA)+ cellSize/2.0 - dcol*(cellSize/4.0)
            h1 = top + cellSize*rowB + cellSize/2.0 + drow*(cellSize/4.0)
            h2 = top + cellSize*(rowA) + cellSize/2.0 - drow*(cellSize/4.0)
            canvas.create_line(w1, h1, w2, h2, width = 2)

            
def drawCurrentWord(canvas):
    ### want same left and right as board
    (left, top, right, bottom) = canvas.data["boardPos"]
    height = canvas.data["canvasH"]
    word = canvas.data["currentWord"]
    canvas.create_rectangle(left, bottom + 50, right, height - 50,
                            fill = "Lightgoldenrod")
    canvas.create_text( (left+right)/2.0, (bottom+height)/2.0, text = word, fill = "Cadetblue4",
                        font = ("Comic Sans MS Bold", "44"))

def createWordsAndPointsText(canvas):
    # avoids having to increment text position when drawing
    wordsList = canvas.data["wordsList"]
    wordsAndPoints = canvas.data["wordsAndPoints"]
    wordText1 = ""
    wordText2 = ""
    wordText3 = ""
    pointsText1 = ""
    pointsText2 = ""
    pointsText3 = ""
    if len(wordsList)>36:
        for i in xrange(18):
            word = wordsList[i]
            wordText1 += word + "\n"
            pointsText1 += str(wordsAndPoints[word]) + "\n"
        for i in xrange(18):
            word = wordsList[18+i]
            wordText2 += word + "\n"
            pointsText2 += str(wordsAndPoints[word]) + "\n"
        for i in xrange(len(wordsList) - 36):
            word = wordsList[36+i]
            wordText3 += word + "\n"
            pointsText3 += str(wordsAndPoints[word]) + "\n"
    elif len(wordsList)>18:
        for i in xrange(18):
            word = wordsList[i]
            wordText1 += word + "\n"
            pointsText1 += str(wordsAndPoints[word]) + "\n"
        for i in xrange(len(wordsList) - 18):
            word = wordsList[18+i]
            wordText2 += word + "\n"
            pointsText2 += str(wordsAndPoints[word]) + "\n"
    else:
        for i in xrange(len(wordsList)):
            word = wordsList[i]
            wordText1 += word + "\n"
            pointsText1 += str(wordsAndPoints[word]) + "\n"        
    return (wordText1, wordText2, wordText3, pointsText1, pointsText2, pointsText3)

def drawWordsList(canvas):
    (wordText1, wordText2, wordText3,
     pointsText1, pointsText2, pointsText3) = createWordsAndPointsText(canvas)
    width = canvas.data["canvasW"]
    (left, top, right, bottom) = canvas.data["boardPos"]
    canvas.create_rectangle(right+75, top, width - 50, bottom,
                            fill = "Lightgoldenrod")
    canvas.create_text(right+85, top+10, anchor = NW, text = wordText1,
                       font = ("Comic Sans MS Bold", "14"))
    canvas.create_text(right+145, top+10, anchor = NW, text = pointsText1,
                       font = ("Comic Sans MS Bold", "14"))
    canvas.create_text(right+160, top+10, anchor = NW, text = wordText2,
                       font = ("Comic Sans MS Bold", "14"))
    canvas.create_text(right+220, top+10, anchor = NW, text = pointsText2,
                       font = ("Comic Sans MS Bold", "14"))
    canvas.create_text(right+235, top+10, anchor = NW, text = wordText3,
                       font = ("Comic Sans MS Bold", "14"))
    canvas.create_text(right+295, top+10, anchor = NW, text = pointsText3,
                       font = ("Comic Sans MS Bold", "14"))

def drawMenuButton(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    canvas.create_rectangle(width - 220, height - 100, width - 120, height- 50,
                            fill = "orange", width = 3)
    canvas.create_text(width - 170, height-75, text = "MENU",
                       font = ("Comic Sans MS Bold", "30"))

def drawClock(canvas):
    time = canvas.data["time"]
    mins = time/60
    seconds = str((time % 60)/10) + str((time%60)%10)
    clock = str(mins) + ":" + str(seconds)
    canvas.create_text(625, 80, text = clock, font = ("Comic Sans MS Bold", "30"))


def drawTotalPoints(canvas):
    wordsList = canvas.data["wordsList"]
    wordsAndPoints = canvas.data["wordsAndPoints"]
    width = canvas.data["canvasW"]
    (left, top, right, bottom) = canvas.data["boardPos"]
    totalScore = 0
    for word in wordsList:
        totalScore += wordsAndPoints[word]
    canvas.data["score"] = totalScore
    canvas.create_rectangle(right+75, bottom + 25, width - 50, bottom +75,
                            fill = "Lightgoldenrod")
    canvas.create_text((right+width+25)/2.0, bottom + 50, text = "Score: " + str(totalScore),
                       font = ("Comic Sans MS Bold", "30"))
    

def drawLogo(canvas):
    width = canvas.data["canvasW"]
    image = canvas.data["thirdImage"]
    canvas.create_image(width/2.0, 50, image=image)
    
def drawGame(canvas):
    drawLogo(canvas)
    drawBoard(canvas)
    drawCurrentWord(canvas)
    drawWordsList(canvas)
    drawMenuButton(canvas)
    drawTotalPoints(canvas)
    drawClock(canvas)
