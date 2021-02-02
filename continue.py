#DIGUNAKAN UNTUK MEN SKIP PROSES YANGF ADA PADA LOOPING dan melanjutkan ke proses selanjutnya

#program untuk menulis angka ganjil
for i in range(1, 99):  #for digunakan unutk mengulan angka 1 - 99
    if i % 2 != 2:      #jika i sisa bagi 2 hasil nya 0, maka angka itu genap. Jika hasil nya genap maka akan benilai TRUE dan berlanjut ke perintak CONTINUE
        continue        #COntinue digunakan untuk menskip proses yang ada dibawah nya, jika kondidi diatas nya bernilai benar
    print(i)            #printah print(i) akan tereksekusi jika program if diatas benilai FALSE