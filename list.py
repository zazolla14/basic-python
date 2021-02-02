# LIST --> type data untuk kumpulan data

# membuat list yang merepotkan dan panjang
#nama1 = "zola"
#nama2 = "dety"
#nama3 = "zolla"
# telalu panjang, cara menggunakan LIST

# cara ini dengan menggunakn nomor INDEKS
nama = ["zolla", "dety", "zolla2"]
nama.append("zolla3")  # untuk menambahkan data kedalam list

print(nama)
print(nama[0])
print(nama[1])
print(nama[2])  # pemanggilan nama berdasarkan indeks dimulai dari 0
print(nama[3])

print(len(nama))  # untuk mengetahui jumlah data

# digunakan unutk menghapus data pada INDEKS, ketika meng hapus data  dari INDEKS maka data akan bergeser
nama.remove("zolla2")
print(nama)
