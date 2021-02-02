#merupakan tipe data yang mirip dengan list, tuple, dan set
#penyimpanan value dengan menggunakn bantuan key berupa string
#Sangat disarankan dalam penggunaan data yang sangat banyak, agar pengaksesan gampang karena menggunakn atribut

customer = {"Name":"Azola", "Age":21, "Address":"Cilacap"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

#FITUR EDIT DATA PADA IDCTIONARY
customer["Company"]="PT.MAJU"           #TMABHA ATRIBUT Company 
customer["Name"]="Azola Zubizarreta"    #EDIT DATA
#del customer["Address"]                 #DELETE DATA

#CARA PERTAMA
#print(f"{name} {age} {address}")

#CARA KEDUA
#for key in customer:
#   value = customer[key]
#    print(f"{key} : {value}")

#CARA KETIGA
#print(customer.items())
#for key in customer.items():
#    print(f"{key[0]} : {key[1]}")

#CARA KEEMPAT
print(customer.items())                 #method pada dictiory hasil nya kan mnejadi tuple

for key, value in customer.items():     #dengan menggunakn tuple maka, value dapat diambil ke dalam dua variable yaitu key dan value
    print(f"{key} : {value}")