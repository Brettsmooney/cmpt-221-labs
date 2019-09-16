#Brett Mooney
import math

def printFunction(totalCost, totalPayment, changeQuarters, changeDimes, changeNickles, changePennies, totalNumCoins, changeValue):
    print("Total cost of items: " + str(totalCost))
    print("Total money given:: " + str(totalPayment))
    print("Your change is as follows: ")
    print("Quarters: " + str(math.floor(changeQuarters)))
    print("Dimes: " + str(math.floor(changeDimes)))
    print("Nickles: " + str(math.floor(changeNickles)))
    print("Pennies: " + str(math.floor(changePennies)))
    print("Total number of coins: " + str(totalNumCoins))
    print("Total value of change: " + str(math.floor(changeValue)))


changeQuarters = 0
changeDimes = 0
changeNickles = 0
changePennies = 0
totalNumCoins = 0

totalCost = 0.00
totalPayment = 0.00
totalChange = 0

programRunning = 1

while programRunning == 1:
  itemCostInputRunning = 1
  paymentInputRunning = 1
  transactionRunning = 1
  restartLoop = 1
  while itemCostInputRunning == 1:
    print("Total Cost of Items: ")#request transaction
    totalCost = input()

    try:
      totalCost = float(totalCost)
      if float(totalCost) <= 0.00 :
        print("Cost must have a value greater than zero!")
      elif float(totalCost) > 0.00 :
        itemCostInputRunning = 0
        totalCost = float(totalCost)
      else:
        print("Invalid input.")
    except:
      print("Invalid Input")

  while transactionRunning == 1:
    while paymentInputRunning == 1:
      print("Total amount of money given: ")#request payment
      totalPayment = input()

      try:
        totalPayment = float(totalPayment)
        if float(totalPayment) < totalCost :
          print("Payment must be greater than cost!")
        elif float(totalPayment) == totalCost :
          print("No change, Transaction complete")
          transactionRunning = 0 #escape while loop
          paymentInputRunning = 0
        else:
          transactionRunning = 0 #escape while loop
          paymentInputRunning = 0
          totalChange = totalPayment - totalCost #calculate change
          changeValue = totalChange

          #Calculate change data
          #at this point totalChange should be positive (example change: 4,89$)
          totalChange = totalChange*100     #(4,89 -- 489 = totalChange)
          changeQuarters = totalChange / 25 #(489 / 25 = 19 = changeQuarters)
          totalChange = totalChange % 25    #(489 % 25 = 14 = totalChange)
          changeDimes = totalChange / 10    #(14 / 10 = 1 = changeDimes)
          totalChange = totalChange % 10    #(14 % 10 = 4 = totalChange)
          changeNickles = totalChange / 5   #(4 / 5 = 0 = changeNickles)
          totalChange = totalChange % 5     #(4 % 5 = 4 = totalChange)
          changePennies = totalChange       #(4 / 1 = 4 = changePennies)

          totalNumCoins = math.floor(changeQuarters) + math.floor(changeDimes) + math.floor(changeNickles) + math.floor(changePennies)


          #Print output
          printFunction(totalCost, totalPayment, changeQuarters, changeDimes, changeNickles, changePennies, totalNumCoins, changeValue)


          while restartLoop == 1:
            print("Calculate another change value? [Y/n]: ")
            restart = input()

            if restart == "Y" or restart == "y" or restart == "yes" or restart == "Yes" or restart == "YEs" or restart == "YES" or restart == "yES" or restart == "yeS" or restart == "1" :
              restartLoop = 0
              print("Program will restart.")
            elif restart == "N" or restart == "n" or restart == "No" or restart == "NO" or restart == "nO" or restart == "no" or restart == "0" :
              programRunning = 0
              restartLoop = 0
              print("Program terminated.")
            else:
              print("Invalid Input")
      except:
        print("Invalid Input")
