class VIN:
    
    #Constructor
    def __init__(self,vin):
        
        if len(vin)!=17:
            print(f"Invalid vin: {vin} length")
            return vin
        for c in vin:
            if c in "IOQ":
                print(f"Invalid vin: {vin} IDQ")
                return vin
        #WMI = First 3 Characters
        self.wmi=vin[0:3]
        #VDS = second 6 with Last being the Check sum
        self.vds=vin[3:9]
        #SER = last 8
        self.ser=vin[9:]
            
    #toString
    def __str__(self):
        return self.wmi+self.vds+self.ser