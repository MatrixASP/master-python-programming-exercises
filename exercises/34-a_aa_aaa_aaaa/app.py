def calc_sum_a():
    num = input('Input number for calculation: ')
    d = int(num)
    d10 = d*10 + d
    d100 = d*100 + d10
    d1000 = d*1000 + d100
    sum = d + d10 + d100 + d1000
    return sum

print(calc_sum_a())
    
    