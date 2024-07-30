def kare(A, B, C, D):
	return A == B and B == C and C == D
A = int(input("A değeri: "))
B = int(input("B değeri: "))
C = int(input("C değeri: "))
D = int(input("D değeri: "))
print("kare mi?", kare(A, B, C, D))
