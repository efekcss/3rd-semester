#soru5-2
ülke="US"
tutar=10
if ülke=="AU":
    if tutar>50:
        print("Kargo ücretsiz")
    else:
        print("Kargo 10 TL")
elif ülke=="US":
    if tutar>150:
        print("Kargo ücretsiz")
    elif tutar>100:
        print("Kargo 1 TL")
    elif tutar >50:
        print("Kargo 3 TL")
    else:
        print("Kargo 5 TL")
else:
    print("Ülke kodu hatalı")
