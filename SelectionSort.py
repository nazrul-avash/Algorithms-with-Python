def sort_by_selection():
	
	index = 0
	for x in range(len(li)):
		smallest = li[x]
		for y in range(x,len(li)):
			if li[y] < smallest:
				smallest = li[y]
				index = y
		if(smallest < li[x]):
			temp = li[x]
			li[x] = li[index]
			li[index] = temp

li = [4,-78,693,1,5,975662,145,-8799645]		
sort_by_selection()
print(li)
