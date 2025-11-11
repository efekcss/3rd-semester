#Soru 7-2
liste=[4,43,6,2,45]
enk=min(liste)
print("en küçük sayı=",enk)

#döngü ile

del liste, enk

liste=[4,43,6,2,45]
enk=liste[0]
for sayı in liste[1:]:
    if sayı < enk:
        enk=sayı
print("en küçük sayı=",enk)
