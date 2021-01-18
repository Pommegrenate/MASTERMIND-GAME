import tkinter as tk
from tkinter import *

from random import randint

inputList = ''
numberOfGuess = 0;

c = 250; # Center of screen on x-axis

gameScreen = tk.Tk();
gameScreen.title("Catch Levoski: The Game");
gameScreen.geometry ("500x550");
gameScreen.resizable(width=FALSE, height=FALSE);


lblTitle = Label(gameScreen, text = "Catch Levoski", fg = "RoyalBlue3");
lblTitle['font'] = ("Courier", 25, "bold", "underline");
lblTitle.place (x = c, y = 30, anchor = 'center');

lblLine0 = Label(gameScreen, text = "************we'll design empty space if we can************");
lblLine0['font'] = ("Helvetica", 15);
lblLine0.place (x = c, y = 75, anchor = 'center');

lblNGuess = Label(gameScreen, text = "Number of Guesses:  " + str(numberOfGuess))
lblNGuess['font'] = ("Helvetica", 15);
lblNGuess.place (x = c, y = 125, anchor = 'center');

lblSecArrangement = Label(gameScreen, text="We'll show the secret arrangement here")
lblSecArrangement['font'] = ("Helvetica", 15);
lblSecArrangement.place (x = c, y = 175, anchor = 'center');



buttons = []
for number in range(0, 7):
    button = Button(gameScreen, text=number, height=1, width=1, command=lambda number=number: input(number), state=DISABLED)
    button['font'] = (10);
    buttons.append(button)

btnStartGame = Button(gameScreen, text="Start Game", command=lambda : start())
btnStartGame['font'] = (10);


cMove = 250 - 65;

for col in range(1, 7):
          buttons[col].place (x = cMove, y = 450, anchor = 'center');
          cMove += 25;

btnStartGame.place (x = c, y = 500, anchor = 'center');



state = "empty"



def start():
    global state

    for button in buttons :
        button["state"] = NORMAL

        if state =="empty":
            state = "started"
            btnStartGame["text"] = "Restart"
            erase()


def input(i):
    global buttons, inputList


    ImtiredOfAssigningVariable = str(i)
    inputList = inputList + ImtiredOfAssigningVariable
    arrayOfInput = list(inputList)
    limit(arrayOfInput)
    
    print(arrayOfInput)
    return(arrayOfInput)


def limit(arrayOfInput):
     global state

     if len(arrayOfInput) == 4:

          for button in buttons :
               button["state"] = DISABLED
               state ="empty"


def erase():
     global inputList, numberOfGuess

     inputList = ''
     numberOfGuess = 0
     
