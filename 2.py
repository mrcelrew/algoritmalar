def ortalama():
    t = 0
    sa = 0
    while True:
        s = int(input("Bir sayı girin: "))
        if s == 0:
            break
        t += s
        sa += 1
    return t / sa if sa > 0 else 0

print("Ortalama:", ortalama())
