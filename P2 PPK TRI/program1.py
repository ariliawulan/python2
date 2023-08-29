bil1 = int(input("masukkan angka pertama : "))
bil2= int(input("masukkan angka kedua : "))

jumlah = bil1 + bil2
kurang = bil1 - bil2
kali = bil1 * bil2
bagi = bil1/bil2
modulus = bil1 % bil2

print("hasil dari %d + %d = %d " % (bil1,bil2,jumlah))
print("hasil dari %d - %d = %d " % (bil1,bil2,kurang))
print("hasil dari %d * %d = %d " % (bil1,bil2,kali))
print("hasil dari %d / %d = %d " % (bil1,bil2,bagi))
print("hasil dari %d mod %d = %d " % (bil1,bil2,modulus))
print(" ")


# Mencari Kesalahan / Debugging
print ("Hello, World!")
print (2 + 2),
print ("Test 123")

a = 2 * 4
print (a*a)
#penulisan print (aa) tidak terdefinisi karena jika perkalian dalam python harus memakai operator *
#dan jika akan print (aa) tidak terdifini karena aa bukan variabel makanya error
#jika ingin output aa maka penulisannya harus ("aa") bukan (aa)