# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(s):
    
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s % 60
    if (sec % 1 != 0):
        sec = int((sec * 100) + 0.5) / 100.0
    
    ho =    ' hours'
    mi =    ' minutes'
    se =    ' seconds'
    comma = ', '
    
    if h == 1:   ho = ho[:len(ho)-2]       
    if m == 1:   mi = mi[:len(mi)-2]        
    if sec == 1: se = se[:len(se)-2]
    
    
    answer = [h, ho, comma, m, mi, comma, sec, se]
    answer = [str(x) for x in answer]
    return ''.join(answer)
