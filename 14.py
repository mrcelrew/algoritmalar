s = int(input("Bir sayı giriniz: "))
print("\n")
eb = 0
while s > 0:
    eb = max(eb, s % 10)
    s //= 10
print("en büyük sayı", eb)
print("\n")