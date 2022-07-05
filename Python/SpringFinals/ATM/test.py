import pandas
df=pandas.read_csv("atmData.csv")

class Construct:
    
    def __init__(self):
        self.pins=df["Pin"]
        self.savings=df["Savings"]
        self.checkings=df["Checkings"]
        return self