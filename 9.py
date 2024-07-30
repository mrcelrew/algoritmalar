def ikilik_sayi_sistemi(n):
    return bin(n).replace("0b", "")
n = int(input("Bir tam sayı girin: "))
print("İkilik sistemde:", ikilik_sayi_sistemi(n))
