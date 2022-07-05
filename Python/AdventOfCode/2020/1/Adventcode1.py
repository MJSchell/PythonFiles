file=open("num.txt","r")
z=file.read()
adminlist=z.splitlines()
file.close()
i=0
a=0
b=0
while i<len(adminlist)-1:
    if int(adminlist[i])+int(adminlist[a])+int(adminlist[b])==2020:
        print(adminlist[i],adminlist[a],adminlist[b])
    if b==len(adminlist)-1:
        a+=1
        b=0
    if a==len(adminlist)-1:
        i+=1
        a=0
    b+=1