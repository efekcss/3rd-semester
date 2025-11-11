# Soru 7-4 //bulunca çıksın
list1=[10,20,30,40,50]
list2=[10,80,90,20]
sayaç=0
for i in list1:
    for j in list2:
        if i==j:
            sayaç+=1
            break
    if sayaç==1:
        break
if sayaç>0:
    print("Ortak değer var")
else:
    print("Ortak değer yok")
