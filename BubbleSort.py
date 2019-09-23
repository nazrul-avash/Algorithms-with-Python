def sort_by_bubble(values):
	for i in range(len(values)-1):
		for j in range(len(values)-i-1):
			if values[j]>values[j+1]:
				values[j],values[j+1] = values[j+1],values[j]
values= [7,2,88,1,9,5]
sort_by_bubble(values)
print(values)				