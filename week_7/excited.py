def distinct(a):
    b=[]
    c=''
    for i in a:
        if i not in b:
            b.append(i)
    b.sort()
    for i in b:
        c+=str(i)
    return c
f= "sofwoeofoweofiosfmsosf"
print(distinct(f))