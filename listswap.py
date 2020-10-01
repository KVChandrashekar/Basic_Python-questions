def swaplist(newList):
	size = len(newList)

	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp

	return newList


newList = [12,32,43,63,43]
 
print(swaplist(newList))