# Tekrar eden harfler olmasın
metin1=input("1. metin: ")
metin2=input("2. metin: ")
cikti=""
for harf in metin2:
    if harf in metin1:
        if harf not in cikti: 
           cikti += harf
print(cikti)
