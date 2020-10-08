def collatz_chain(n):
	a=[]
	while n!=1:
		a.append(n)
		if n%2==0:
			n=n//2
		else:
			n=3*n+1
	a.append(1)
	return a

def problem():
	max_l, max_n = 0, 0
	for n in range(1, 1000000):
		c=collatz_chain(n)
		l=len(c)
		if l>max_l:
			max_l=l
			max_n=n
	return max_n


	
		
		