x=0
y=10

if x or y:
    x +=1
    if not x or y:
        x+=1
    else:
        x+=2
else:
    x+=3

print(x)