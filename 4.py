def carpma(A, B):
    sonuc = 0
    for _ in range(B):
        sonuc += A
    return sonuc

A = int(input("A sayısını girin: "))
B = int(input("B sayısını girin: "))
print("Sonuç:", carpma(A, B))
