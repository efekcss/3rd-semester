sayi=int(input("Bir sayi giriniz: "))
sayaç=sayi
while sayaç>0:
    print(sayaç, end=" ")
    sayaç -= 1 #sayaç=sayaç-1
# For döngüsü ile
print()
sayi=int(input("Bir sayi giriniz: "))
for sayaç in range(sayi, 0, -1):
    print(sayaç, end=" ")
