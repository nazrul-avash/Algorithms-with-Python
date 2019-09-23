def quick_sort(values):
	if len(values)< 2:
		return values
	else:
		pivot = values[0]
		smaller = [x for x in values[1:] if x <= pivot]
		larger = [x for x in values[1:] if x> pivot]
		return 	quick_sort(smaller)+[pivot]+quick_sort(larger)
	return values
def make_partition(values):
	pivot = values[0]
	pivot_index =0
	larger_index = -1
	smaller_index = 0
	for x in range(len(values)):
		if values[x] < pivot and  x < pivot_index:
			values[x],values[pivot_index] =values[pivot_index],values[x] 
			smaller_index = pivot_index
			pivot_index = x	
			# if larger_index > 0:
			# 	values[pivot_index],values[larger_index] =values[larger_index],values[pivot_index]
			# 	pivot_index,larger_index = larger_index,pivot_index 
		elif values[x]> pivot and x< pivot_index:
			values[x],values[pivot_index] =values[pivot_index],values[x]
			larger_index = pivot_index
			pivot_index = x 	
	print(values)		
values=[7,2,88,1,9,5,8,3,4]
# print(quick_sort(values))
make_partition(values)
print(values)

