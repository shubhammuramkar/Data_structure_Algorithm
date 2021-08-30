#1. 1002. Find Common Characters - https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        check = list(words[0])
        for i in range(1,n):
            new = []
            for char in words[i]:
                if char in check:
                    new.append(char)
                    check.remove(char)
            check = new
        return check
                
#2. 414. Third Maximum Number - https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ## Approach 1
        numset = set(nums)
        if len(numset) <= 2:
            return max(nums)
        else:
            for i in range(2):
                numset = numset - {max(numset)} 
            return max(numset)

        ## Approach 2
        # n = len(nums)
        # stack = []
        # x = nums[0]
        # count = 0
        # for i in nums:
        #     if i not in stack:
        #         stack.append(i)
        #     else:
        #         continue
        # stack.sort()
        # if len(stack) > 2:
        #     return stack[-3]
        # else:
        #     return stack[-1]


#3. 448. Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ## Approach 1 without extra space
        n = len(nums)
        return list( set(range(1,n+1)) - set(nums))
        
        
        ## Approach 2 -  with extra space
        # nums = list(set(nums))
        # result = []
        # nums.sort()
        # x = 1
        # # for i in range(1,n+1):
        # #     if i not in nums:
        # #         result.append(i)
        # # return result
        # for i in range(1,n+1):
        #     if i != nums[i-x]:
        #         result.append(i)
        #         x += 1
        #     x = 1
        # return result


#4. 453. Minimum Moves to Equal Array Elements - https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # n = max(nums)
        # moves = 0
        # for i in nums:
        #     moves += abs(n-i)
        # return moves
        m = min(nums)
        step = 0
        for i in nums:
            step += abs(i-m)
        return step
    
#5. 455. Assign Cookies - https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        while len(s) != 0 and len(g) != 0:
            s_max = s[-1]  # we can take max but also have time limit problem
            g_max = g[-1]
            if s_max >= g_max:
                count += 1
                s.remove(s_max)
                g.remove(g_max)
            else:
                g.remove(g_max)
        return count 
            
#6. 697. Degree of an Array - https://leetcode.com/problems/degree-of-an-array/
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict_ = {}
        new_result = 999999
        n = len(nums)
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1    
        degree = 1
        values = []
        for key,val in dict_.items():
            if val > degree:
                degree = val
                
        for key,val in dict_.items():
            if val == degree:
                values.append(key)
                   
        for v in range(len(values)):
            update_key = values[v]
            for i in range(n):
                if nums[i] == update_key:
                    start = i
                    break
            for i in range(n-1,-1,-1):
                if nums[i] == update_key:
                    end = i
                    break
            result = end - start + 1
            if result < new_result :
                new_result = result                
        return new_result
        
 #7. 605. Can Place Flowers  - https://leetcode.com/problems/can-place-flowers/
 ## not able to optimize it further need help
 class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fl = len(flowerbed)
        if fl < 3:
            if n == 1 and flowerbed[0] == 0:
                return True
            elif n == 0 and flowerbed[0] == 1:
                return True
            elif n == 1 and flowerbed[0] == 1:
                return False
            elif n == 0 and flowerbed[0] == 0:
                return True
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0 and n>0:
                flowerbed[0] = 1
                n -= 1
                if n == 0:
                    return True
            if flowerbed[-1] == 0 and flowerbed[-2] == 0 and n>0:
                flowerbed[-1] = 1
                n -= 1
                if n == 0:
                    return True
            for i in range(1,fl-2):
                prev = flowerbed[i-1]
                curr = flowerbed[i]
                next = flowerbed[i+1]
                if prev == 0 and curr == 0 and next == 0 and n >0:
                    flowerbed[i-1] = 1
                    n -= 1
                elif prev == 1 and curr == 0 and next == 0 and n > 0:
                    if flowerbed[i+2] == 0:
                        flowerbed[i+1] = 1
                        n -= 1
                elif prev == 0 and curr == 0 and next == 1 and n > 0:
                    if flowerbed[i-2] == 0:
                        flowerbed[i-1] = 1
                        n -= 1
                if n == 0:
                    return True
            return False
                
 #8. 66. Plus One - https://leetcode.com/problems/plus-one/
 class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        result = []
        
        # Convertig into string
        for i in digits:
            stack.append(str(i))
            
        # making a number as a string '123'
        val = ''.join(stack)
        
        # converting into int and Plus 1
        plusOne = int(val) + 1
        
        # convert back to string of list
        val1 = list(str(plusOne))
        
        # converting string of list into int of list
        for i in val1:
            result.append(int(i))
            
        return result
        
#9. 136. Single Number - https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dict_ ={}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        
        for key, val in dict_.items():
            if val == 1:
                return key
 
 # 10. 137. Single Number II - https://leetcode.com/problems/single-number-ii/
 class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for key,val in dict_.items():
            if val == 1:
                return key

# 11. 260. Single Number III - https://leetcode.com/problems/single-number-iii/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict_ = {}
        result = []
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for key,val in dict_.items():
            if val == 1:
                result.append(key)
        return result


# 12.  43. Multiply Strings https://leetcode.com/problems/multiply-strings/ - 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ## Approach 2 
        carry1 = 1
        result = 0
        for i in num1[::-1]:  # in reverse order
            carry2 = 1
            for j in num2[::-1]:
                result += int(i)*int(j)*carry1*carry2
                carry2 *= 10
            carry1 *= 10
        return str(result)
        
        # ## Approach 1
        # ans1 = 0
        # for i in num1:
        #     ans1 = ans1*10 + ord(i) - 48
        # ans2 = 0
        # for i in num2:
        #     ans2 = ans2*10 + ord(i) - 48
        # return str(ans1*ans2)
                    
 # 13. 474. Ones and Zeroes - https://leetcode.com/problems/ones-and-zeroes/    
# doubt

            
# 14. valid tic tac toe
# doubt                    
                
























