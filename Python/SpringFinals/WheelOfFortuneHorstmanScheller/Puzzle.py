import random
from player import Player
#import WoFWheel
playing=True
buying=False
guessing=False
singleguess=True
class Puzzle:
    moneylist=[0,-1,200,250,300,350,400,450,500,550,600,650,700,750]
    wordlist=[]
    blankslist=[]
    guesses=[]
    guess=['CONSIDER','EVIDENT','PRACTICE','STRAWBERRY','FRIENDSHIP','EVERYTHING','MOTIVATION','APPRECIATE','FRIENDSHIP']
    def getWord():
        word=random.choice(Puzzle.guess)
        del Puzzle.guess[Puzzle.guess.index(word)]
        return word
    playing=True
    #Guessing The Word
    #Set Word list and Blank list equal to Length of Word
    def getBlanks(word):
        for i in range(len(word)):
            Puzzle.blankslist.append('_')
            Puzzle.wordlist.append(word[i])

    def addturn(playerturn):
        playerturn+=1
        if playerturn>3:
            playerturn=1
        return playerturn
        
    def playerguess(word,wordlist,blankslist,guesses,playerturn):
        global pint
        global guessing
        global buying
        global singleguess
        money=random.choice(Puzzle.moneylist)
        while Puzzle.playing==True:
            
            
            
            
            
    #Print Out Info
            if money==0:
                print('\nIt is '+Player.playernames[playerturn-1]+"'s turn")
                print('and they got a BANKRUPT')
                print('\n\n\n\n\n')
                Player.playerlist[playerturn-1]-=Player.playerlist[playerturn-1]
                money=random.choice(Puzzle.moneylist)
                playerturn=Puzzle.addturn(playerturn)
            elif money==(-1):
                print('\nIt is '+Player.playernames[playerturn-1]+"'s turn")
                print('and they got a LOSE A TURN')
                print('\n\n\n\n\n')
                money=random.choice(Puzzle.moneylist)
                playerturn=Puzzle.addturn(playerturn)
            if money>0:
                print('\n\n\n\n\n')
                
                print(word)
                print("$"+str(money))
            for i in range(len(blankslist)):
                print(blankslist[i]+' ', end = '')
            print("\n")
            print('Guesses:')
            for i in range(len(guesses)):
                print(guesses[i]+' ', end = '')
#                                                            https://www.articledesk.net/python-print-without-new-line/ no new line for print statement
            print('\nIt is '+Player.playernames[playerturn-1]+"'s turn")
            print(Player.playernames[playerturn-1],"'s balance: $"+str(Player.playerlist[playerturn-1]))
            print("type 'Guess' to Guess\ntype 'Buy' to Buy a vowel")
            pint=str.upper(input('\n'))
            print('\n\n\n\n\n')
            
            
            
            
    #Check if Guess is valid
            if len(pint)==1:
                if str.isalpha(pint)==True: 
                                    #https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-letters-in-python is alphabetical character
                    if not(pint in "AEIOUaeiou"):
                        if not(pint in guesses):
                            playerturn,money=Puzzle.checkword(word,wordlist,blankslist,guesses,money,playerturn)
                        else:
                            print('Sorry Try Again')
                    elif buying==True:
                        playerturn,money=Puzzle.checkword(word,wordlist,blankslist,guesses,money,playerturn)
                        buying=False
                    else:
                        print("Sorry You Havn't asked to buy a vowel")
                else:
                    print('Sorry Try Again')
                    
                    
                    
            #if player would like to guess the word
            elif pint == "GUESS":
                guessing=True
                
                
                
            #if player wants to buy a vowel
            elif pint == "BUY":
                if Player.playerlist[playerturn-1] >=250:
                    Player.playerlist[playerturn-1]-=250
                    buying=True
                else:
                    print("Sorry You Don't have enough money")     
            elif guessing==True:
                if pint==word:
                    Player.playerlist[playerturn-1]+=1000
                    print('The Winner for this puzzle Is: '+Player.playernames[playerturn-1])
                    Puzzle.playing=False
                else:
                    guessing=False
                    money=random.choice(Puzzle.moneylist)
                    playerturn=Puzzle.addturn(playerturn)
            else:
                print('Sorry Try Again')
            







    def checkword(word,wordlist,blankslist,guesses,money,playerturn): #needs work
        guesses.append(pint)
        if pint in wordlist:
            for i in range(len(wordlist)):
                if pint == wordlist[i]:
                    blankslist[i]=pint
                    Player.playerlist[playerturn-1]+=money
        else:
            playerturn=Puzzle.addturn(playerturn)
        money=random.choice(Puzzle.moneylist)
        return playerturn,money
    
    def go(turn):
        playerturn=turn
        word=Puzzle.getWord()
        Puzzle.getBlanks(word)
        blankslist=Puzzle.blankslist
        wordlist=Puzzle.wordlist
        guesses=Puzzle.guesses
        Puzzle.playerguess(word,wordlist,blankslist,guesses,playerturn)
        