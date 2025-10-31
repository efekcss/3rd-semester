
"""# Harf notundan sonuç kararı
harf=input("Harf Notu=")
if len(harf) != 2:
    print("Geçersiz not")
else:
    if "A" in harf:
        print("Şahane")
    elif "B" in harf:
        print("Çok iyi")
    elif "C" in harf:
        print("İyi")
    elif "D" in harf:
        print("Geçer")
    elif "F" in harf:
        if harf=="F1":
            print("Devamsız")
        else:
            print("Kalır")
    else:
        print("Geçersiz not")
"""
"""#Hata kontrol geliştirin              
"""
harf=input("Harf Notu=").upper()
if len(harf) != 2 and harf not in ["A","B","C","D","F","1","2","3"]:
    print("Geçersiz not")
else:
    if "A" in harf:
        print("Şahane")
    elif "B" in harf:
        print("Çok iyi")
    elif "C" in harf:
        print("İyi")
    elif "D" in harf:
        print("Geçer")
    elif "F" in harf:
        if harf.upper() == "F1":
            print("Devamsiz")
        else:
            print("Kalir")
    else:
        print("Geçersiz not")