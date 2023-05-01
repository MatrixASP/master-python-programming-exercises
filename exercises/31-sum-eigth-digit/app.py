def sum_eigth_digit(lower, upper):
    values = []
    ##lower = '1000'
    ##upper = '3000'
    for num in range(int(lower), int(upper) + 1, 1):
        #for n in num:
        #print(str(num))
        num_str = str(num) # convert number
        cnt = 0
        for n in num_str:
            #print(n)
            if int(n) % 2 != 0 or int(n) == 0: #if not div by 2 bail oreve if n  == 0
                #print(n)
                break
            else:
                cnt +=1
                if cnt == 4:
                    values.append(int(num_str))
    return (values)
    
                
    
print(sum_eigth_digit('1000', '3000') )