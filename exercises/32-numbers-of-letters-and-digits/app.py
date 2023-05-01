def letters_and_digits():
    txt = input('Please input sentence with letters and numbers:  ')
    lett = 0
    numb = 0
    for l in txt:
        if l.isdigit():
            numb = numb+1
        elif l.isalpha():
            lett = lett +1
        else:
            continue
            
    return (" LETTERS {lett}\n NUMBERS {numb}  ")
            
#txt = 'hello world! 123'

print(letters_and_digits())