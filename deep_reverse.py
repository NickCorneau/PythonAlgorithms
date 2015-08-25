# Procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(l):
    l.reverse()
    for i in l:
        if is_list(i):
            deep_reverse(i)
    return l
	
p = [1, [2, 3, [4, [5, 6]]]]
#>>> [[[[6, 5], 4], 3, 2], 1]