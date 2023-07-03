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

# 1790. Check if One String Swap Can Make Strings Equal

# You are given two strings s1 and s2 of equal length.
# A string swap is an operation where you choose two indices in a string
# (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing
# at most one string swap on exactly one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        a = {i: s1.count(i) for i in s1}
        b = {i: s2.count(i) for i in s2}
        for i in range(len(s1)):
            if s1[i] != s2[i] and s1.count(s1[i]) == s2.count(s2[i]):
                count += 1
        if (count == 2 or count == 0) and a == b:
            return True
        else:
            return False

# 1491. Average Salary Excluding the Minimum and Maximum Salary

# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:-1]
        return sum(salary) / len(salary)

# 1859. Sorting the Sentence

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each word consists of lowercase and uppercase English letters.
#
# A sentence can be shuffled by appending the 1-indexed word position to each word
# then rearranging the words in the sentence.
#
# For example, the sentence "This is a sentence" can be shuffled
# as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words,
# reconstruct and return the original sentence.

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda x: x[-1])
        s = [i[0:len(i)-1] for i in s]

        return ' '.join(s)

# 455. Assign Cookies

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i],
# which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in s:
            for j in g:
                if i >= j:
                    count += 1
                    g.remove(j)
                    break
        return count

# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
#
# Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers:
                first = target - numbers[i]
                one = i
                break
        for j in range(len(numbers)):
            if first == numbers[j] and j != one:
                two = j
                break
        return [one+1, two+1]


# 1221. Split a String in Balanced Strings

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a = []
        count = 0
        for i in s:
            a.append(i)
            if a.count('L') == a.count('R'):
                count += 1
                a.clear()
        return count


# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters
# in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])