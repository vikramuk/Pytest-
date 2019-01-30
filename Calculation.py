def add(a,b):
	return a+b
	
def sub(a,b):
	return a-b 
	
def mul(a,b):
	return (a*b)

def div(a,b):
	try:
		return a/b
	except:
		return "error: EDIV"
		
if __name__=="__main__":
	print(add(2,5))
	print(sub(1,3))
	print(mul(1,3))
	print(div(1,0))
			
	

