def generate_dict(n):
    sq_dict = {}
    i = 1
    
    while i <= n:
        sq_dict.update({i: i*i})
        i = i + 1 
    return sq_dict
        
print(generate_dict(8))