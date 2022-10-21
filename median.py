"""Median calculator."""
def calcMedian(numList):
    numList.sort()

    if (len(numList) % 2) == 1:
        return numList[len(numList)//2]
    else:
        return (numList[len(numList)//2 - 1] + numList[len(numList)//2]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
