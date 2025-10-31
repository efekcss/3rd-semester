# Soru 6-4 Asal sayılar
limit=int(input("Sinir : "))
for sayi in range(2,limit):
    bayrak=0
    for bolen in range(2,sayi):
        if sayi % bolen == 0:
            # sayı asal değil
            bayrak=1  #flag
            break
    if bayrak == 0:
        print(sayi, "Asaldir.")
