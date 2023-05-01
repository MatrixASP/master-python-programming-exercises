#Complete the function to return the number of day of the week for k'th day of year. 
def day_of_week(k):
    ddict = {'1': 4, '2':5, '3':6, '4': 0, '5': 1, '6': 2, '0': 3 }
    
    md = k%7
    md_str = repr(md)
    return ddict[md_str]
      




#Invoke function day_of_week with an interger between 0 and 6 (number for days of week)
print(day_of_week(1))