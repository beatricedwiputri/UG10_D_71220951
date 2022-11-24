#Test Case 1
print("\(^o^) Selamat datang di Kalkulator Sederhana (^o^)/")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan")
print("Ketik 3 unutk menghitung perkalian")
print("Ketik 4 untuk menghitung pembagian")
print("Ketik 5 untuk menghitung sisa hasil bagi (modulus).")
print("Ketik 6 untuk menghitung pemangkatan")
pilihananda = input("Masukkan pilihan Anda:")
bilpertama = input("Masukkan bilangan pertama:")
bilkedua = input("Masukkan bilangan kedua:")

bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
penjumlahan = bilpertama+bilkedua
if(pilihananda == "1"):
    print("Hasil dari",bilpertama, "dijumlahkan dengan", bilkedua, "adalah", str(penjumlahan))
else:
    print("")

bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
pengurangan = bilpertama-bilkedua
if(pilihananda == "2"):
    print("Hasil dari",bilpertama, "dikurangkan dengan", bilkedua, "adalah", str(pengurangan))
else:
    print("")


bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
perkalian = bilpertama*bilkedua
if(pilihananda == "3"):
    print("Hasil dari",bilpertama, "dikalikan dengan", bilkedua, "adalah", str(perkalian))
else:
    print("")

bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
pembagian = bilpertama/bilkedua
if(pilihananda == "4"):
    print("Hasil dari",bilpertama, "dibagi dengan", bilkedua, "adalah", str(pembagian))
else:
    print("")

bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
pembagian = bilpertama%bilkedua
if(pilihananda == "5"):
    print("Hasil dari",bilpertama, "dimodulus dengan", bilkedua, "adalah", str(pembagian))
else:
    print("")

bilpertama = int(bilpertama)
bilkedua = int(bilkedua)
pemangkatan = bilpertama^bilkedua
if(pilihananda == "6"):
    print("Hasil dari",bilpertama, "dipangkatkan dengan", bilkedua, "adalah", str(pemangkatan))
else:
    print("")
