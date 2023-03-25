def last2(str):
    if len(str) < 2:
        return 0
          
    cnt = 0
    end = str[len(str)-2:]
                
    for i in range(len(str) - 2):
        if str[i:i+2] == end:
            cnt += 1
                                  
    return cnt