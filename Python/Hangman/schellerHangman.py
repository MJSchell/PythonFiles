import random


guess=['CONSIDER','EVIDENT','PRACTICE']
word=random.choice(guess)
wordlist=[]
playerturn=True
blanks=''
blankslist=[]
strikes=0
guesses=[]

#Set Word list and Blank list equal to Length of Word
for i in range(len(word)):
    blankslist.append('_')
    wordlist.append(word[i])


def playerguess(blanks,word,strikes,wordlist,blankslist,guesses):
    playerturn=True
#Set blanks equivilent to if guess is right
    blanks=''
    for i in range(len(blankslist)):
        blanks+=blankslist[i]+' '
    while playerturn==True:
#Print Out Info
        print('\n\n\n\n\n'+blanks)
        print('Strikes:',strikes)
        print('Guesses:')
        for i in range(len(guesses)):
            print(guesses[i]+' ', end = '')
                                                        #https://www.articledesk.net/python-print-without-new-line/ no new line for print statement
        pint=str.upper(input('\nGuess:'))
#Check if Guess is valid
        if len(pint)==1:
            if str.isalpha(pint)==True: 
                                                        #https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-letters-in-python is alphabetical character
                checkword(blanks,word,strikes,wordlist,blankslist,guesses,pint)
                playerturn=False
            else:
                print('Sorry Try Again')
        else:
            print('Sorry Try Again')


def checkword(blanks,word,strikes,wordlist,blankslist,guesses,pint):
    guesses.append(pint)
#if guess is in word
    if pint in wordlist:
        for i in range(len(wordlist)):
            if wordlist[i]==pint:
                blankslist[i]=pint
#if guess not in word
    else:
        strikes+=1
#win condition
    if not('_' in blankslist):
        print('\n\n\n\n\n\nYou Won ')
        print('Your Word Is:', word)
    if '_' in blankslist:
#loss condition
        if strikes<=6:
            playerguess(blanks,word,strikes,wordlist,blankslist,guesses)
        else:
            print('\n\n\n\n\n\nGAME OVER ')

#Run/Main  
playerguess(blanks,word,strikes,wordlist,blankslist,guesses)