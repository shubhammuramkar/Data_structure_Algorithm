#1.  283. Move Zeroes - https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 0:
            for i in range(len(nums)):
                for j in range(i,len(nums)):
                    if nums[i] == 0 and nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
#2. 217. Contains Duplicate  - https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Approach 1
        n = len(nums)
        unique = len(set(nums))
        if n == unique:
            return False
        else:
            return True
        
#         ## Approach 2
#         n = len(nums)
#         dict_ = {}
#         for i in range(n):
#             if nums[i] not in dict_:
#                 dict_[nums[i]] = 1
#             else:
#                 dict_[nums[i]] += 1
        
#         l = len(dict_)
#         if n == l:
#             return False
#         else:
#             return True

#3. 219. Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii/ - TIme limit exceed
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n-1,-1,-1):
            start = 0
            while start < i:
                if nums[start] == nums[i] and abs(i-start) <= k:
                    print(nums)
                    print(start,i,nums[i])
                    return True
                else:
                    start += 1
        return False

 #4. 228. Summary Ranges - https://leetcode.com/problems/summary-ranges/
 class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        result = []
        x = 0
        count = 0
        while True:
            if nums[x] == nums[-1]:
                result.append(str(nums[x]))
                return result
            start = x 
            next_ = x+1 
            while nums[x] + 1 == nums[next_]:
                x = next_
                next_ = next_ + 1
                count += 1
                if next_ == n:
                    break   
            if count > 0:
                length = str(nums[start])+'->'+str(nums[x])
            else:
                length = str(nums[start])                
            result.append(length)
            if next_ == n:
                return result
            x = next_
            count = 0
                
                
            
#5. 303. Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
        


#6 - 304. Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/  - TIme limit exceed
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix  = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1,row2+1):
            for col in range(col1,col2+1):
                ans += self.matrix[row][col]
        return ans  
        

#7. 27. Remove Element - https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        
        
        for i in nums:
            if i == val:
                count += 1
                
        for i in range(n-1):
            if nums[i] == val:
                for j in range(i+1,n):
                    if nums[j] != val:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        rem = n - count
        for i in nums[rem:]:
            i = '_'
            
        return rem
            
 #8. 349. Intersection of Two Arrays - 	https://leetcode.com/problems/intersection-of-two-arrays/submissions/
 class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        nums_1 = []
        nums_2 = []
        result = []
        for i in range(n1):
            if nums1[i] not in nums_1:
                nums_1.append(nums1[i])
        for j in range(n2):
            if nums2[j] not in nums_2:
                nums_2.append(nums2[j])
                
        for i in nums_1:
            for j in nums_2:
                if i == j:
                    result.append(i)
        return result

 #9.  350. Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/
 class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        final = {}
        for i in nums1:
            if i not in final:
                final[i] = 1
            else:
                final[i] += 1
        
        for j in nums2:
            if j in final:
                if final[j] > 1:
                    final[j] -= 1
                else:
                    del final[j]
                result.append(j)
        return result
        
 # 10. 496. Next Greater Element I - https://leetcode.com/problems/next-greater-element-i/
 class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        great = [0]*n
        great[-1] = -1
        x = 0
        result = []
        for i in range(n-1):
            flag = 1
            for j in range(i+1,n):
                if nums2[i] < nums2[j]:
                    great[i] = nums2[j]
                    flag = 0
                    break
            if flag:
                great[i] = -1                
        print(nums2,great)       
        for i in nums1:
            for j in range(n):
                if i == nums2[j]:
                    result.append(great[j])
        return result
            
            
 #11. 503. Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/
 class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(1,2*n):  # to for the circular
            i %= n   # help in circular travel
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                result[ind] = nums[i]
            stack.append(i)
        return result

        
#12. 556. Next Greater Element III - https://leetcode.com/problems/next-greater-element-iii/
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        index = len(digits) - 1
        print(digits,index)
        while index - 1 >= 0 and digits[index] <= digits[index - 1]:
            index -= 1			
        if index == 0:
            return -1

        greater = index

        while greater + 1 < len(digits) and digits[greater + 1] > digits [index - 1]:
            greater += 1

        digits[greater], digits[index - 1] = digits[index - 1], digits[greater]
        digits[index :] = digits[index :][::-1]

        digits = int("".join(digits))

        return digits if digits < 1 << 31 else -1                


#13. 1366. Rank Teams by Votes https://leetcode.com/problems/rank-teams-by-votes/
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for x in votes:
            for i in range(len(x)):
                if x[i] not in d:
                    d[x[i]] = [0]*len(x)
                d[x[i]][i] += 1
        l = sorted(list(d.keys())) # sort the team alphabetically first       
        ans = sorted(l, key = lambda x: d[x], reverse = True) # then sort it based on votes
        return "".join(ans)
   
        
#14. 1338. Reduce Array Size to The Half - https://leetcode.com/problems/reduce-array-size-to-the-half/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hmap={}
        n=len(arr)
        ans=0
        for i in range(len(arr)):
            if arr[i] not in hmap:
                hmap[arr[i]]=1
            else:
                hmap[arr[i]]+=1
        v1=sorted(hmap.values(),reverse=True)
        temp,i=n,0
        while i<len(v1) and temp>n/2:
            temp-=v1[i]
            i+=1
            ans+=1
        return ans       



# Doubts - 

# Array class 3 - 
# 307. Range Sum Query - Mutable 
# https://leetcode.com/problems/range-sum-query-mutable/
# Time limit exceed

# 957. Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/
# For n = 1000000
# Time limit exceed

# Assignment 1
# Q 7 and 15

# Assignment 2
# 219. Contains Duplicate II 
# https://leetcode.com/problems/contains-duplicate-ii/
# Time limit exceed

# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# Time limit exceed

# 556. Next Greater Element III -
#  https://leetcode.com/problems/next-greater-element-iii/ 

# 13. 1366. Rank Teams by Votes 
# https://leetcode.com/problems/rank-teams-by-votes/

# #14. 1338. Reduce Array Size to The Half -
#  https://leetcode.com/problems/reduce-array-size-to-the-half/
