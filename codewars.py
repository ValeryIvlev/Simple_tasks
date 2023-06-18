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