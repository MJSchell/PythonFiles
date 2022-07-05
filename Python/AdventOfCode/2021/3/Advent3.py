file=open("binary.txt","r")
z=file.read()
adminlist=z.splitlines()
i=0
a=0
b=0
while i<len(adminlist):
    z=int(adminlist[i])
    if z==1:
        a+=1
    if z==0:
        b+=1
    i+=1
print('1:',a,'0:',b)
#011101001101 = 1869
#100010110010 = 226