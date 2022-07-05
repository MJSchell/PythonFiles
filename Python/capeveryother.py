s=input('String: ')
word=''
listy=[]
for i in range(len(s)):
    listy.append(s[i])
for i in range(len(listy)):
    if i%2==1:
        listy[i]=str.upper(listy[i])
    if i%2==0:
        listy[i]=str.lower(listy[i])
for i in range(len(listy)):
    word+=listy[i]
print(word)