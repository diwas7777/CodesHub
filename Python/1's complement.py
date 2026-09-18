#User input
mainValue = (input("Enter main value ->"))
secondValue = (input("Enter second value ->"))

print("making equal number of digits")
while len(mainValue) != len(secondValue): #makes equal number of digits
    if len(mainValue) < len(secondValue): #adds 0 to main value
        mainValue = "0" + mainValue

    else:                                   #adds 0 to the second value
        secondValue = "0" + secondValue

print ("main value -> " + mainValue)
print ("second value -> " + secondValue + "\n")


#Finding 1's complement

print("finding 1's complement of second value")
firstList = list(secondValue)
i = 0
newSecondValue = ""
while i<len(firstList):
    convertedValue = 1 - int(firstList[i])
    if newSecondValue == "":
        newSecondValue = str(convertedValue)
    else:
        newSecondValue = newSecondValue + str(convertedValue)
    i+=1
print ("-> " + newSecondValue + "\n")


# Converting values to binary and finding the sum
try:
    sumBinary = bin(int(newSecondValue, 2) + int(mainValue, 2))

except ValueError:
    print("Error: Your main value is not a binary number, please write a new value")

else:
    print("Adding main value to the complement value")

    additionResult = sumBinary[2:]
    print (newSecondValue + "+" + mainValue +"-> " + additionResult )
    i = 0
    secondList = list(additionResult)
    while len(mainValue) > len(additionResult):
        additionResult = "0" + additionResult

    if len(mainValue) != len(additionResult):
        print ("overflow occured so removing overflow digit and adding it to remaining value")
        remainingValue = ""
        while i<len(secondList):
            if i == 0:
                overflowDigit = secondList[i]
            elif remainingValue == "":
                remainingValue = secondList[i]
            else:
                remainingValue = remainingValue + secondList[i]
            i+=1

        sumBinary =  bin(int(remainingValue, 2) + int(overflowDigit, 2))
        result = sumBinary[2:]
        print(mainValue + " - " + secondValue + " = " + result)

    else:
        print("finding 1's complement of second value")
        thirdList = list(additionResult)
        i = 0
        result = ""
        while (i<len(thirdList)):
            convertedValue = 1 - int(thirdList[i])
            if result == "":
                result = str(convertedValue)
            else:
                result = result + str(convertedValue)
            i+=1
        print(mainValue + " - " + secondValue + " = -" + result)


