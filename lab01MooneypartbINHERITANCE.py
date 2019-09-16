#Brett Mooney
class Vehicle:
    def __init__(self, modelID, FCC, FCM):
        self.modelIdentification = modelID
        self.fuelCapCurr = FCC
        self.fuelCapMax = FCM
    def printVehicleInfo(self):
        print("ModelID: " + self.modelIdentification)
        print("Fuel: " + str(self.fuelCapCurr) + "/" + str(self.fuelCapMax))

class CommercialVehicle(Vehicle):
    def __init__(self, modelID, FCC, FCM, dname):
        super().__init__(modelID, FCC, FCM)
        self.driverName = dname
    def getDriverName(self):
        return self.driverName

class UtilityVehicle(Vehicle):
    def __init__(self, modelID, FCC, FCM, vType):
        super().__init__(modelID, FCC, FCM)
        self.vehicleType = vType
    def getVehicleType(self):
        return self.vehicleType





x = Vehicle("fedex0001", 100, 200)
x.printVehicleInfo()

y = CommercialVehicle("walmart0041", 100, 200, "Gregg")
y.printVehicleInfo()
print(y.getDriverName())

z = UtilityVehicle("wegmans0066", 20, 50, "forklift")
z.printVehicleInfo()
print(z.getVehicleType())
