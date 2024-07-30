sayi = int(input("4 haneli bir sayı giriniz: "))
binler = sayi // 1000
yuzler = (sayi // 100) % 10
onlar = (sayi // 10) % 10
birler = sayi % 10
print("binler: ", binler, "\n yüzler: ", yuzler, "\n onlar: ", onlar, "\n birler: ", birler)
