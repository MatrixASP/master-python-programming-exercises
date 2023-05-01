#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
      hrs = mins = 0
      if secs >= 3600:
            hrs = secs//3600
            secs = secs - (hrs * 3600)
            
      if secs > 60:
            mins = secs//60
            
      return hrs, mins
  #return None

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))