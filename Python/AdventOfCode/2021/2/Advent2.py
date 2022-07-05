import re
file=open("dive.txt","r")
z=file.read()
adminlist=z.splitlines()
x=0
y=0
i=0
while i<len(adminlist):
    txt=adminlist[i]
    z=re.findall(r'\d+', txt)
    num=int(z[0])
    if 'forward' in txt:
        x+=num
    if 'up' in txt:
        y-=num
    if 'down' in txt:
        y+=num
    i+=1
print(x*y)
    

