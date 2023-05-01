def two_dimensional_array(rows, cols):
    arr=[]
    # rows, cols = 3,5
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(i*j)
        arr.append(col)
        
    return (arr)

print(two_dimensional_array(2, 7))