def fd(n):
    toplam = sum(1 / (x ** 2) for x in range(1, n + 1))
    return toplam

n = int(input("n değeri: "))
print("Fonksiyon Değeri: ", fd(n))
