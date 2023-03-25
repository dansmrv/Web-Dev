def array123(num):
    for i in range(len(num) - 2):
        if num[i] == 1 and num[i+1] == 2 and num[i+2] == 3:
            return True
                  
    return False