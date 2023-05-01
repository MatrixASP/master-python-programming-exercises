#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
      hrs = n // 60
      mins = n % 60
      
      return hrs, mins
  #return None

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(210))
