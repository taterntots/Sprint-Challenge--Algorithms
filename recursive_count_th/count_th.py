'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # (base case) If word is smaller than two characters, return zero
    if len(word) < 2:
        return 0

    # Recursively check the string for 'th'
    if 'th' in word:
        print(word)
        return 1 + count_th(word.replace('th', '[YOINK]', 1))
    else:
        return 0

print(f'Total Count:', count_th('therapyth'))

# -------------------------------
# UNDERSTANDING THE PROBLEM
# -------------------------------

# We are trying to determine how many times the letters 'th' appear in a given word. The letters 'th' must appear in that exact order. They must also be lowercase because casing matters.

# -------------------------------
# PLANNING
# -------------------------------

# WITH RECURSION
# Declare base case:
    # If word is smaller than two characters, return zero
# If the letters 't' and 'h' are found next to each other, replace 'th' with GOTCHA
# Return the counter

# WITHOUT RECURSION
# Loop through the word and split it into a list of characters
# If the letters 't' and 'h' are found next to each other, add one to a counter
# Return the counter