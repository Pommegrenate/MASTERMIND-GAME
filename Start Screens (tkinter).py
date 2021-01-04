import tkinter as tk
from tkinter import *


# Starting Screen ===========

startScreen = tk.Tk();
startScreen.title ("Catch Levoski");
startScreen.geometry ("500x500");
startScreen.resizable(width=FALSE, height=FALSE);

c = 250; # center of window

bgImage = PhotoImage(file = "C:\\Users\\Letitia\\Pictures\\FBL Badge.png"); # Everyone will need to change it to the file location of where they put this badge image
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

start = Button (startScreen, text = "Start", command = introduction); # All of the buttons need a function to work but idk how to make each screen into a function yet
start.place (x = c, y = 400, anchor = 'center');
start['font'] = ("Helvetica", 12);

startScreen.mainloop();


# Introduction Screen ==============

##introScreen = tk.Tk();
##introScreen.title ("Catch Levoski: Introduction");
##introScreen.geometry ("500x500");
##introScreen.resizable(width=FALSE, height=FALSE);
##
##c = 250;
##
##introTitle = Label (introScreen, text = "Introduction");
##introTitle['font'] = ("Helvetica", 25, "bold", "underline");
##introTitle.place (x = c, y = 25, anchor = 'center');
##
##story = Label (introScreen, text = "Hello, Fabulous Bureau of Liberations (FBL)\n"
##                                    "secret agent. This is the FBL headquarters.\n\n"
##                                    "Levoski, the undercover spy, has captured\n"
##                                    "your partner, Alina. She's trapped in a\n"
##                                    "locked room with him and it's up to you to\n"
##                                    "free her. You're the only FBL agent able to\n"
##                                    "do it. You just need to get past this locked\n"
##                                    "door to get to him. You'll need to use your\n"
##                                    "logical thinking and deduction skills to\n"
##                                    "solve his tricky code.\n\n"
##                                    "Good luck agent, report back soon.");
##story['font'] = ("Courier", 12);
##story.place (x = c, y = 200, anchor = 'center');
##
##nextPage = Button (introScreen, text = "Next Page >>", command = howToPlay);
##nextPage.place (x = c, y = 475, anchor = 'center');
##nextPage['font'] = ("Helvetica", 10, "italic");
##
##skip = Button (introScreen, text = "Skip")   #, command = GAME_COMMAND_GOES_HERE);
##skip.place (x = 460, y = 475, anchor = 'center');
##skip['font'] = ("Helvetica", 10, "italic");



# How to Play Screen =============

##howToPlayScreen = tk.Tk();
##howToPlayScreen.title ("Catch Levoski: How to Play & Rules");
##howToPlayScreen.geometry ("750x500");
##howToPlayScreen.resizable(width=FALSE, height=FALSE);
##
##c = 750/2;
##
##rulesTitle = Label (howToPlayScreen, text = "How to Play & Rules");
##rulesTitle['font'] = ("Helvetica", 25, "bold", "underline");
##rulesTitle.place (x = c, y = 25, anchor = 'center');
##
##instructions = Label (howToPlayScreen,
##                      text = "The door lock will have a randomly generated 4-digit code and you will have 12 tries to\n"
##                             "guess the correct code. If you don't guess it correctly in those 12 tries, then you wll \n"
##                             "fail the mission and Levoski will get away. Remember, the code can have duplicate numbers. \n"
##                             "For example the code could be '2533' or '1141'. \n\n"
##                             "To input your guess, use the 6 different numbers given at the bottom of the screen. \n"
##                             "If you make a mistake inputting your code, then you can redo that guess by pressing \n"
##                             "the 'Redo' button underneath the 6 numbers. \n"
##                             "When you are ready to submit your 4-digit guess, click on the 'Check' button beside the \n"
##                             "'Redo' button. \n\n"
##                             "When you submit your guess, the door will check if any of your inputs were correct \n"
##                             "using these indicators: \n"
##                             " - White dot when you guess a correct number but not in the correct position \n"
##                             " - Green dot when you guess a correct number AND in the correct position \n"
##                             " - Red dot when a number is not correct \n"
##                             "There will be 4 dots in total, the same as the number of digits in the code. \n\n"
##                             "If you did not correctly guess the entire code, then you'll have another guess, \n"
##                             "but you only have 12 in total so be careful. \n\n"
##                             "If you do guess the correct code, then you win! You made it in time to save Alina \n"
##                             "and beat Levoski!",
##                      justify = LEFT);
##instructions['font'] = ("Courier", 10);
##instructions.place (x = c, y = 250, anchor = 'center');
##
##prevPage = Button (howToPlayScreen, text = "<< Prev. Page", command = introduction);
##prevPage.place (x = c, y = 475, anchor = 'center');
##prevPage['font'] = ("Helvetica", 10, "italic");
##
##ok = Button (howToPlayScreen, text = "OK")   #, command = GAME_COMMAND_GOES_HERE);
##ok.place (x = 465, y = 475, anchor = 'center');
##ok['font'] = ("Helvetica", 10, "italic");
