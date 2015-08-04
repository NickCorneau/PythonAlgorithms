# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(s):
    s = s.split()
    count = 0
    for word in s:
        count = count + 1
    return(count)