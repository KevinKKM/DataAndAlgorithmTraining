import sys

result_cache = [None]*100000
#Recursion part and DPA part
def fib(n):
	result = result_cache[n]
	
	if(result==None):
		if(n==0):
			return 0
		elif(n==1):
			return 1
		else:
			result = fib(n-2)+fib(n-1)
		result_cache[n] = result
	return result

		
#Main part, default value is 50, after the input, it will process the fib seq
def main():
	fib_seq = []
	number = 50
	try:
		arvg_num = len(sys.argv)
		#Check if you have input the number, otherwise it will process the default input
		if(arvg_num > 1):
			number = int(sys.argv[1])
		for i in range(0,number):
			fib_seq.append(str(fib(i)))
		output = ",".join(fib_seq)
		print("The fibonacci Polynomial of %d:\n%s"%(number,output))
	except:
		#in case...if you input some weird char.....
		print("please input the valid number")
		
#Init part
if __name__ == '__main__':
	main()