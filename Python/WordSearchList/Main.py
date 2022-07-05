file=open("word.txt","r")
z=file.read()
adminlist=z.splitlines()
file.close()

listy=[]
for word in adminlist:
    listy.append(word[::-1])
    

print(len('ZPCHMEJHUYWOQPFLXUUXLOMDUWRUJVAEYSHGAWGIKXDVRNFU'))

