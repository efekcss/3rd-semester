# Soru 7-3
liste=["123","121","ahmet","xy","xyx"]
sayaç=0
for öğe in liste:
    if len(öğe)>2 and öğe[0]==öğe[-1]:
        sayaç +=1
print(f"Ölçütü sağlayan {sayaç} tane öğe vardır.")
