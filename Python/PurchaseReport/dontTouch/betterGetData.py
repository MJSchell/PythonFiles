import pandas
import matplotlib.pyplot as plt

mockData = pandas.read_csv("./MOCK_DATA.csv")

dic = {}
companies = mockData["company"]
amount = mockData["cost"]

unq = mockData.company.unique()
unq.sort()
for i in unq:
    dic[i] = 0

for i in range(len(companies)):
    dic[companies[i]] = dic[companies[i]] + amount[i]

total = 0
for i in dic:
    total+=dic[i]

print(dic)
#https://pythonguides.com/python-format-number-with-commas/
print("\nTotal:","{:,}".format(round(total)))

keyList = list(sorted(dic.values()))

neededKeys1 = []
neededKeys2 = []
for i in range(len(keyList)):
    if i < 20:
        for j in dic:
            if dic[j] == keyList[i]:
                neededKeys1.append([j, dic[j]])
    elif(i > len(keyList)-20):
        for j in dic:
            if dic[j] == keyList[i]:
                neededKeys2.append([j, dic[j]])

for i in neededKeys1:
    plt.xticks(rotation = 90)
    plt.bar(i[0],i[1])
plt.show()
for i in neededKeys2:
    plt.xticks(rotation = 90)
    plt.bar(i[0],i[1])
plt.show()