#Describe the coding approach towards drawing a series of concentric square boxes with alternating 0’s and 1’s, in a single loop/pass. 
#Example of a series of boxes generated with n=5 (dimension) below:
#[[1 1 1 1 1 1 1 1 1]
# [1 0 0 0 0 0 0 0 1]
# [1 0 1 1 1 1 1 0 1]
# [1 0 1 0 0 0 1 0 1]
# [1 0 1 0 1 0 1 0 1]
# [1 0 1 0 0 0 1 0 1]
# [1 0 1 1 1 1 1 0 1]
# [1 0 0 0 0 0 0 0 1]
# [1 1 1 1 1 1 1 1 1]]
 m=9
n=9
a=[[None]*n for i in range(m)]
#k is start of rows l is the start of columns
k=0
l=0
value=1
import numpy as np
while k<m and l<n:

	#Fill the first row
	for i in range(l, n):
		a[k][i]=value
	k+=1
	#Fill the last row
	for i in range(l, n):
		a[n-1][i] = value
	m-=1
	#Fill the last column
	for i in range(k, m):
		a[i][n-1]=value
	n-=1


	#Fill the first column
	for i in range(k, m):
		a[i][l]=value
	l+=1
	if value:
		value=0
	else:
		value=1
print(np.array(a))
