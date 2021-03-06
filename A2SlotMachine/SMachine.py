# Source File Name: slotmachine.py
# Author's Name: Tom Tsiliopoulos
# Last Modified By: Harsimrat Kaur
# Date Last Modified: Tuesday May 22, 2012
""" 
  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module

  Version: 0.1 - * Created Back end functions for the slot machine program Reels, pullthehandle, and
                 is_number (a validation function).
                 * Text output provides debugging information to check if the Slot Machine program does
                 what it's supposed to do.
                 * Used research from the internet to set the Reels function to simulate basic slot reels
"""

# import statements
import pygame, pygame.font, pygame.event, pygame.draw, string, random
from pygame.locals import *
pygame.init()
pygame.mixer.init()

#Supplied Code
def spin(player_cash, jackpot, Bet):
    player_cash -= Bet
    jackpot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    line_Reel = Reels()
    Fruits = line_Reel[0] + " - " + line_Reel[1] + " - " + line_Reel[2]
    winnings = 0
    jackPot = False
    
    # Match 3
    if line_Reel.count("Grapes") == 3:
        winnings,win = Bet*20,True
    elif line_Reel.count("Lime") == 3:
        winnings,win = Bet*30,True
    elif line_Reel.count("Orange") == 3:
        winnings,win = Bet*40,True
    elif line_Reel.count("Cherry") == 3:
        winnings,win = Bet*100,True
    elif line_Reel.count("Bar") == 3:
        winnings,win = Bet*200,True
    elif line_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif line_Reel.count("Seven") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif line_Reel.count("Blank") == 0:
        if line_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if line_Reel.count("Lime") == 2:
            winnings,win = Bet*2,True
        elif line_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif line_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif line_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif line_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif line_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
    elif line_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
    else:
            winnings, win = Bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        player_cash += int(winnings)

def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Grapes"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Banana"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Orange"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Cherry"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Bar"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Bell"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Seven"    

    
    return Bet_Line
def increaseBet(bet, player_cash):
    if(player_cash <= bet):
        return player_cash
    else:
        if(bet == 100):
            return bet
        else:
            return bet + 1

def decreaseBet(bet):
    if(bet == 0):
        return bet
    else:
        return bet - 1


def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    
    # Match 3
    if Fruit_Reel.count("Grapes") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("Banana") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("Orange") == 3:
        winnings,win = Bet*40,True
    elif Fruit_Reel.count("Cherry") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("Bar") == 3:
        winnings,win = Bet*200,True
    elif Fruit_Reel.count("Bell") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("Seven") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("Blank") == 0:
        if Fruit_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("Banana") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win

def main():
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    screen = pygame.display.set_mode((406, 407))    
    #create background
    background = pygame.image.load("images/slot-machine.gif")
    
    #create images
    reel1 = pygame.image.load("images/spin.gif")
    reel2 = pygame.image.load("images/spin.gif")
    reel3 = pygame.image.load("images/spin.gif")
    
    enoughCredits = True
    #create sound
    startup = pygame.mixer.Sound("Sounds/machine.wav")
    startup.play()
    #Render
    screen.blit(background, (0, 0))
    screen.blit(reel1, (65,155))
    screen.blit(reel2, (170,155))
    screen.blit(reel3, (275,155))
    
    
if __name__ == "__main__": main()
