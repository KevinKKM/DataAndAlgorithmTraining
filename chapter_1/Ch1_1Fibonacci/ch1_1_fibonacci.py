import sys

#Recursion part
def fib(n):
	if(n==0):
		return 0
	if(n>2):
		return fib(n-2)+fib(n-1)
	else:
		return 1
		
#Main part, default value is 10, after the input, it will process the fib seq
def main():
	fib_seq = []
	number = 10
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