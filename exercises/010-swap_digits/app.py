#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    num_S = str(num)
    num = num_S[1] + num_S[0]
    num = int(num)
    return num
  # Your code here
  #return None
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(31))
