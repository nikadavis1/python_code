"""
Nika Davis
1001552896
10/24/2019
"""

def main():
	file = open("input_RPN.txt",'r')
	
	equations=file.readlines()
	#print (equations)
	a=[]
	for eq in equations:
		eq_list=eq.split()
		for i in eq_list:
			if(i.isnumeric())==True:
				a.append(int(i))
			else:	
				re=Cal(a.pop(-2),a.pop(-1),i)
				a.append(re)
		
	print(a)
	file.close()
	
def Cal(a, b, c):
	
	if c == "+":
		return(a+b)
	elif c == "-":
		return(a-b)
	elif c == "*":
		return(a*b)
	elif c == "/":
		return(a/b)
	
	
	

main()

