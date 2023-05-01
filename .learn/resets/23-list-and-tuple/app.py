# def list_gen():
#     #csn =[]
#     # csn = input('linput comma seperated list')
#     # csn.replace(",","")
#     # return tuple(csn)
#     csn = []
#     csn = input('Enter COMMA seperated NUMBERS :')
#     csn = csn.replace(',', "")
#     print(csn)
#     csn = list(csn)
#     #print(csn)
#     #print (type(csn))
#     return tuple(csn)

# print (list_gen())
values=input("")
l=values.split(",")
t=tuple(l)
print (l)
print (t)

# 
values=input("")
t=tuple(values.split(','))
print(t)