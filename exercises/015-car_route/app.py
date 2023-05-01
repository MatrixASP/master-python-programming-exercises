#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.
import math
def car_route(n,m):
    # rnd = round(m/n)
    
    # actual = m/n
    
    # if actual > rnd:
    #     return rnd + 1
    # else:
    #     return rnd
    return math.ceil(m/n)
  #return None


#Invoke the function with two intergers.
print(car_route(20,44))