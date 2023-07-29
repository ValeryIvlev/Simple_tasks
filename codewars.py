# 5 kyu
# Moving Zeros To The End

# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    count_zero = lst.count(0)
    for i in range(count_zero):
        lst.remove(0)
    for i in range(count_zero):
        lst.append(0)
    return lst

# 5 kyu
# Extract the domain name from a URL

# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string. For example:

# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    new_url = url.replace('http://', '').replace('https://', '').replace('www.', '')
    return new_url[:new_url.find('.')]

# 6 kyu
# Highest Scoring Word

# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

def high(x):
    x = x.split()
    maximum = 0
    word = ''
    for i in x:
        minimum = 0
        for j in i:
            minimum += ord(j) - 96
            if maximum < minimum:
                maximum = minimum
                word = i

    return word


# 6 kyu
# Unique In Order

# Implement the function unique_in_order which takes as argument
# a sequence and returns a list of items without any elements
# with the same value next to each other
# and preserving the original order of elements.

def unique_in_order(sequence):
    last_i = ''
    a = []
    for i in sequence:
        if i != last_i:
            a.append(i)
        last_i = i
    return a