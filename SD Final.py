import tkinter as tk
import random

def diceRoll():
    #Generates a random number between one and six to be seen in dice_label
    number = random.randint(1, 6)
    dice_label["text"] = number
    
def coin():
    #Shows the coin window and hides the dice window
    top_level.deiconify()
    window.withdraw()

def returnButton():
    #shows the dice window and re-hides the coin window
    top_level.withdraw()
    window.deiconify()
    
def coinFlip():
    #Generates a random number between 1 and 2. If 1, outputs "Heads", if 2, outputs "Tails"
        face = random.randint(1, 2)
        if face == 1:
            coin_label["text"] = "Heads"
        elif face == 2:
            coin_label["text"] = "Tails"

#Generates the main dice window and configures it
window = tk.Tk()
window.title("Dice Game")
window.columnconfigure(1, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)

#Generates the widgets for the dice window
dice_label = tk.Label(window, text=0)
dice_button = tk.Button(window, text = "Roll", command = diceRoll)
coin_button = tk.Button(window,
                 text = "Coin Game",
                 command = coin)
#Places the widgets on the dice window
dice_button.grid(row=0,column = 0, padx=5)
dice_label.grid(row=0, column = 1, padx=5)
coin_button.grid(row=1, column = 0, padx=5)

#Generates configures the coin window and hides it
#until coin game button is pressed

top_level = tk.Toplevel(window)
top_level.title("Coin Game")
top_level.withdraw()

#Generates widgets for the coin window
return_button = tk.Button(top_level,
                          text = "Return",
                          command = returnButton)

coin_flip = tk.Button(top_level, text="Flip", command = coinFlip)

coin_label = tk.Label(top_level, text="______")

#Places the widgets on the coin window
return_button.grid(row=1, column = 0, padx=5)
coin_label.grid(row=0,column=1, padx=5)
coin_flip.grid(row=0, column=0, padx=5)

#Runs the program
window.mainloop()
