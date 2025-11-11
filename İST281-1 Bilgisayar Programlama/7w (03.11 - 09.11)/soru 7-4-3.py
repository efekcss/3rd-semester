# Soru 7-4 //bulunca çıkmasın - for yerine while kullanalım
list1=[10,20,30,40,50]
list2=[10,80,90,20]
u1=len(list1)
u2=len(list2)
sayaç=0
i=0
while i < u1:
    j=0
    while j < u2:
        if list1[i]==list2[j]:
            sayaç+=1
        j+=1
    i+=1
if sayaç>0:
    print("Ortak değer var")
else:
    print("Ortak değer yok")
# sonraki prg: bulunca çıksın
# sonraki prg: if olmasın
