def print_formula():
    l_n = input('Get comma seperated numbers for FORMULA')
    l_n = l_n.split(',')
    #print(l_n)


    li = []
    C = 50
    H = 30
    #list_n = list_n.strip(",")
    for xi in l_n:
        #print(xi)
        D = (int(xi))
        Q = round((2*C*D/H)**0.5)
        li.append(Q)
    return li   

print(print_formula())