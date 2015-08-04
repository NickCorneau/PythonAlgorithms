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
