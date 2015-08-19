
def convert_seconds(s):
    
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s % 60
    
    if (sec % 1 == 0):    
        sec = int(sec)
    ho =    ' hours'
    mi =    ' minutes'
    se =    ' seconds'
    comma = ', '
    
    if h == 1:   ho = ho[:len(ho)-1]       
    if m == 1:   mi = mi[:len(mi)-1]        
    if sec == 1: se = se[:len(se)-1]
    
    
    answer = [h, ho, comma, m, mi, comma, sec, se]
    answer = [str(x) for x in answer]
    return ''.join(answer)

def download_time(data1, type1, data2, type2):
    if type1 == 'kb': type1 = 2 ** 10
    if type1 == 'kB': type1 = 2 ** 10 * 8
    if type1 == 'Mb': type1 = 2 ** 20
    if type1 == 'MB': type1 = 2 ** 20 * 8
    if type1 == 'Gb': type1 = 2 ** 30
    if type1 == 'GB': type1 = 2 ** 30 * 8
    if type1 == 'Tb': type1 = 2 ** 40
    if type1 == 'TB': type1 = 2 ** 40 * 8
        
    if type2 == 'kb': type2 = 2 ** 10
    if type2 == 'kB': type2 = 2 ** 10 * 8
    if type2 == 'Mb': type2 = 2 ** 20
    if type2 == 'MB': type2 = 2 ** 20 * 8
    if type2 == 'Gb': type2 = 2 ** 30
    if type2 == 'GB': type2 = 2 ** 30 * 8
    if type2 == 'Tb': type2 = 2 ** 40
    if type2 == 'TB': type2 = 2 ** 40 * 8
      
    bit_size1 = float(data1) * float(type1)
    bit_size2 = float(data2) * float(type2)

    download_speed = (bit_size1/ bit_size2)
    return(convert_seconds(download_speed))
