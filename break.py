#digunakan untuk menstop perulangan

for i in range(1, 100):
    if i % 50 == 0:
        break           #kebalikan dari CONTINUE. BREAK diginakan untuk menhentikan LOOPING jika nilai nya sudah bernilai TRUE
    print(i)