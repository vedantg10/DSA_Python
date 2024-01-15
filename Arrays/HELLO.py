def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print (biggestNumber)


findBiggestNumber([1, 2, 4, 5 , 6, 9, 10, 13, 16, 54, 16])