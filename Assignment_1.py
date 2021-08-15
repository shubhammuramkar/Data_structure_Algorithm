## Doubts
 # 7. 122. Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/  - Not able to solve

#15 48. Rotate Image - https://leetcode.com/problems/rotate-image/ - not able to solve without using extra space


# 1. Two Sum - https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        d = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in d:
                return [d[rem],i] 
            else:
                d[nums[i]] = i


# 2. 167. Two Sum II - Input array is sorted  - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        last = size-1
        first = 0
        
        ## 2pointer approach
        for i in range(size):
            sum_ = numbers[first] + numbers[last]
            if sum_ == target:
                return [first+1,last+1]
            elif sum_ > target:
                last -= 1
            else:
                first += 1
            
        
# 3. 88. Merge Sorted Array - https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            nums1
        else:
            j = 0
            for i in range(m,len(nums1)):
                    nums1[i] = nums2[j]
                    j += 1
            nums1.sort()


 # 4. 118. Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/
 class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1],[1,1]]
        for i in range(numRows-2):
            last_l = len(result[-1])-1
            inner = [1]
            for j in range(last_l):
                inner.append(result[-1][j]+result[-1][j+1])
            inner.append(1)
            result.append(inner)
        return result
                
# 5. 119. Pascal's Triangle II - https://leetcode.com/problems/pascals-triangle-ii/        
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        result = [[1],[1,1]]
        for i in range(rowIndex-1):
            inner = [1]
            last_l = len(result[-1])-1
            for j in range(last_l):
                inner.append(result[-1][j]+result[-1][j+1])
            inner.append(1)
            result.append(inner)
        return result[-1]
            
 #6. 121. Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_l = [0]*n
        max_l[-1] = prices[-1]
        profit = 0
        ## Finding the maximun from the right and storing in max_l
        for i in range(n-2,-1,-1):
            if prices[i] > max_l[i+1]:
                max_l[i] = prices[i]
            else:
                max_l[i] = max_l[i+1]
        
        # if buy is less then max_l till that next value 
        for i in range(n-1):
            buy = prices[i]
            sell = max_l[i+1]
            if sell > buy:
                profit = max(sell - buy,profit)
        return profit

#============================================================

# 7. 122. Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Not able to solve

#============================================================

# 8. 169. Majority Element - https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        ## finding the ceil value of n/2
        if size == 1:
            return nums[0]
        elif size%2 == 0:
            n = int(size/2)
        else:
            n = int(size/2)+1   
        ## dict_ store the value count of each number if exceed n/2 we return the ans.
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
                if dict_[i] >= n:
                    return i

# 9. 229. Majority Element II - https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = []
        if size == 1:
            return nums
        n = int(size/3)
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for key,value in dict_.items():
            if value > n:
                result.append(key)
        return result


#============================================================
# 10. https://leetcode.com/problems/missing-ranges/ - premium Question
#============================================================


#11. 15. 3Sum- https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.using2pointer(nums)
    
    # 2 pointer approach - optimal
    def using2pointer(self,nums):
        n = len(nums)
        if n == 0 or n ==1:
            return []
        result = [] # for result
        added = set() # to avoid duplicated 3 sum
        nums.sort() # to apply 2 pointer method 
        for i in range(n-1,-1,-1):
            last = nums[i]
            start,end = 0,i-1
            while start < end:
                a,b,c = last,nums[start],nums[end]
                s = a+b+c
                if s == 0:
                    if (a,b,c) not in added:
                        result.append([a,b,c])
                        added.add((a,b,c))
                     # start += 1  ##  we can use start +=1 or end-=1 just to continue the while loop else it goes to infinite loop
                    end -= 1
                elif s > 0:
                    end -= 1
                else:
                    start += 1
        return result

#============================================================
#12. https://leetcode.com/problems/3sum-smaller/  -premium Question
#============================================================


#13. 16. 3Sum Closest - https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prev = 999999999
        nums.sort()
        result = 0
        for i in range(n-1,-1,-1):
            last  = nums[i]
            start = 0
            end = i-1
            while start < end:
                pair = last + nums[start] + nums[end]
                value = abs(pair - target)
                print(last , nums[start] , nums[end],pair,value)
                if value < prev:
                    prev = value
                    result = pair
                    print('res',result)
                if pair < target :
                    start+=1
                elif pair > target:
                    end -= 1
                else:
                    result = pair
                    break
        return result
                    
        
#14. 18. 4Sum - https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        added = set()
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n-1,-1,-1):
            last = nums[i]
            for j in range(i-1,-1,-1):
                last_2 = nums[j]
                start = 0
                end = j-1
                while start < end:
                    pair = last + last_2 + nums[start] + nums[end]
                    if pair == target:
                        if (last,last_2,nums[start],nums[end]) not in added:
                            result.append([last,last_2,nums[start],nums[end]])
                            added.add((last,last_2,nums[start],nums[end]))
                        start += 1
                    elif pair < target:
                        start += 1
                    else:
                        end -= 1
        return result


#15 48. Rotate Image - https://leetcode.com/problems/rotate-image/ - not able to solve without using extra space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = 0
        result = []
        n = len(matrix)
        if n == 1:
            return matrix
        for j in range(n):
            pair = []
            for i in range(n-1,-1,-1):
                pair.append(matrix[i][x])
            x += 1
            result.append(pair)
        print(result)




