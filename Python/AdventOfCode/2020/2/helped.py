#file=open("input.txt","r")
#z=file.read()
#adminlist=z.splitlines()
#file.close()
#i=0
#while i<len(adminlist):
#    x=adminlist[i]
#    z=x.split('-',1)
#    y=z[1]
#    p=y.split(':',1)
#    john=p[0]
#    bleh=john.split(' ', 1)
#    file=open("inputletter.txt","a")
#    file.write(bleh[1]+'\n')
#    i+=1
#file.close()
class Do:
    def do():
        file=open("inputfirst.txt","r")
        z=file.read()
        first=z.splitlines()
        file.close()
        file=open("inputsecond.txt","r")
        z=file.read()
        second=z.splitlines()
        file.close()
        file=open("inputletters.txt","r")
        z=file.read()
        letters=z.splitlines()
        file.close()
        file=open("inputletter.txt","r")
        z=file.read()
        letter=z.splitlines()
        file.close()
        return first,second,letters,letter
Do.do()