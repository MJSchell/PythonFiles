#import matplotlib.pyplot as plt
import pandas

mockData = pandas.read_csv("./MOCK_DATA.csv")["state"].to_list()
dic = {}
#https://moonbooks.org/Articles/How-to-create-a-list-of-US-states-in-python-/
us_states = ['District of Columbia','Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#https://stackabuse.com/python-how-to-add-keys-to-dictionary/
for i in us_states:
    dic[i] = 0

for i in mockData:
    dic[i] = dic[i] + 1

print(dic)
for i in dic:
    if dic[i] == 0:
        print(i)