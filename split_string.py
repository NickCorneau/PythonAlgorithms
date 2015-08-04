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
