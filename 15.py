print("""
      

sayı eğer 5-10 arasında ise girilen sayının karesini alıp gösteriyoruz, eğer
5'ten küçük ise faktöriyelini alıyoruz, 10'dan büyük ise sayıyı ikiye bölüp bir eksiğini yazıyoruz


""")


s = float(input("Bir sayı giriniz: "))
if 5 <= s <= 10:
    print("5-10 arasında girdiniz, işte size karesini veriyorum => ", s ** 2)
elif s < 5:
    fakt = 1
    for i in range(1, int(s) + 1):
        fakt *= i
    print("5'ten küçük girdiniz, işte sizee faktöriyeli => ", fakt)
else:
    print("10'dan büyük sayı girdiniz, işte size sayıyı ikiye bölüp verdim => ", (s / 2) - 1)