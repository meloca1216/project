#############################################
###  draw help screen 
###  with directions
#############################################

# Megan Cahill
# mcahill

directions = "Directions.txt"

def loadTextString(fileName):
    fileHandler = open(fileName, "rt") # rt stands for read text
    text = fileHandler.read() # read the entire file into a single string
    fileHandler.close() # close the file
    return text

def drawHelpScreen(canvas):
    directs = loadTextString(directions)
    height = canvas.data["canvasH"]
    width = canvas.data["canvasW"]
    canvas.create_rectangle( 50, 50, width-50, height-50, fill = "magenta",
                             width = 0)
    canvas.create_text( width/2.0, height/2.0, text = directs,
                        font = ("Comic Sans MS Bold", "14"))
    ## "menu button"
    canvas.create_rectangle(width - 160, height - 110, width - 60, height- 60,
                            fill = "orange", width = 3)
    canvas.create_text(width - 110, height-85, text = "MENU",
                       font = ("Comic Sans MS Bold", "30"))
