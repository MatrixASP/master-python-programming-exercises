def check_case(txt) :
    up = 0
    lo = 0
    for l in txt:
        if l.isalpha():
            if l.isupper():
                lo += 1
            elif l.islower():
                up += 1
            else:
                pass
    return (f"UPPERCASE {up}, LOWERCASE {lo}")

txt = 'IS it Lower 123! OORG is cupper'
print(check_case(txt))
