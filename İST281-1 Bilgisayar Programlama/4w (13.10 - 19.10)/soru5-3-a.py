# Soru 5-3-a
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b:
    if a>c:
        enb=a
    else:
        enb=c
else:
    if b>c:
        enb=b
    else:
        enb=c
print("en büyük=",enb)
