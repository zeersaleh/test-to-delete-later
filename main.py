myBill = float(input("What was the bill?:"))
numberOfPeople = int(input("How many people?:"))
tip = int (input("Waht percent tip you want to leave: 15,18, or 20 percent?"))

billWithTip= tip/100 * myBill + myBill
billPerPerson = billWithTip/numberOfPeople
finalAmount = round(billPerPerson,2)
print("You all owe", finalAmount)
