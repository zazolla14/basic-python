def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print(f"Nama            : {kontak['nama']}")
        print(f"Email           : {kontak['email']}")
        print(f"No Telephone    : {kontak['no_telp']}")
        print("======================================")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    no_telp = input("No Telepon : ")

    kontak = {
        "nama" : nama,
        "email" : email,
        "no_telp" : no_telp
    }
    return kontak

def hapus_kontak(daftar_kontak):
    nama_kontak = input("Nama kontak yang akan dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):                  #setiap isi dari array daftar_kontak akan dimasukan ke dalam variabel i
        kontak = daftar_kontak[i]
        if nama_kontak == kontak["nama"]:                   #daftar_kotak[i] yaitu menampilkan nomer array dari variabel i, kemudian daftar_kontak[0] dengan key ["nama"] apakah sudah sama dengan nama_kontak
            index = i                                       #value dari variable i dimasukan ke dalam variabel index, lalu.......
            break

    if index == -1:                                         #jika index tidak sama dengan i, maka data tidak ditemukan, karena program tidak menjalan index = i
        print("Maaf Data Nama tidak ditemuka")
    else:
        del daftar_kontak[index]
        print("Data Nama Kontak berhasil dihapus!")

def cari_kontak(daftar_kontak):
    nama_kontak = input("Cari kontak berdasarkan nama : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if nama_kontak == kontak["nama"]:
            index = i
            break

    if index == -1:
        print("Maaf Data Nama tidak ditemuka")
    else:
        print(f"Nama : {daftar_kontak[index]['nama']}")
        print(f"Email : {daftar_kontak[index]['email']}")
        print(f"Nomer Telephone : {daftar_kontak[index]['no_telp']}")