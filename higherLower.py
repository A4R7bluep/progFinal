''' 
**************************************************
	Program: HigherOrLower
	Definition: This program will play a game with the user of higher or lower.
        It will generate a deck of cards and the computer and user will draw
        a random card from the deck and see which is higher. 
        The person with the higher card wins.

	Author: Ross Gibson
	Date: 2/27/24
	History:
**************************************************
'''


"""
    import random

    object[] deck = []
    int gamesWon = 0
    int gamesLost = 0

    class card
        constructor(assigned suit and number)
            string suit = assigned suit
            string number = assigned number
        endconstructor
    endclass


    procedure deck_setup()
        string[] suits = array of suits as strings
        string[] numbers = array of numbers and faces as strings

        for loop through all 4 suits
            for loop through all 13 numbers and faces
                create object from class card and send suit and number
            endfor
        endfor
    endprocedure

    procedure higher_lower(the computer's card, the user's card)
        result = get input from user whether the card is higher or lower

        if computer's card is lower than user's and user said lower
            gamesWon += 1
            print that user won

        else if computer's card is higher than user's and user said lower
            gamesLost += 1
            print that computer won

        else if if computer's card is higher than user's and user said higher
            gamesWon += 1
            print that user won

        else if computer's card is lower than user's and user said higher
            gamesLost += 1
            print that computer won
        
        else
            print a tie
        endif
    endprocedure

    run deck_setup()

    do
        int computeridx = random number for deck array index
        object computercard = deck[computeidx]
        pop card from deck at index computeridx
        output that computer has picked a card

        wait for user to press enter to chose card
        int useridx = random number for deck array index
        object usercard = deck[useridx]
        pop card from deck at index useridx
        output that user picked card

        higher_lower(computer's card, user's card)

    while deck is not empty or user wants to continue game (prompt user)
"""

from random import randint, shuffle
from cardImages import Card_Imgs

class Term:
    """
    =================================================== 
        Class: Term
        Definition: contains ANSI escape sequences for text formatting
        Author: Ross Gibson
        Date: 2/27/24
        History: 
    ===================================================
    """
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033c'

class Card:
    """
    =================================================== 
        Class: Card 
        Definition: contains the suit and number, 
            and an abbreviated way to display the card
        Author: Ross Gibson
        Date: 2/27/24
        History: 
    ===================================================
    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.cardImg = Card_Imgs.return_card(suit, str(number))
        # self.cardImg = ""

        if number < 11:
            self.numberName = str(number)
        else:
            match number:
                case 11:
                    self.numberName = "Jack"
                case 12:
                    self.numberName = "Queen"
                case 13:
                    self.numberName = "King"
                case 14:
                    self.numberName = "Ace"

    def __repr__(self):
        return f"{Term.BOLD}{Term.CYAN}{self.numberName} of {self.suit}{Term.ENDC}"

def deck_setup():
    """
    =================================================== 
        Function: deck_setup 
        Definition: creates the deck before playing
        Author: Ross Gibson
        Date: 2/27/24
        History: 
    ===================================================
    """

    deck = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for suit in suits:
        for number in numbers:
            deck.append(Card(suit, number))
    
    shuffle(deck)
    
    return deck


def higher_lower(computercard, usercard):
    """
    =================================================== 
        Function: higher_lower 
        Definition: compares the user's card to the computer's card
        Author: Ross Gibson
        Date: 2/27/24
        History: 
    ===================================================
    """

    response = input(f"{Term.BOLD}Is the card you chose higher or lower than my card?: {Term.ENDC}").lower()

    if computercard.number > usercard.number and response == "higher":
        print(f"{Term.RED}Incorrect! Computer had {computercard}{Term.RED}, and you had {usercard}{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
        
        return -1 # for a user loss
    
    elif computercard.number < usercard.number and response == "lower":
        print(f"{Term.RED}Incorrect! Computer had {computercard}{Term.RED}, and you had {usercard}{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
        
        return -1 # for a user loss
    
    elif computercard.number < usercard.number and response == "higher":
        print(f"{Term.GREEN}Correct! Computer had {computercard}{Term.GREEN}, and you had {usercard}{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
        
        return 1 # for a user win
    
    elif computercard.number > usercard.number and response == "lower":
        print(f"{Term.GREEN}Correct! Computer had {computercard}{Term.GREEN}, and you had {usercard}{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
        
        return 1 # for a user win
    
    elif computercard.number == usercard.number:
        print(f"{Term.ORANGE}A tie ocurred. Computer had {computercard}{Term.ORANGE}, and you had {usercard}{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
        
        return 0 # for a tie
    
    else:
        print(f"{Term.BOLD}{Term.RED}Incorrect Response!{Term.ENDC}")
        
        for i in range(len(computercard.cardImg)):
            print(f"{computercard.cardImg[i]}       {usercard.cardImg[i]}")
    
    
    


if __name__ == "__main__":
    deck = []
    gamesWon = 0
    gamesLost = 0

    deck = deck_setup()

    print(Term.CLEAR)

    cont = True

    while len(deck) != 0 and cont:
        computeridx = randint(0, len(deck) - 1)
        computercard = deck.pop(computeridx) # pop returns removed item
        print("Computer has picked a card")

        useridx = randint(0, len(deck) - 1)
        usercard = deck.pop(useridx) # pop returns removed item
        print(f"Your card is the {usercard}")

        result = higher_lower(computercard, usercard)
        
        match result:
            case 1: # user won
                gamesWon += 1
            case -1: # user loss
                gamesLost += 1

        cont = input(f"{Term.BOLD}Do you want to continue playing? [y/N]: {Term.ENDC}").upper()
        
        match cont:
            case "Y":
                cont = bool(True)
            case "N":
                cont = bool(False)
            case _:
                print("Incorrect Format, considering as False")
                cont = bool(False)
        
        print()

    print(f"{Term.BOLD}You won {gamesWon} times, and lost {gamesLost} times{Term.ENDC}")