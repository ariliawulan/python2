white=[255,255,255]
red=(255,0,0)

print(white[1])
#hasilnya akan 255 karena waktu cetak disini belum berubah

red[0]=128
print(red[0])
#hasilnya akan error karena tuple tidak bisa di modif dan bersifat immutable

white[1]=155
print(white[1])
#white yang semula bernilai 255 akan terubah 155 karena list bisa diubah