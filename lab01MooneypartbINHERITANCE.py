#Brett Mooney
class Vehicle:
    def __init__(self, modelID, FCC, FCM, mileage, MPG):
        self.modelIdentification = modelID
        self.fuelCapCurr = FCC
        self.fuelCapMax = FCM
        self.currMilesDriven = mileage
        self.milesPerGallon = MPG

    def printVehicleInfo(self):
        print("ModelID: " + self.modelIdentification)
        print("Fuel: " + str(self.fuelCapCurr) + "/" + str(self.fuelCapMax))
        print("Mileage" + str(self.currMilesDriven))
        print("Miles Per Gallon: " + str(self.milesPerGallon))

    def getCurrFuel(self):
        return self.fuelCapCurr
    def setCurrFuel(self, newFuel):
        self.fuelCapCurr = newFuel

    def getVehicleMileage(self):
        return self.currMilesDriven
    def setVehicleMileage(self, newVM):
        self.currMilesDriven = newVM
    def addVehicleMileage(self, addMiles):
        self.VehicleMilage += addMiles

    def getVehicleMPG(self):
        return self.milesPerGallon
    def setVehicleMPG(self, newMPG):
        self.milesPerGallon = newMPG

    def drive(self, tripDistance):
        #distance travelled in miles / milespergallon to find number of gallons used
        #subtract number of gallons used from fuelCapCurr
        #AS LONG AS FUEL IN THE CAR IS MORE THAN FUEL BEING USED!!!
        if (tripDistance / self.milesPerGallon) < self.fuelCapCurr :
            self.fuelCapCurr -= (tripDistance / self.milesPerGallon)
            #add the miles driven to the odometer
            self.addVehicleMileage(tripDistance) #add miles to odometer
        else:
            print("Not enough fuel to complete the trip")



class CommercialVehicle(Vehicle):
    def __init__(self, modelID, FCC, FCM, mileage, MPG, dname):
        super().__init__(modelID, FCC, FCM, mileage, MPG)
        self.driverName = dname
    def getDriverName(self):
        return self.driverName
    def setDriverName(self, dname):
        self.driverName = dname

class UtilityVehicle(Vehicle):
    def __init__(self, modelID, FCC, FCM, mileage, MPG, vType):
        super().__init__(modelID, FCC, FCM, mileage, MPG)
        self.vehicleType = vType
    def getVehicleType(self):
        return self.vehicleType
    def setVehicleType(self, vtype):
        self.vehicleType = vtype

testVehicle = Vehicle("chewy000367", 200, 200, 10)
testVehicle.printVehicleInfo()



#x = Vehicle("fedex0001", 100, 200)
#x.printVehicleInfo()

#y = CommercialVehicle("walmart0041", 100, 200, "Gregg")
#y.printVehicleInfo()
#print(y.getDriverName())

#z = UtilityVehicle("wegmans0066", 20, 50, "forklift")
#z.printVehicleInfo()
#print(z.getVehicleType())
