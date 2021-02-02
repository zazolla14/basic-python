nama_depan='Azola '     #pemberial spasi pada akhir kata bisa ditambahkan pada akhir kata tersebut atau bisa menggunakan " "/' ' sebagai format string spasi
nama_tengah='Zubizarreta '
nama_belakang='Azola '
nama_lengkap=nama_depan+nama_tengah+nama_belakang

#CARA KONVENSIONAL
perkenalan='Hallo nama saya' + nama_lengkap + 'biasa dipanggil' + ' ' + nama_depan      #cara ini terlalu panjang
#CARA STRING FORMAT
perkenalan2= f"Hello nama saya {nama_lengkap}biasa dipanggil {nama_depan}"             #cara ini lebih pendek, tetapi dengan menambahakn huruf f pada awal.
# HURUF F DIGIBAKAN UNTUK MENANDAI BAHWA ITU ADALAH STRING FORMAT

print(perkenalan)
print(perkenalan2)