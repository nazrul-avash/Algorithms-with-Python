# def countdown(n):
# 	if n == 0:
# 		print(n)
# 		return
# 	else:
# 		print(n)
# 		return countdown(n-1)
# countdown(15)			
# li = [4,5,6]
# li2 = [x for x in li if x >=5]
# print(li2)
def is_power(number):
	return (number & (number-1)) == 1
print(is_power(8))	