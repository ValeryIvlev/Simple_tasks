# 2341

# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
#
# Return a 0-indexed integer array answer of size 2 where answer[0]
# is the number of pairs that are formed and answer[1]
# is the number of leftover integers in nums after doing the operation as many times as possible.

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        a = {}
        total_par = 0
        count = 0
        for i in nums:
            a[i] = a.get(i, 0) + 1

        for value in a.values():
            if value % 2 == 0:
                s = value // 2
                total_par += s
            elif value == 1:
                count += 1
                continue
            else:
                s = (value - 1) // 2
                count += 1
                total_par += s
        return [total_par, count]

# 2148. Count Elements With Strictly Smaller and Greater Elements

# Given an integer array nums, return the number of elements that have both a strictly
# smaller and a strictly greater element appear in nums.

class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        for i in nums:
            if i == min(nums):
                while i in nums2:
                    nums2.remove(i)
            if i == max(nums):
                while i in nums2:
                    nums2.remove(i)
        return len(nums2)

# 9. Palindrome Number

# Given an integer x, return true if x is a
# palindrome and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1] and x >= 0:
            return True
        else:
            return False

# 66. Plus One

#You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        a = ''.join(digits)
        a = str(int(a) + 1)
        s = list(map(int, [i for i in a]))
        return s

# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False