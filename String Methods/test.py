# strings are immutable
# string methods operate on existing strings and create a new string



var1 = "amna is a good girl"
print(len(var1))

# upper method = converts to uppercase
print(var1.upper())

# lower method = converts to lowercase
print(var1.lower())

a="this is beautiful !!!!!!"
# rstrip = removes the trailing characters and not the leading characters
print(a.rstrip("!"))

# replace = replaces all the occurences of a string with another string
print(a.replace("beautiful", "wonderful"))

blogheading = "Top 10 programming languages in 2024"
# split method = splits the string into a list of substrings based on a specified delimiter
print(blogheading.split(" "))

# capitalize=converts the first characetr of rhe string into uppercase
print(var1.capitalize())

# centre= aligns the string to centre as per the parameters given by the user
print(var1.center(50))

# count= counts the number of occurences of a substring in the string
print(blogheading.count("a"))

# endswith() = checks if the string ends with a specified suffix
print(blogheading.endswith("2024"))
print(blogheading.endswith("20203"))

# find= locates the first index of a given value in a string and returns 1 if it is not present in the stirng
print(blogheading.find("10"))

# alphanum=checks if a string consist of only alphanumeric characters(A-Z, a-z, 0-9)
print(blogheading.isalnum())

# isalpha= checks if a string consist of only alphabetic characters
print(blogheading.isalpha())

# islower()= checks if all the characters in a string are lowercase
print(var1.islower())

   # checks if all the characters in a string are uppercase
print(var1.isupper())

# istitle= checks if first character of every word in a string is capital or not
print(blogheading.istitle())

# title=converts first character of every word to a capital letter
print(blogheading.title())

