
string=f'''0 0 0 0 0 0 0 0 7 
7 2 0 3 0 9 0 0 1 
0 0 8 7 0 5 0 6 0 
5 0 2 8 9 0 0 0 0 
0 4 0 5 0 1 0 9 0 
0 0 0 0 6 3 7 0 5 
0 3 0 9 0 6 1 0 0 
2 0 0 1 0 7 0 5 3 
9 0 0 0 0 0 0 0 0 
'''
string=string.replace("|", "")
string=string.replace(" ", "")
string=string.replace("-", "")
print(string)
"""
for i in range(9):
    print(i)

import random

def generate():
        puzzle=[]
        generateagainst=['1','2','3','4','5','6','7','8','9']
        for i in range(len(generateagainst)):
            delete=random.choice(generateagainst)
            string+=delete
            generateagainst.remove(delete)
        puzzle.append(string)
        for row in range(8):
            generateagainst=['1','2','3','4','5','6','7','8','9']
            for collumn in range(9):
                delete=random.choice(generateagainst)
                if delete==puzzle[row][collumn]:
                    'cont.'
"""