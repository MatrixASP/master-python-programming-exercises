def remove_duplicate_words(text):
    text = text.split()
    txt = set(text)
    txt = sorted(txt)
    txt =  " ".join(txt)
    return txt

words = ' hello world and practice makes perfect and hello world again'

print (remove_duplicate_words(words))