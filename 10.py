while True:
    def ucak_hizi(t):
        if t <= 15:
            return (480 / 15) * t
        elif t <= 35:
            return 480
        elif t <= 50:
            return 480 - (480 / 15) * (t - 35)
        else:
            return 0
    
    t = float(input("Dakika giriniz: "))
    print("Uçağın hızı", ucak_hizi(t), "km hızda")