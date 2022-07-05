
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('elec_access_data.csv',header=0)

#which countries we want to look at
OurCountries=["Russia","Spain","Poland","Romania","Netherlands","Kosovo","Luxembourg","Belgium","Liechtenstein","Monaco","Moldova","Ireleand","Malta","Austria","Belarus","United Kingdom","Denmark","Switzerland","Finland","Greece","Hungary","Sweden","Norway","San Marino","Ukraine","Germany","Italy","France","Slovenia","Estonia"]
for z in range(len(OurCountries)):
    country1=OurCountries[z]
    for i in range(len(OurCountries)):
        country=OurCountries[i]
        if country1==country:
            print(country)
        
print(len(OurCountries))

#find unique countries
UniqueContries=df.Entity.unique()


#graph the our countries
#go find each of our countries i nthe unique countries
for c in UniqueContries:
    if c in OurCountries:
    #grab the data of that paticular country
        #x axis
        years= df[df["Entity"]==c]['Year']
        #y axis
        elecAccess=df[df["Entity"]==c]['Access']
        #if the entity column is equal our country, make dataframe of the access
        
        #since we are putting multiple countries in one graph
        #plot out graph
        plt.plot(years,elecAccess,label=c)
plt.ylabel("% of Country Population")
plt.xlabel("Years")
plt.legend()
plt.title("% of Population of Population with Electricty Access")
plt.show()