import pandas as pd

file=open("EVV Weather Obs.txt","r")
z=file.read()
adminlist=z.splitlines()
file.close()
#print(adminlist[0])
stationlist=[]
namelist=[]
Yearlist=[]
Monthlist=[]
Daylist=[]
PRCPlist=[]
SNWDlist=[]
Snowlist=[]
TAVGlist=[]
TMAXlist=[]
TMINlist=[]
TOBSlist=[]
 
for i in range(2,len(adminlist)):
    station=adminlist[i][0:17]
    stationlist.append(station)
    name=adminlist[i][35:69]
    namelist.append(name)
    Year=adminlist[i][69:73]
    Yearlist.append(Year)
    Month=adminlist[i][73:75]
    Monthlist.append(Month)
    Day=adminlist[i][75:77]
    Daylist.append(Day)
    prcp=adminlist[i][78:85]
    PRCPlist.append(prcp)
    SNWD=adminlist[i][87:93]
    SNWDlist.append(SNWD)
    snow=adminlist[i][96:101]
    Snowlist.append(snow)
    TAVG=adminlist[i][105:112]
    TAVGlist.append(TAVG)
    TMAX=adminlist[i][114:118]
    TMAXlist.append(TMAX)
    TMIN=adminlist[i][122:128]
    TMINlist.append(TMIN)
    TOBS=adminlist[i][132:139]
    TOBSlist.append(TOBS)

dict={'Sation': stationlist, 'Station_Name': namelist, 'Year': Yearlist,'Month': Monthlist, "Day": Daylist, 'PRCP': PRCPlist, 'SNWD': SNWDlist, 'SNOW':Snowlist,'TAVG':TAVGlist,'TMAX':TMAXlist,'TMIN':TMINlist,'TOBS':TOBSlist}
df=pd.DataFrame(dict)

df.to_csv('WeatherData.csv')
