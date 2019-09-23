#Brett Mooney
import time

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
        print("Mileage: " + str(self.currMilesDriven))
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
        self.currMilesDriven += addMiles

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
            print("Trip Completed.")
            print(" ")
        else:
            print("Not enough fuel to complete the trip")
            print(" ")

    def refillTank(self):
        if self.fuelCapCurr != self.fuelCapMax:
            self.fuelCapCurr = self.fuelCapMax
            print("Tank has been filled!")
            print(" ")
        else:
            print("Tank is already full!")
            print(" ")

    #You can also use a float value: time.sleep(5) Delays for 5 seconds.
    def doADonut(self):
        if (self.fuelCapCurr != 0):
            self.fuelCapCurr -= 5.0
            time.sleep(1)
            print("*...rrrRRRRrrrr...*")
            time.sleep(1)
            print("*...rrrRRRRrrrr...*")
            time.sleep(.5)
            print("*...rrrRRRRRRRRSCREEEEEEEEEEEEEEEEEEEEEEEEEE...*")
            time.sleep(.5)
            print("*...EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE...*")
            time.sleep(1)
            print("that was fun!")
            time.sleep(1.5)
            print("")
        else :
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            print("Not enough fuel, Knievel, shoulda went with the Mercedes.")
            print("")


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

print("QA engineers keep out")
print("")
programRunning = 1
testVehicle = Vehicle("walmart001777", 200, 200, 50000, 10)
testVehicle.printVehicleInfo()
print("")

while programRunning == 1:
    print("Select an action by entering the number.")
    print("1.) -drive")
    print("2.) -refill tank")
    print("3.) -donuts")
    print("4.) -exit program")
    actionSelection = input()

    if actionSelection == "1":
        print("How many miles to drive?")
        milesToDrive = input()
        try:
            float(milesToDrive)
            testVehicle.drive(float(milesToDrive))
            testVehicle.printVehicleInfo()
        except:
            print("Invalid Input")
    elif actionSelection == "2":
        testVehicle.refillTank()
        testVehicle.printVehicleInfo()
    elif actionSelection == "3":
        testVehicle.doADonut()
        testVehicle.printVehicleInfo()
    elif actionSelection == "4":
        print("Program will shutdown.")
        programRunning = 0
    else :
        print("Invalid input.")

    print(" ")#spacing





#.  3   5

#x = Vehicle("fedex0001", 100, 200)
#x.printVehicleInfo()

#y = CommercialVehicle("walmart0041", 100, 200, "Gregg")
#y.printVehicleInfo()
#print(y.getDriverName())

#z = UtilityVehicle("wegmans0066", 20, 50, "forklift")
#z.printVehicleInfo()
#print(z.getVehicleType())
