# 4. 




#3. Magic Index - Find Index In Sorted Array Such That A[i] = i.
def magic_index(arr):
	count = 0
	n = len(arr)
	for i in range(n):
		if i == arr[i]:
			return i
arr = [1,2,2,3,4]		
# print(magic_index(arr))

#2.Find an Element in 2 dimensional sorted array
def find_in_2d(arr2d,element):
	if element > arr2d[-1][-1]:  # element is greater then the last element of our sorted arry
		return False
	Row = len(arr2d)
	Col = len(arr2d[0])
	for x in range(Row):
		if element <= arr2d[x][-1]:  # check for last element of the row
			for y in range(Col):
				if arr2d[x][y] == element:
					return True
			return False
	return False

arr2d = [
          [1,10,12],
          [22,32,91]
]
row = len(arr2d)
col = len(arr2d[0])
col_last = arr2d[1][-1]
# print(row,col)
# print(col_last)
# if find_in_2d(arr2d,91):
# 	print('Found')
# else:
# 	print('Not found')



#1.Find a Number occurring odd number of times in a Given array
def odd_times(arr):
	count = 1
	stack = []
	n = len(arr)
	visited = [0] * n
	for i in range(n):
		if not visited[i]:
			for j in range(i+1,n):
				visited[i] = 1
				if arr[i] == arr[j]:
					visited[j] = 1
					count += 1
			if count%2 == 1:
				stack.append(arr[i])
			count = 1
	return stack				
arr = [2,2,4,5,1,1,2,3,3,3,4]
# print(odd_times(arr))