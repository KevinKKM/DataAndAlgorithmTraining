#display the factorial sequnce, we keep the Big O only execute N times, which is O(N)
def factorial(n):
	result = 1
	for i in range(0,n+1):
		if(i!=0):
			result = result*i
		print("%s! = %s"%(str(i),str(result)))
	
#input the value
if __name__=='__main__':
	try:
		in_val = input("Please input the integer in order to calculate the factorial:\n")
		number = int(in_val)
		factorial(number)
	except:
		print("Please input the valid number")