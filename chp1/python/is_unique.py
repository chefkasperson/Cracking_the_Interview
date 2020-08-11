def isUnique(string):
    char_set = {}
    for element in string:
        if element in char_set:
            return False
        else:
            char_set[element] = True
        
        return True
