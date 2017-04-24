##################################
###  Tests behind legal moves  ###
###    and words in Boggle,    ###
###   what screen it's on and  ###
### which game is being played ###
##################################


# Megan Cahill
# mcahill

def whichGameDice(canvas):
    four = canvas.data["fourByFour"]
    five = canvas.data["fiveByFive"]
    challenge = canvas.data["challengeCube"]
    diceSets = canvas.data["diceSets"]
    if four:
        if challenge:
            game = "fourChallenge"
        else:
            game = "fourByFour"
    if five:
        if challenge:
            game = "fiveChallenge"
        else:
            game = "fiveByFive"
    canvas.data["game"] = game
    dice = diceSets[game]
    return dice


def validMove(canvas, row, col):
    clicked = canvas.data["clicked"]
    (prevRow, prevCol) = clicked[-1]
    if (prevRow - row, prevCol - col) == (0,0):
        return False
    elif (abs(prevRow - row) > 1) or (abs(prevCol - col) > 1):
        return False
    else: return True

def wordsLongEnough(listOfWords):
    for entry in listOfWords:
        if len(entry) < 3:
            listOfWords.remove(entry)
    return listOfWords

def getBoggleDictionary(fileName):
    fileHandler = open(fileName, "rt")
    words = fileHandler.readlines() 
    fileHandler.close()
    words = words[0].split("\r")
    words = wordsLongEnough(words)
    return words

wordFile = "larger_dict.txt"
dictionary = getBoggleDictionary(wordFile)

def isValidWord(canvas,word):
    game = canvas.data["game"]
    wordsList = canvas.data["wordsList"]
    if word in wordsList:
        return False
    else:
        if game == "fourByFour" or game == "fourChallenge":
            if len(word) >= 3 and (word in dictionary):
                return True
            else:
                return False
        elif game == "fiveByFive" or game == "fiveChallenge":
            if len(word) >= 4 and (word in dictionary):
                return True
            else:
                return False

def getScore(canvas, word):
    clicked = canvas.data["clicked"]
    score = 0
    if ((canvas.data["challengeRowCol"] != None) and
        (canvas.data["challengeRowCol"] in clicked)):
        score += 3
    if len(word)<= 4:
        score += 1
    elif len(word) == 5:
        score += 2
    elif len(word) == 6:
        score += 3
    elif len(word) == 7:
        score += 5
    elif len(word) >= 8:
        score += 11
    return score

def submitWord(canvas, word):
    wordsAndPoints = canvas.data["wordsAndPoints"]
    wordsList = canvas.data["wordsList"]
    word = word.lower()
    if isValidWord(canvas, word):
        wordsList.append(word)
        points = getScore(canvas, word)
        wordsAndPoints[word] = points
        canvas.data["currentWord"] = ""
        canvas.data["clicked"] = []
    else:
        canvas.data["currentWord"] = ""
        canvas.data["clicked"] = []
        
