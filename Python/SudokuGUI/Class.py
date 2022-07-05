class Checker:

    #turning horizontal to vertical -- Uneeded
    def HtoV(file):
        z=0
        fileout=[]
        for i in range(len(file)):
            string=''
            for i in range(len(file)):
                string+=file[i][z]
            z+=1
            fileout.append(string)
        return fileout



    #checking function
    def checkthisout(tocheckfileH,horizontalcorrect):
        z=0
        wrong=[]
        section=0
        for i in range(len(horizontalcorrect)):
            for z in range(len(horizontalcorrect)):
                if z in range(0,3) and i in range(0,3):
                    section=1
                if z in range(3,6) and i in range(0,3):
                    section=2
                if z in range(6,9) and i in range(0,3):
                    section=3
                if z in range(0,3) and i in range(3,6):
                    section=4
                if z in range(3,6) and i in range(3,6):
                    section=5
                if z in range(6,9) and i in range(3,6):
                    section=6
                if z in range(0,3) and i in range(6,9):
                    section=7
                if z in range(3,6) and i in range(6,9):
                    section=8
                if z in range(6,9) and i in range(6,9):
                    section=9
                if not(tocheckfileH[i][z]==horizontalcorrect[i][z]):
                    string='\n\tSection '+str(section)+'\n\t(Horizontal) Row '+str(i+1)+' (Vertical) Collumn '+str(z+1)
                    wrong.append(string)
        return wrong
'''
import random
class Generate:
    
    def generate():
        puzzle=[]
        generations=1
        generateagainst=['1','2','3','4','5','6','7','8','9']
        for i in range(len(generateagainst)):
            delete=random.choice(generateagainst)
            string+=delete
            generateagainst.remove(delete)
        puzzle.append(string)
        for i in range(8):
            generateagainst=['1','2','3','4','5','6','7','8','9']
'''