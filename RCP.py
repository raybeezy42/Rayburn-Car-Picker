#!/usr/bin/python

class Vehicle:
    def __init__(self,make,model,color,fuelType,options):
        self.make=make
        self.model=model
        self.color=color
        self.fuelType=fuelType
        self.options=options

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getColor(self):
        return self.color
    def getFuelType(self):
        return self.fuelType
    def getOptions(self):
        return self.options

class Car(Vehicle):

    def __init__(self,make,model,color,fuelType,options,engineSize,numDoors):
        Vehicle.__init__(self,make,model,color,fuelType,options)
        self.engineSize=engineSize
        self.numDoors=numDoors

    def getEngineSize(self):
        return self.engineSize
    def numDoors(Self):
        return self.numDoors

    def printDetails(self):
        print("Car Make : ",self.make)
        print("Car Model : ",self.model)
        print("Car Color : ",self.color)
        print("Fuel Type : ",self.fuelType)
        print("Options : ",self.options)
        print("Engine Size : ",self.engineSize)
        print("Number of Doors :",self.numDoors)

class Pickup(Vehicle):

    def __init__(self,make,model,color,fuelType,options,cabStyle,bedLength):
        Vehicle.__init__(self,make,model,color,fuelType,options)
        self.cabStyle=cabStyle
        self.bedLength=bedLength

    def getCabStyle(self):
        return self.cabStyle
    def getBedLength(self):
        return self.bedLength

    def printDetails(self):
        print("Pickup Make : ",self.make)
        print("Pickup Model : ",self.model)
        print("Pickup Color : ",self.color)
        print("Fuel Type : ",self.fuelType)
        print("Options : ",self.options)
        print("Cab Style : ",self.cabStyle)
        print("Bed Length :",self.bedLength)
  
garage=[]
while(True):
    option = int(input("Enter \n1 For a Car \n2 For a Pickup \n3 to exit \n"))
    if(option==1):
        make=input("Enter Car Make : ")
        model=input("Enter Car Model : ")
        color=input("Enter Car Color : ")
        fuelType=input("Enter Fuel type : ")
        options=input("Enter Car Option : ")
        engineSize=int(input("Enter Engine Size : "))
        numDoors=int(input("Enter Number of Doors : "))
        p=Car(make,model,color,fuelType,options,engineSize,numDoors)
        garage.append(p)
    elif(option==2):
        make=input("Enter Pickup Make : ")
        model=input("Enter Pickup Model : ")
        color=input("Enter Pickup Color : ")
        fuelType=input("Enter Fuel type : ")
        options=input("Enter Pickup Option : ")
        cabStyle=input("Enter Cab Style : ")
        bedLength=int(input("Enter Bed length : "))
        t=Pickup(make,model,color,fuelType,options,cabStyle,bedLength)
        garage.append(t)
    else:
        break

print("The details for your vehicles are :")
for v in garage:
    print(v.printDetails())
