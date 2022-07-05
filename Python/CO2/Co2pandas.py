import pandas as pd
import matplotlib.pyplot as plt
import math

co2Data = pd.read_csv("co2_data.csv",header=0)

#clean the data

#remove -99.99
co2Data["Average"]=co2Data["Average"].replace(-99.99,math.nan)  #Nan means not a number

#drop the nan
co2Data.dropna(subset=["Average"],inplace=True)




plt.plot(co2Data["decimal_year"],co2Data["Average"])
plt.ylabel("Average Co2")
plt.xlabel("Years")
plt.title("Average Co2 Over time")
plt.show()