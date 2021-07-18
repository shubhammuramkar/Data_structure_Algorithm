# #Q4. Find Max and Min element in single pass (single traversal of array) 
def min_max_element(arr):
    if not arr:
        return
    min_ = arr[0]
    max_ = arr[0]
    
    for i in arr[1:]:
        if min_ > i:
            min_ = i
        if max_ < i:
            max_ = i
    return min_, max_
  
#Q3. Find the min element in the array
def min_element(arr):
    if not arr:
        return
    min_ = arr[0]
    for i in arr[1:]:
        if min_ > i:
            min_ = i
    return min_
  
#Q2. Find the max element in the array
def max_element(arr):
    if not arr:
        return
    max_ = arr[0]
    for i in arr[1:]:
        if i > max_:
            max_ = i
    return max_

# Q1. Given an array, print all the elements in the array. where array can be if any size  
def array_travel(arr):
    if not arr:
        return
    for element in arr:
        print(element)
