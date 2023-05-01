#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
     if num > 9:
        num = str(num)
        num = num[-2:]
        num = int(num)
        return num
     else:
        return ('Number MUST be greater than 9')

#Invoke the function with any interger greater than 9.
print(last_two_digits(29786))
