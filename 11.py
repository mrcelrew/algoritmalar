def kaprekar(sayi):
    s = f"{sayi:04d}"
    
    KAPREKAR_CONSTANT = 6174
    
    while True:
        kb = ''.join(sorted(s))
        bk = kb[::-1]

        bk_num = int(bk)
        kb_num = int(kb)
        

        s = str(bk_num - kb_num).zfill(4)
        
        if int(s) == KAPREKAR_CONSTANT:
            return True
        
        elif s == "0000":
            return False

s = int(input("4 basamaklı bir sayı giriniz: "))

if kaprekar(s):
    print("Bu orjinal bir sayıdır ve sonuç 6174'tür.")
else:
    print("Bu orjinal bir sayı değil.")
