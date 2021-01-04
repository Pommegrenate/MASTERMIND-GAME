import tkinter as tk
from tkinter import *


# Starting Screen ===========

startScreen = tk.Tk();
startScreen.title ("Catch Levoski");
startScreen.geometry ("500x500");
startScreen.resizable(width=FALSE, height=FALSE);

c = 250; # center of window

bgImage = PhotoImage(file = "C:\\Users\\Letitia\\Pictures\\FBL Badge.png");
bg = Label (startScreen, image = bgImage, bg = "grey");
bg.place (x = 0, y = 0, relwidth = 1, relheight = 1);

titleFrame = Frame (bg);
titleFrame.place (x = c, y = 150, anchor = 'center');

headingFrame = Frame (bg);
headingFrame.place (x = c, y = 225, anchor = 'center');

title = Label (titleFrame, text = "Catch Levoski");
title['font'] = ("Courier", 32, "bold");
title.pack ();

subheading = Label (headingFrame, text = "Are you ready to catch the undercover \n"
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
##story = Label (introScreen, text = "Hello, Fabulous Bureau of Liberations (FBL) \n"
##                                    "secret agent. This is the FBL headquarters. \n\n"
##                                    "Levoski, the undercover spy, has captured \n"
##                                    "your partner, Alina. She's trapped in a \n"
##                                    "locked room with him and it's up to you to \n"
##                                    "free her. You're the only FBL agent able to \n"
##                                    "do it. You just need to get past this locked \n"
##                                    "door to get to him. You'll need to use your \n"
##                                    "logical thinking and deduction skills to \n"
##                                    "solve his tricky code. \n\n"
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
##howToPlayScreen.geometry ("500x500");
##howToPlayScreen.resizable(width=FALSE, height=FALSE);
##
##c = 250;
##
##rulesTitle = Label (howToPlayScreen, text = "How to Play & Rules");
##rulesTitle['font'] = ("Helvetica", 25, "bold", "underline");
##rulesTitle.place (x = c, y = 25, anchor = 'center');
##
##instructions = Label (howToPlayScreen, text = "afa");
##instructions['font'] = ("Courier", 12);
##instructions.place (x = c, y = 200, anchor = 'center');
##
##rules = Label (howToPlayScreen, text = "ffafaaf");
##rules['font'] = ("Courier", 12);
##rules.place (x = c, y = 400, anchor = 'center');
##
##prevPage = Button (howToPlayScreen, text = "<< Prev. Page", command = introduction);
##prevPage.place (x = c, y = 475, anchor = 'center');
##prevPage['font'] = ("Helvetica", 10, "italic");
##
##ok = Button (howToPlayScreen, text = "OK")   #, command = GAME_COMMAND_GOES_HERE);
##ok.place (x = 465, y = 475, anchor = 'center');
##ok['font'] = ("Helvetica", 10, "italic");
