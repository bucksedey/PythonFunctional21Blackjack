#Author: Marco Flores https://github.com/bucksedey
"""
21 Blackjack Rules used in this program:
+   Original deck: [2,3,4,5,6,7,8,9,10,10,10,10,11]

+   The dealer will deal 2 random cards for each player which is you and the dealer
    each time the dealer gives a card to a player this card will not be in the main deck for the rest of the game.

+   11 is the Ace and if the player that holds it has more than 21 points it will be turned into a 1.

+   If you have not completed 21 points in your first deal, you can either stand (which it means to keep the cards you have) or deal one more 
    card.

+   You can only deal one more time since the first deal.

+   The dealer will deal for itself until it has over 17 points if it gets over 21 points without an ace you win.
    once the dealer is over 17 it will stop to deal cards and if it has the same amount of points as you it's a draw, 
    if it has more then you lose, if it has 21 you'll lose too.

+   If you have over 21 points you lose automatically.
"""
import random

def AsciiArt(): #THis is an ascii art i found at https://www.asciiart.eu/miscellaneous/playing-cards
    print("""
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
""")

#You is how I named the user for this program
def RandomCard(deck): #This function returns a random card from the main deck 
    size = len(deck)
    rnum = random.randint(0,size) #Gets a random number that will be used as index

    card = deck.pop(rnum-1) #Stores the value of the card poped at the previous random index

    return card #The card obtained from the deck

def FirstDeal(dealerDeck,yourDeck,deck): #This function deals 4 cards from the original deck, 2 cards for each player 
    i = 2
    while i>0:
        card = RandomCard(deck)
        dealerDeck.append(card) #adds an item (card) at the end of the list

        card = RandomCard(deck)
        yourDeck.append(card)
        i-=1

def YourPoints(yourDeck): #This function returns the amount of points you have
    points = 0
    for x in yourDeck:
        points = x + points
    return points

def DealerPoints(dealerDeck): #This function returns the amount of points the dealer has
    points = 0
    for x in dealerDeck:
        points = x + points
    return points

def CheckWinner(dealerDeck,yourDeck,deck): #This function checks if someone has already win at the first try
    if(YourPoints(yourDeck)==21):
        if(YourPoints(yourDeck)==DealerPoints(dealerDeck)): 
            print("It's a Draw")
            Ending(dealerDeck,yourDeck)
        else:
            print("You Win!!")
            Ending(dealerDeck,yourDeck)
    elif(DealerPoints(dealerDeck)==21):
        print("You Lose :(")
        Ending(dealerDeck,yourDeck)
    else: #Here you will choose if you want to stand or deal 
        choice = 'd'
        while(choice != 'd' or choice != 's'):
            choice = input("To stand press 's' to deal press 'd'?: ")
            if(choice.lower() == 'd'):
                Deal(dealerDeck,yourDeck,deck)
                break
            elif(choice.lower() == 's'):
                DealerDeal(dealerDeck,yourDeck,deck)
                break
            else:
                print("invalid input, try again")

def Deal(dealerDeck,yourDeck,deck): #Get a random card to your deck from the general deck
    card = RandomCard(deck)
    yourDeck.append(card) 
    

    RelevantInfo(dealerDeck,yourDeck)
    AceHandling(dealerDeck,yourDeck)

    if(YourPoints(yourDeck)>21):
        print("You lose ;(")
        Ending(dealerDeck,yourDeck)
    else:
        DealerDeal(dealerDeck,yourDeck,deck)

def DealerDeal(dealerDeck,yourDeck,deck): #This function will deal cards for the dealer until it has 17 or plus points
    while(DealerPoints(dealerDeck) <= 17):
        card = RandomCard(deck)
        dealerDeck.append(card)
        AceHandling(dealerDeck,yourDeck)
    
    if(DealerPoints(dealerDeck)==21): #If you have 21 and dealer too it's a draw
        if(DealerPoints(dealerDeck)==YourPoints(yourDeck)):
            print("It's a Draw")
            Ending(dealerDeck,yourDeck)
        else:
            print("You lose")   #You lose, dealer has 21 points and you don't
            Ending(dealerDeck,yourDeck)
    elif(DealerPoints(dealerDeck)>21): #You win if dealer has over 21 points
        print("Dealer got over 21 points, You Win!!") 
        Ending(dealerDeck,yourDeck)
    else:
        if(DealerPoints(dealerDeck)>YourPoints(yourDeck)): #If dealer has more points than you 
            print("You lose ;(")
            Ending(dealerDeck,yourDeck)
        elif(DealerPoints(dealerDeck)==YourPoints(yourDeck)): #If you have the same amount of points it's a draw
            print("It's a Draw")
            Ending(dealerDeck,yourDeck)
        else:
            print("You Win!!!")     #If you have more points than the dealer
            Ending(dealerDeck,yourDeck)

def AllInfo(dealerDeck,yourDeck): #This function shows all the info into the terminal at the end of the game

    print("\nFinal scores and decks:\n")
    print(f"Dealer's deck is: {dealerDeck}")
    print(f"Dealer's final points: {DealerPoints(dealerDeck)}")
    print(f"Your deck is: {yourDeck}")
    print(f"Your final points: {YourPoints(yourDeck)}")

def RelevantInfo(dealerDeck,yourDeck): #This function only shows the relevant info to you it not reveals all the info about the dealer
    print(f"\nDealer's first card is: {dealerDeck[0]}")
    print(f"Your deck is: {yourDeck}")
    print(f"Your points: {YourPoints(yourDeck)}")

def AceHandling(dealerDeck,yourDeck): #This function handles when a player has an ace (11) in its deck and has over 21 points
    if(YourPoints(yourDeck)>21):
        if 11 in yourDeck: 
            aceIndex = yourDeck.index(11)
            yourDeck[aceIndex]=1 #If you have over 21 points your ace(11) will be changed for 1 
            print("Your ace has changed from 11 to 1\n")
    elif(DealerPoints(dealerDeck)>21):
        if 11 in dealerDeck:
            aceIndex = dealerDeck.index(11)
            dealerDeck[aceIndex]=1#If dealer has over 21 points its ace(11) will be changed for 1 
            print("Dealer's ace has changed from 11 to 1\n")

def Ending(dealerDeck,yourDeck): #This function calls the other function AllInfo in order to display all the information about the game
    AllInfo(dealerDeck,yourDeck)
    print("Thanks for playing!!")

    while(True): #This message will ask if you want to keep playing or not
        sel = input("Do you want to play again? (y/n): ")
        if(sel.lower() == 'y'):
            Menu()
        elif(sel.lower() == 'n'):
            print("goodbye")
            exit()
        else:
            print("Invalid input, try again")

def Menu(): #This is the main function of the code, it will call the rest of the functions
    AsciiArt()
    print("\nHello, Welcome to 21 blackjack game\n")

    #The following lists or arrays will be used in the rest of the code but it is important to restart them on each run

    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10] #This is the main deck that will be used in the rest of the code
    dealerDeck = [] #Dealer's deck
    yourDeck = [] #User's deck 

    
    FirstDeal(dealerDeck,yourDeck,deck) 
    RelevantInfo(dealerDeck,yourDeck)
    CheckWinner(dealerDeck,yourDeck,deck)


Menu()