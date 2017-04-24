# Game Over

# Megan Cahill
# mcahill
    
def drawGameOver(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    currentScore = canvas.data["score"]
    words = canvas.data["wordsList"]
    msg = "Game Over!\nYou found " + str(len(words)) + " words!\nFinal Score: " + str(currentScore)
    canvas.create_rectangle( 50, 50, width-50, height-50, fill = "maroon",
                             width = 0)
    canvas.create_text(width/2.0, height/2.0, text = msg, fill = "magenta",
                       font = ("Comic Sans MS", "48"))
    canvas.create_rectangle(width/2.0 - 50, height*3/4.0, width/2.0+50, height*3/4.0+50,
                            fill = "orange", width = 3)
    canvas.create_text(width/2.0, height*3/4.0+25, text = "MENU",
                       font = ("Comic Sans MS Bold", "30"))
