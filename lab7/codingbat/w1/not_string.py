def not_string(str):
    if len(str) < 3 or str[:3] != "not":
        return "not " + str
          
    return str