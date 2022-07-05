file=open("vins.csv","r")
z=file.read()
adminlist=z.splitlines()
file.close()
index=0
for line in adminlist:
    index+=1
    if "O" in line or "I" in line or "Q" in line:
        print(index,line)