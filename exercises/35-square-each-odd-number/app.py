
def square_odds():  
    lst = input('input list of numbers: ')
    lnums = lst.split(',')
    #lnums = [int]
    ln_square = [int(x)*int(x) for x in lnums if  int(x) % 2 == 1]
    return ln_square

#lnums = "1,5,2,3,6,7, 9"
print(square_odds())