def kalanli_bolme(A, B):
    kalan = A
    bolum = 0
    while kalan >= B:
        kalan -= B
        bolum += 1
    return bolum, kalan

A = int(input("A sayısını girin: "))
B = int(input("B sayısını girin: "))
bolum, kalan = kalanli_bolme(A, B)
print("Bölüm:", bolum, "Kalan:", kalan)

