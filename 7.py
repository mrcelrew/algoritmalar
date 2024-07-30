def kob():
    t = 0
    sa = 0
    while True:
        s = int(input("Bir sayı girin: "))
        if sayi == 0:
            break
        t += s ** 2
        sa += 1
    return t / sa if sa > 0 else 0

print("Karelerin Ortalaması:", kob())
