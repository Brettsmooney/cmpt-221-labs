#Brett Mooney
import math
print("Total Cost of Items: ")#request transaction
totalCost = float(input())

changeQuarters = 0
changeDimes = 0
changeNickles = 0
changePennies = 0
totalNumCoins = 0
totalChange = 0

transactionRunning = 1
while transactionRunning == 1:

  print("Total amount of money given: ")#request payment
  totalPayment = float(input())

  totalChange = totalPayment - totalCost #calculate change

  if totalChange < 0: #negative number
    print("The transaction requires more payment to be completed")
  elif totalChange == 0:
    print("No change, Transaction complete")
    transactionRunning = 0 #escape while loop
  else:
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
    print("Total cost of items: " + str(totalCost))
    print("Total money given:: " + str(totalPayment))
    print("Your change is as follows: ")
    print("Quarters: " + str(math.floor(changeQuarters)))
    print("Dimes: " + str(math.floor(changeDimes)))
    print("Nickles: " + str(math.floor(changeNickles)))
    print("Pennies: " + str(math.floor(changePennies)))
    print("Total number of coins: " + str(totalNumCoins))
    print("Total value of change: " + str(math.floor(changeValue)))
    transactionRunning = 0 #escape while loop



#Calculate another change value? [Y/n]:
