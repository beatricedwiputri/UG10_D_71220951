#Test Case 1
nama1 = input("Masukkan nama pemain pertama:")
nama2 = input("Masukkan nama pemain kedua:")
nama3 = input("Masukkan nama pemain ketiga:")
jml1 = input("Masukkan jumlah kartu pemain prtama:")
jml2 = input("Masukkan jumlah kartu pemain kedua:")
jml3 = input("Masukkan jumlah kartu pemain ketiga:")
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("ena menang dengan jumlah kartu terbanyak", max(list1))

#Test Case 2
nama1 = input("Masukkan nama pemain pertama:")
nama2 = input("Masukkan nama pemain kedua:")
nama3 = input("Masukkan nama pemain ketiga:")
jml1 = input("Masukkan jumlah kartu pemain pertama:")
jml2 = input("Masukkan jumlah kartu pemain kedua:")
jml3 = input("Masukkan jumlah kartu pemain ketiga:")
jml1 = int(jml1)
jml2 = int(jml2)
jml3 = int(jml3)
if(jml1>21,jml2>21,jml3>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
else:
    print("")
