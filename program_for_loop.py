#TUGAS akan menginput data dari pengguna menggunakan IF, FOR LOOp, LSIT, RANGE

banyak = int(input("Berapa banyak data yang akan diinput : "))
banyak2= banyak + 1

nama=[]
umur=[]
for no in range(1, banyak2):
    print(f"Masukan data ke {no} : ")
    n=input("Nama : ")
    u=int(input("Umur : "))

    nama.append(n)
    umur.append(u)

print("=======================")
print("Data berhasil disimpan!")
print("-----------------------")
pilihan = input("Apakah ingin menampilkan data (y/n) : ") 
print("=======================")

if pilihan == "y" or pilihan == "Y":
    print("Tampilan nama : ")
    print(nama)
    print("Tampilan umur : ")
    print(umur)

    print("================")
    print("Menampilkan Data")

    for i in range(0, len(nama)):
        tampil_n = nama[i]
        tampil_u = umur[i]
        print(f"Hasil input dengan nama {tampil_n} berumur {tampil_u}")
else:
    print("Keluar dari program!")