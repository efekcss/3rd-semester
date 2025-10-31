# Ateş tespit
ateş=float(input("Vucut sıcaklığı="))
if ateş <= 35.5:
    print("Hipotermi")
elif ateş <= 37.5:
    print("Normal")
elif ateş <= 38.5:
    print("Ateş")
else:
    print("Yüksek ateş")
