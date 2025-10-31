while True:
    print("En fazla 3 basamakli bir sayi girin : ")
    print("Cikmak için 'iptal' yazin")
    s = input("Sayi: ")

    if s == "iptal":
        print("Ciktiniz")
        break

    if len(s) <= 3:
        print("Oldu\n")
    else:
        print("Hatali sayi")