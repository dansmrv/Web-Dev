def caught_speeding(speed, is_birthday):
    a = 5 if is_birthday else 0
    
    if (speed <= 60 + a):
        return 0
              
    elif (60 + a < speed) and (speed <= 80 + a):
        return 1
                        
    else:
      return 2
