def tek_cift_kontrol(sayi):
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"

sayi = int(input("Bir sayı girin: "))
print(tek_cift_kontrol(sayi))
