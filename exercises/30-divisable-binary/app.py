def divisible_binary(nums_s):
    nums = nums_s.split(',')
    arr=[]
    for n in nums:
        if n[0] != '0':
            num = int(n)
            if num % 5 == 0:
                arr.append(str(num))
    return ','.join(arr)

nums_s = '1001,1010,0011,0101,1000, 1010101, 011111, 10010'
print(divisible_binary(nums_s))