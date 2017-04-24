#############################################
###  draw menu with gameplay options
###  and play and help screens
#############################################

## Megan Cahill
## mcahill

from Tkinter import *

def drawOptions(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    ### four
    canvas.create_rectangle(width/3.0, height/2.0, width/3.0+25, height/2.0+25,
                            fill = "yellow", width = 0)
    canvas.create_text(width/3.0+13, height/2.0+50, text = "Four By Four", fill = "yellow",
                       font = ("Comic Sans MS Bold", "20"))
    ### five
    canvas.create_rectangle(width*2/3.0-25, height/2.0, width*2/3.0, height/2.0+25,
                            fill = "yellow", width = 0)
    canvas.create_text(width*2/3.0-13, height/2.0+50, text = "Five By Five", fill = "yellow",
                       font = ("Comic Sans MS Bold", "20"))
    ### challenge
    canvas.create_rectangle(width/2.0-13, height*2/3.0-50, width/2.0+13, height*2/3.0-24,
                            fill = "yellow", width = 0)
    canvas.create_text(width/2.0, height*2/3.0, text = "Challenge Cube", fill = "yellow",
                      font = ("Comic Sans MS Bold", "20"))


                       
def drawOptionsSelected(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    four = canvas.data["fourByFour"]
    five = canvas.data["fiveByFive"]
    challenge = canvas.data["challengeCube"]
    if four:
        canvas.create_oval(width/3.0, height/2.0, width/3.0+25, height/2.0+25,
                            fill = "red")
    if five:
        canvas.create_oval(width*2/3.0-25, height/2.0, width*2/3.0, height/2.0+25,
                            fill = "red")
    if challenge:
        canvas.create_oval(width/2.0-13, height*2/3.0-50, width/2.0+13, height*2/3.0+-24,
                            fill = "red")

def drawHelpAndPlay(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    # "play button"
    canvas.create_rectangle(width/2.0 - 50, height*3/4.0-25, width/2.0+50, height*3/4.0+25,
                            fill = "orange", width = 3)
    canvas.create_text(width/2.0, height*3/4.0, text = "PLAY",
                       font = ("Comic Sans MS Bold", "30"))
    # "access help"
    canvas.create_rectangle(width/2.0 - 50, height*3/4.0 + 50, width/2.0+50, height*3/4.0+100,
                            fill = "orange", width = 3)
    canvas.create_text(width/2.0, height*3/4.0+75, text = "HELP",
                       font = ("Comic Sans MS Bold", "30"))


def drawMenu(canvas):
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    image = canvas.data["image"]
    canvas.create_rectangle( 50, 50, width-50, height-50, fill = "purple",
                             width = 0)
    canvas.create_image(width/2.0, 190, image=image)
    drawOptions(canvas)
    drawOptionsSelected(canvas)
    drawHelpAndPlay(canvas)
    
