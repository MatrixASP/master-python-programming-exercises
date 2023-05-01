#Complete the function to return the tens digit of a given interger
def tens_digit(num):
      num_S = str(num)  
      dig = num_S[-2]
      dig = int(dig)
      return dig
      
# @return None




#Invoke the function with any interger.
print(tens_digit(129854))