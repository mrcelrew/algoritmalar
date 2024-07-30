def fakt(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakt(n - 1)

def us(tab, exp):
    return tab ** exp

def cos_taylor(x):
    cos_x = 1
    for n in range(1, 10):
        cos_x += (-1)**n * (us(x, 2*n) / fakt(2*n))
    return cos_x

while True:
    try:
        x = float(input("x değerini giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

print("cos(x) =", cos_taylor(x))