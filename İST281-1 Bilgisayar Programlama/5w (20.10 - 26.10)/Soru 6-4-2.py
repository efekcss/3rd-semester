# Soru 6-4 Asal sayılar (bayrak kullanmadan)
limit=int(input("Sinir: "))
bölen=0
for sayi in range(2,limit):
    for bolen in range(2,sayi):
        if sayi % bolen == 0:
            # sayı asal değil
            break
    if sayi == bölen:
        print(sayi, "Asaldir.")
#Hatayı bulun
