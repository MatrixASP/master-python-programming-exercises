#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
      num = str(num)
      num_arr = num.split('.')
      digit_s = num_arr[1][0]
      digit = int(digit_s)
      return digit
  #return None



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(23.3486))                      