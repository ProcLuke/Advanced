def transform_words(words:list) -> list:
    #def transformation(word:str) -> str:
    #    return word.upper() + str(len(word))
    
    #transformation = lambda w: w.upper() + str(len(w))

    return list(map(lambda w: w.upper() + str(len(w)), words))
