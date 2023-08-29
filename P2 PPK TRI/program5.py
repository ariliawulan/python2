N = int(input("Masukkan jumlah detik: "))

A = 60*60*24
HARI = N//A
B = A*HARI
C = N-B
JAM = C//(60*60)
D = JAM*(60*60)
E = C-D
MENIT = E//60
DETIK = N%60

print("Detik yang dimasukkan", N)
print(HARI, "Hari", JAM, "jam", MENIT, "Menit", DETIK, "Detik")

#menggunakan format string literal
print(f"{N} detik sama dengan:")
print(f"{HARI} hari {JAM} jam {MENIT} menit {DETIK} detik.")
3