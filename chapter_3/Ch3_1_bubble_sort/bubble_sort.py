import random

def bubble_sort(arr):
	compare_count = 0
	lenOfArr = len(arr)
	for i in range(0,len(arr)-1):
		for j in range(0,len(arr)-1):
			if(j==len(arr)-1):
				break
			else:
				compare_count = compare_count+1
				cur = arr[j]
				next = arr[j+1]
				if(cur > next):
					arr[j] = next
					arr[j+1] = cur
					
	print("Length of the Array: %d"%lenOfArr)
	print("Compare time: %d"%compare_count)
	print("Result:")
	print(arr)
				

if __name__=="__main__":
	my_input = input("Please enter the number of random element: ")
	try:
		my_input = int(my_input)
		my_arr = []
		for i in range(0,my_input):
			my_arr.append(random.randint(0,my_input))
		bubble_sort(my_arr)
	except:
		print(sys.exc_info()[0])