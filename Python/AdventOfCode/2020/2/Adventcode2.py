from helped import Do
first,second,letters,letter=Do.do()
num=0
valid=0
while num<len(first):
    a=0
    for letter[num] in letters[num]:
        a+=1
    if int(first[num])<= a <=int(second[num]):
        valid+=1
    num+=1
print(valid)