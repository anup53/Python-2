i=input("Enter your file name") 
	f=open(i,'r')
	data=f.read()
	print(data)
	f.close()