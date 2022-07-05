increased=0
i=0
file=open("my_file.txt","r")
z=file.read()
adminlist=z.splitlines()
file.close()
for i in range(len(adminlist)-1):
    if int(adminlist[i])<int(adminlist[i+1]):
        increased+=1
    i+=1
print(increased)