 #283. Move Zeroes
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
                                          
#1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return
        arr = sorted(arr)
        lis = []
        min_d = 10000
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                dif = abs(arr[i] - arr[j])
                if dif < min_d:
                    if dif == 0:
                        continue
                    min_d = min(dif,min_d)
        for i in arr:
            pair = []
            num2 = i + min_d
            print(min_d)
            if num2 in arr:
                pair.append(i)
                pair.append(num2)
                lis.append(pair)
        return lis
            

#888. Fair Candy Swap
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        pair = []
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                # swap
                temp = aliceSizes[i]
                aliceSizes[i] = bobSizes[j]
                bobSizes[j] = temp
                
                #checking
                if sum(aliceSizes) == sum(bobSizes):
                    pair.append(bobSizes[j])
                    pair.append(aliceSizes[i]) 
                    return pair
                
                # swap
                temp = bobSizes[j]
                bobSizes[j] = aliceSizes[i]
                aliceSizes[i] = temp

#169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        maj = 0
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for key,value in dict_.items():
            if n < dict_[key]:
                return key
                
        


#867. Transpose Matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        lis1 = []
        row = len(matrix) 
        col = len(matrix[0]) 
        for j in range(col):
            lis = []
            for i in range(row):
                lis.append(matrix[i][j])
            lis1.append(lis)
        return lis1

# 1550. Three Consecutive Odds
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        flag = 0
        for i in range(len(arr)):
            if arr[i]%2 == 1:
                flag += 1
                if flag == 3:
                    break
            else:
                flag = 0
        if flag == 3:
            return True
        else:
            return False
                
                


# 1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return
        arr = sorted(arr)
        lis = []
        min_d = 10000
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                dif = abs(arr[i] - arr[j])
                if dif < min_d:
                    if dif == 0:
                        continue
                    min_d = min(dif,min_d)
        for i in arr:
            pair = []
            num2 = i + min_d
            print(min_d)
            if num2 in arr:
                pair.append(i)
                pair.append(num2)
                lis.append(pair)
        return lis


# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = list(jewels)
        strone = list(stones)
        dict_ = {}
        for i in strone:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        val = 0
        for i in jew:
            for j in dict_.keys():
                if i == j:
                    val += dict_[j]
        return val

# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # ans = []
        # ans.append(nums[0])
        for i in range(1,len(nums)):
            sum_ = 0
            for j in range(i):
                sum_ =nums[j] + nums[i]
            nums[i] = sum_
        return nums

# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ = 0
        for i in accounts:
            sum_ = 0
            for j in i:
                sum_ = sum_ + j
            max_ = max(sum_,max_)
        return max_