'''
Requirement:
User will supply a word from console.
Requirement 1) You need to find all the vowels(a/e/i/o/u) in the word.
Requirement 2) Further enhance your code, only collect vowels once (we don't want duplicate vowels)
'''

# PREPARE DATA BEGIN ===============================================

# 1) I need to store the 5 vowels letter into a list, so that I can check whether some letter is a member of the list or not
vowels = list("aeiou")

# 2) I need a variable which is to store the word user gives me
word = input("Please give me the word:")

# 3) I need a container (or a list) which is to hold all the vowels inside the word which user just gave me
found = []


# MAIN PROGRAM BEGIN ==============================================

# Step 1) Check and collect vowels

# I loop all the characters in the word to check whether it is a vowel
# Attention: loop a str value
for letter in word:

    # if the letter is a member of vowels list, then I append it to the list variable - found
    if letter in vowels:
        found.append(letter)


# Step 2) Print result
for vowel in found:
    print(vowel, end = ' ')