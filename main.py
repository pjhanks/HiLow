# High Low card game
# From Object Oriented Python by Irv Kalb

import random

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
              'Queen', 'King')

NCARDS = 4

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

# Main
print('Welcome to Hi/Lo!')
print('You have to choose whether the next card to be shown will be higher or'
      'lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points!')
print('You have 50 points to start')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):
        answer = input('Willl the next card be higher or lower than the ' +
                       currentCardRank + ' of ' + currentCardSuit
                       + '? (enter h or l): ')
        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher!')
                score = score + 20
            else:
                print('Sorry, you chose higher but it was lower :(')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print('You got it right, it was lower!')
                score = score + 20
            else:
                print('Sorry, you chose lower but it was higher :(')
                score = score - 15

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')