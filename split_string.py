# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    arr = []
    index = 0
    
    if (source[len(source)-1] not in splitlist):
        source = source + splitlist[0]
        
    
    for word in range(len(source)): 
        if source[word] in splitlist:
                arr.append(source[index:word])
                index = word + 1
    print(arr)
    return [x for x in arr if x != '']