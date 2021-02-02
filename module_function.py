#fubction yang akan di panggil pada file module.py

def say_hello(nama):
    return f"Hello {nama}"

def total (*list_angka):
    hasil = 0
    for angka in list_angka:
        hasil = hasil + angka
    return f"Hasil dari total penjumlahan {list_angka} = {hasil}"