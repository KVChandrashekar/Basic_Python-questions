#prime numbers in between given interval of numbers

start =int(input('enter start number:'))
end = int(input('enter the end number'))

for i in range(start,end):
    if i>1:
	    for j in range(2,i):
		    if(i % j==0):
			    break
	    else:
		    print(i)