def complex_word_filter(words, min_length):
    return list(map(lambda w: w.upper() + str(w.count("a") + w.count("e") + w.count("i") + w.count("o") + w.count("u")), filter(lambda x: len(x)>min_length,words)))
