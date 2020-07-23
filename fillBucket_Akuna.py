def fillBucket(picture):
	height=len(picture)
	length=len(picture[0])
	fill_status=[[0 for i in range(length)] for j in range(height)]
	result=0
	for i in range(height):
		for j in range(length):
			if not fill_status[i][j]:
				fill(picture, i, j, fill_status, picture[i][j])
				result+=1
	return result

def fill(picture, i, j, fill_status, color):
	fill_status[i][j]=1
	#up
	for up in range(i-1,-1,-1):
		if (not fill_status[up][j]) and picture[up][j]==color:
			fill(picture, up,j,fill_status,color)
		else:
			break
	#down
	for down in range(i+1, len(fill_status)):
		if (not fill_status[down][j]) and picture[down][j]==color:
			fill(picture, down,j,fill_status,color)
		else:
			break
	#left
	for left in range(j-1, -1, -1):
		if (not fill_status[i][left]) and picture[i][left]==color:
			fill(picture, i,left,fill_status,color)
		else:
			break
	#right
	for right in range(j+1, len(picture[0])):
		if (not fill_status[i][right]) and picture[i][right]==color:
			fill(picture, i,right,fill_status,color)
		else:
			break
p=[["a", "a", "b"],["a", "a", "a"], ["a", "c", "a"], ["a", "a", "d"]]
print(fillBucket(p))
