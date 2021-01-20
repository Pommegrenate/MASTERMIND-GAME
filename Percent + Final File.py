import tkinter as tk
from tkinter import *

from random import randint

# Commands for each button (closes the screen it's on and opens a new screen)
def startCommands ():
    introduction ();
    startScreen.destroy ();

def nextPageCommands ():
    howToPlay ();
    introScreen.destroy ();    

def prevPageCommands ():
    introduction ();
    howToPlayScreen.destroy ();

def skipCommands ():
    game ();
    introScreen.destroy ();
    
def okCommands ():
    game ();
    howToPlayScreen.destroy ();


# Starting Screen ===========

def gameTitle ():
    global bgImage, startScreen

    startScreen = tk.Tk ();
    startScreen.title ("Catch Levoski");
    startScreen.geometry ("500x500");
    startScreen.resizable(width=FALSE, height=FALSE);

    c = 250; # center of window

    bgImage = PhotoImage(file = "FBL Badge.png");
    bg = Label (startScreen, image = bgImage, bg = "grey");
    bg.place (x = 0, y = 0, relwidth = 1, relheight = 1);

    titleFrame = Frame (bg);
    titleFrame.place (x = c, y = 150, anchor = 'center');

    headingFrame = Frame (bg);
    headingFrame.place (x = c, y = 225, anchor = 'center');

    title = Label (titleFrame, text = "Catch Levoski");
    title['font'] = ("Courier", 32, "bold");
    title.pack ();

    subheading = Label (headingFrame, text = "Are you ready to catch the undercover\n"
                                             "spy, Levoski?");
    subheading['font'] = ("Courier", 14);
    subheading.pack ();

    start = Button (startScreen, text = "Start", command = startCommands);
    start.place (x = c, y = 400, anchor = 'center');
    start['font'] = ("Helvetica", 12);



# Introduction Screen ==============

def introduction ():
    global introScreen
    
    introScreen = tk.Tk ();
    introScreen.title ("Catch Levoski: Introduction");
    introScreen.geometry ("500x500");
    introScreen.resizable(width=FALSE, height=FALSE);

    c = 500/2;

    introTitle = Label (introScreen, text = "Introduction");
    introTitle['font'] = ("Helvetica", 25, "bold", "underline");
    introTitle.place (x = c, y = 25, anchor = 'center');

    story = Label (introScreen, text = "Hello, Fabulous Bureau of Liberations (FBL)\n"
                                        "secret agent. This is the FBL headquarters.\n\n"
                                        "Levoski, the undercover spy, has captured\n"
                                        "your partner, Alina. She's trapped in a\n"
                                        "locked room with him and it's up to you to\n"
                                        "free her. You're the only FBL agent able to\n"
                                        "do it. You just need to get past this locked\n"
                                        "door to get to him. You'll need to use your\n"
                                        "logical thinking and deduction skills to\n"
                                        "solve his tricky code.\n\n"
                                        "Good luck agent, report back soon.");
    story['font'] = ("Courier", 12);
    story.place (x = c, y = 200, anchor = 'center');

    nextPage = Button (introScreen, text = "Next Page >>", command = nextPageCommands);
    nextPage.place (x = c, y = 475, anchor = 'center');
    nextPage['font'] = ("Helvetica", 10, "italic");

    skip = Button (introScreen, text = "Skip", command = skipCommands);
    skip.place (x = 460, y = 475, anchor = 'center');
    skip['font'] = ("Helvetica", 10, "italic");



# How to Play Screen =============

def howToPlay ():
    global howToPlayScreen
    
    howToPlayScreen = tk.Tk ();
    howToPlayScreen.title ("Catch Levoski: How to Play & Rules");
    howToPlayScreen.geometry ("750x500");
    howToPlayScreen.resizable(width=FALSE, height=FALSE);

    c = 750/2;

    rulesTitle = Label (howToPlayScreen, text = "How to Play & Rules");
    rulesTitle['font'] = ("Helvetica", 25, "bold", "underline");
    rulesTitle.place (x = c, y = 25, anchor = 'center');

    instructions = Label (howToPlayScreen,
                          text = "The door lock will have a randomly generated 4-digit code and you will have 12 tries to\n"
                                 "guess the correct code. If you don't guess it correctly in those 12 tries, then you wll \n"
                                 "fail the mission and Levoski will get away. Remember, the code can have duplicate numbers. \n"
                                 "For example the code could be '2533' or '1141'. \n\n"
                                 "To input your guess, use the 6 different numbers given at the bottom of the screen. \n"
                                 "If you make a mistake inputting your code, then you can redo that guess by pressing \n"
                                 "the 'Erase' button underneath the 6 numbers. \n"
                                 "When you are ready to submit your 4-digit guess, click on the 'Check' button. \n\n"
                                 "When you submit your guess, the door will check if any of your inputs were correct \n"
                                 "using these star indicators: \n"
                                 " - Grey star when you guess a correct number but NOT in the correct position \n"
                                 " - Red star when you guess a correct number AND in the correct position \n"
                                 " - Black star when a number is not correct \n"
                                 "There will be 4 stars in total, the same as the number of digits in the code. \n\n"
                                 "If you did not correctly guess the entire code, then you'll have another guess, \n"
                                 "but you only have 12 in total so be careful. \n\n"
                                 "To take another guess after you've checked your answer, press the 'Erase' button. \n\n"
                                 "If you do guess the correct code, then you win! You made it in time to save Alina \n"
                                 "and beat Levoski!",
                          justify = LEFT);
    instructions['font'] = ("Courier", 10);
    instructions.place (x = c, y = 250, anchor = 'center');

    prevPage = Button (howToPlayScreen, text = "<< Prev. Page", command = prevPageCommands);
    prevPage.place (x = c, y = 475, anchor = 'center');
    prevPage['font'] = ("Helvetica", 10, "italic");

    ok = Button (howToPlayScreen, text = "OK", command = okCommands);
    ok.place (x = 715, y = 475, anchor = 'center');
    ok['font'] = ("Helvetica", 10, "italic");



# Game Screen =============


inputList = ''
numberOfGuess = 0;

c = 500/2;

def game ():
    global gameScreen, lblSecArrangement, percentText
    
    gameScreen = tk.Tk ();
    gameScreen.title("Catch Levoski: The Game");
    gameScreen.geometry ("500x550");
    gameScreen.resizable(width=FALSE, height=FALSE);


    lblTitle = Label(gameScreen, text = "Catch Levoski", fg = "RoyalBlue3");
    lblTitle['font'] = ("Courier", 25, "bold", "underline");
    lblTitle.place (x = c, y = 30, anchor = 'center');

    lblNGuess = Label(gameScreen, text = "Number of Guesses:  " + str(numberOfGuess))
    lblNGuess['font'] = ("Helvetica", 15);
    lblNGuess.place (x = c, y = 125, anchor = 'center');

    lblSecArrangement = Label(gameScreen, text="")
    lblSecArrangement['font'] = ("Helvetica", 15);
    lblSecArrangement.place (x = c, y = 175, anchor = 'center');

    percentText = Label (gameScreen, fg = "CadetBlue");
    percentText['font'] = ("Helvetica", 13);
    percentText.place (x = c, y = 350, anchor = 'center');

    gameButtons ();


# Buttons created for the game
def gameButtons ():
    global buttons, btnStartGame, btnCheck, btnEraseGame, number

    cMove = 250 - 65;

    buttons = []
    for number in range(0, 7):
        button = Button(gameScreen, text=number, command=lambda number=number: userInput(number), state=DISABLED)
        button['font'] = (10);
        buttons.append(button)

    btnStartGame = Button(gameScreen, text="Start Game", command=lambda : start())
    btnStartGame['font'] = (10);

    btnEraseGame = Button(gameScreen, text="Erase", command=lambda : erase())
    btnEraseGame['font'] = (10);
    
    btnCheck = Button(gameScreen, text="Check", command=lambda : check(), state = DISABLED)
    btnCheck['font'] = (10);

    btnStartGame.place (x = c, y = 500, anchor = 'center');

    for col in range(1, 7):
        buttons[col].place (x = cMove, y = 450, anchor = 'center');
        cMove += 25;




# Secret code (Random numbers)
state = "empty";

def code ():
    global arrayOfArrangement, backuplist
     
    secretArrangement = ''

    while len(secretArrangement) != 4 :  # While the number of arrayOfArrangement is NOT 4

        randomNumber = str(randint(1, 6)); # There are 6 numbers
        secretArrangement = secretArrangement + randomNumber;

    arrayOfArrangement = list(secretArrangement);
    backuplist = arrayOfArrangement

    print (arrayOfArrangement);

    return arrayOfArrangement


array = code()


# Start button changes to "Restart" and will display the game buttons (restart, erase, check)
def start ():
    global state
    
    for button in buttons :
        button["state"] = NORMAL

        if state =="empty":
            state = "started"
            btnStartGame["text"] = "Restart"
            btnStartGame.place (x = c - 100, y = 500, anchor = 'center');
            
            btnCheck.place (x = c + 100, y = 500, anchor = 'center');
            btnEraseGame.place (x = c + 25, y = 500, anchor = 'center');
            btnEraseGame["state"] = NORMAL
            
            array = code()
            blank()



# Outputs the user's input in a list until it hits 4
def userInput(number):
    global buttons, inputList, arrayOfInput

    IM = str(number)
    inputList = inputList + IM
    arrayOfInput = list(inputList)
    limit() #don't pass it


# Creates a limit on how many numbers you can input to 4
def limit(): #no parameter
    global state, arrayOfInput #add to globals in both defs
     

    if len(arrayOfInput) == 4:
        print(arrayOfInput)
        print("You've reached the last number you can enter.")
        btnCheck["state"] = NORMAL
        for button in buttons :
            button["state"] = DISABLED
            state ="empty"


    else:
        if len(arrayOfInput) == 1:
            print("You've just entered your 1st input number.")

        elif len(arrayOfInput) == 2:
            print("You've just entered your 2nd input number.")

        else:
            print("You've just entered your 3rd input number.")


arrayOfInput= [] #declare here but empty

# Makes numberOfGuess = 0 when you use press "Restart" button
def blank():
    global inputList, numberOfGuess

    inputList = ''
    numberOfGuess = 0
    lblNGuess = Label(gameScreen, text = "Number of Guesses:  " + str(numberOfGuess));
    lblNGuess['font'] = ("Helvetica", 15);
    lblNGuess.place (x = c, y = 125, anchor = 'center');


# Erases your current input and let's you make a new input
def erase():
    global inputList

    inputList = ''
    for button in buttons :
         button["state"] = NORMAL

# Checks if userInput matches with secret arrangement + adds to numberOfGuess counter
def check():
    global numberOfGuess, arrayOfArrangement
    
    numberOfGuess += 1
    
    lblNGuess = Label(gameScreen, text = "Number of Guesses:  " + str(numberOfGuess))
    lblNGuess['font'] = ("Helvetica", 15);
    lblNGuess.place (x = c, y = 125, anchor = 'center');
    
    if numberOfGuess == 2:
        for button in buttons:
            button["state"] = DISABLED

        btnCheck["state"] = DISABLED
        btnEraseGame["state"] = DISABLED

        print ("The secret arragement was : ", arrayOfArrangement)

        lblSecArrangement['text'] = "The secret code was: " + str(arrayOfArrangement)
               
          
    position()
    

# Digits that are the correct number AND in the correct position ****First
def position ():
    global lol, rightPosition
     
    lol = arrayOfArrangement[:]
    rightPosition = 0

    for x in range (0,4):
        if arrayOfInput[x] == lol[x]:
            lol[x] = ''
            arrayOfInput[x] = 'empty'
            rightPosition += 1
               
    wrongPosition(rightPosition)
         
# Digits that are the correct number NOT in the correct position
def wrongPosition (rightPosition):
    rightNum = 0
    count = 4;
    y = 0;

    while count != 0:
        for item in range (0, 4):
            if arrayOfInput[y] == lol[item]:
                arrayOfInput[y] = 'empty'
                lol[item] = ''
                rightNum += 1;  
                   
        y += 1
        count -= 1

         
    btnCheck["state"] = DISABLED
    
    for button in buttons :
        button["state"] = DISABLED


    indicator(rightPosition, rightNum)
          

# Indicator stars
def indicator (bothRight, oneRight):
    indicatorsTitle = Label(gameScreen, text = "Indicators");
    indicatorsTitle['font'] = ("Helvetica", 17, "underline");
    indicatorsTitle.place (x = c, y = 225, anchor = 'center');
    
    q = 196; # Placement of stars on x-axis
    
    # Position + number is correct

    for star in range (0, bothRight):
        bothIndic = Label (gameScreen, text = "*", fg = "red");
        bothIndic['font'] = ("Helvetica", 25);
        bothIndic.place (x = q, y = 250);
        q += 30;
      
     
    # Number is correct
    for star in range (0, oneRight):
        oneIndic = Label (gameScreen, text = "*", fg = "grey");
        oneIndic['font'] = ("Helvetica", 25);
        oneIndic.place (x = q, y = 250);
        q += 30;

    # Not correct
    noneRight = 4 - bothRight - oneRight;

    for star in range (0, noneRight):
        noneIndic = Label (gameScreen, text = "*", fg = "black");
        noneIndic['font'] = ("Helvetica", 25);
        noneIndic.place (x = q, y = 250);
        q += 30;

        msgPercents (bothRight)




def msgPercents (bothRight):
    global percentText
    
    percentage = float((bothRight / 4) * 100);
    
    if bothRight == 0:
        percentMsg = "Ohh that's not the right code at all... Well keep trying FBL agent. \nWe won't fire you just because of this. \nYou got ";
        
    elif bothRight == 4:
        percentMsg = "You did it! You solved the code in time! \nNow you can save Alina and catch Levoski. \nYou got ";
        
    else:
        percentMsg = "You're getting there. Once you unlock this door, Alina will be saved! \nYou got ";
        
    percentText.config (text = str(percentMsg) + str(percentage) + "% correct out of 100.0%!")

    

    




# Main Program =============================

gameTitle();


