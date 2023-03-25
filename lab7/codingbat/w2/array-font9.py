def array_front9(num):
    for i in range(4):
        if i < len(num) and num[i] == 9:
            return True
                  
    return False