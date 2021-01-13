import tkinter
import random as rnd

# variables that are going to be used as global
userChoice = None
previousResults = []

# -------- functions ----------

# this method checks whether the input is within the specified range and if so, it sends you to the in-game menu.
def playGame():
    global userChoice
    try:
        userChoice = int(numberOfDice.get())
    except:
        emptyWarning = tkinter.Label(text="You must enter a number.")
        emptyWarning.pack()

    if not userChoice:
        pass
    elif userChoice < 1 or userChoice > 3:
        warning = tkinter.Label(text="The value must be between 1 and 3. Please try again.")
        warning.pack()
    else:
        menuWindow.destroy()

        gameWindow = tkinter.Tk()
        gameWindow.title("Dice Rolling Simulator")
        gameWindow.geometry("300x500")

        rollDiceButton = tkinter.Button(gameWindow, text="Roll Dice", width=10, height=2, command=rollDice)
        rollDiceButton.pack(pady=5)

        clearButton = tkinter.Button(gameWindow, text="Clear", width=10, height=2, command=clearPreviousResults)
        clearButton.pack(pady=5)

        exitGameButton = tkinter.Button(gameWindow, text="Quit Game", width=10, height=2, command=quit)
        exitGameButton.pack(side=tkinter.BOTTOM)

# this method can be executed for as many times as the user wants.
def rollDice():
    global previousResults
    numbers = []
    for i in range(userChoice):
        number = rnd.randint(1, 6)
        numbers.append(number)

    diceResult = tkinter.Label(text=numbers, font=("Calibri", 12))
    diceResult.pack()
    previousResults.append(diceResult)

# displaying latest outputs by clearing more previous ones.
def clearPreviousResults():
    global previousResults
    for eachResult in previousResults:
        eachResult.destroy()

# -------- main ----------
menuWindow = tkinter.Tk()
menuWindow.title("Dice Rolling Simulator")
menuWindow.geometry("600x300")

welcomeMessage = tkinter.Label(menuWindow, text="Welcome to Dice Rolling Simulator!", font=("Calibri", 20, "bold"))
welcomeMessage.pack(pady=20)

diceInfo = tkinter.Label(menuWindow,
                         text="Please enter the number of dice you want to play with (at most 3, at least 1): ",
                         font=("Calibri", 12))
diceInfo.pack(pady=20)

numberOfDice = tkinter.Entry(menuWindow, font=("Calibri", 12))
numberOfDice.pack(pady=10)

playGameButton = tkinter.Button(menuWindow, text="Play", width=10, height=2, command=playGame)
playGameButton.pack(pady=20)

menuWindow.mainloop()
