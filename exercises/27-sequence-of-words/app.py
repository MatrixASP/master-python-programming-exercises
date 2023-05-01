def sequence_of_words(words):
    ws = words.split(',')   
    wsort = sorted(ws)
    return (','.join(wsort))

words = 'without,hello,bag,world'
print(sequence_of_words(words))