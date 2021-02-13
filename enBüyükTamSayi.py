liste = []
adet = int(input('Kaç Tane Tam Sayı Gireceksin: '))
for n in range(adet):
    sayi = int(input('Lütfen tam sayı gir: '))
    liste.append(sayi)
b=0    
for x in liste:
    if x % 2 == 1 and x >= b:
        b = x

print("Listedeki en büyük tam sayı: : ",b)

