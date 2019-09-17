def SearchBinarily(number):
	low = 0
	high = len(li) -1
	while low <= high:
		mid = (low+ high)//2
		if number == li[mid]:
			return str(number)+" Found at index: "+ str(mid)
		elif number < li[mid]:
			high = mid -1
		elif number > li[mid]:
			low = mid + 1
	return str(number)+ " is not in the list."
li = [2,6,9,87,139,659]	
print(SearchBinarily(139))				