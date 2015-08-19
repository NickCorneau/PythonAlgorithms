# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return match, replacement


def apply_converter(converter, string):
    
    match, replacement = converter
    st = ''
    index = string.find(match)
    while (index != -1):
        if match not in string:
            break
        st = string[:index] + replacement + string[index+len(match):]        
        index = string.find(match)
        string = st
        print(index, st, string)
    return st

c1 = make_converter('&', 'and')
print apply_converter(c1, 'The cat & the dog')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaabaa')
#>>> ab

