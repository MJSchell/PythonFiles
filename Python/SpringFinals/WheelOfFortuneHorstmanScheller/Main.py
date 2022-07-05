from Puzzle import Puzzle
from player import Player
import random
listy=[]

def reset():
    Puzzle.playing=True
    Puzzle.buying=False
    Puzzle.guessing=False
    Puzzle.singleguess=True
    Puzzle.wordlist=[]
    Puzzle.blankslist=[]
    Puzzle.guesses=[]
#If you get lost ---> https://runestone.academy/ns/books/published/fopp/Inheritance/chapterProject.html ---- A helpful tool or way of rethinking
print("Americas game, Wheeeeeeeeeeeeeel of Fortune! The worlds most popular game\n")
print("show! And now, from the Sony Studios, here they are the stars of our show, Pat Sajak\n")
print("and Vanna White!\n")

pin=input("Please enter player 1's names\n")
listy.append(pin)
pin=input("Please enter player 2's names\n")
listy.append(pin)
pin=input("Please enter player 3's names\n")
listy.append(pin)

for i in range(3):
    number=random.randint(0,len(listy)-1)
    Player.playernames.append(listy[number])
    del listy[number]
Puzzle.go(1)

reset()

Puzzle.go(1)

reset()

Puzzle.go(1)

reset()

Puzzle.go(1)

print("Final Scores:\n")
for i in range(3):
    print(Player.playernames[i],"'s balance: $"+str(Player.playerlist[i]))
