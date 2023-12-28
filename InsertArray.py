def insertArray(array,Newvalue,posisi,Arrsize):
    tempValues = []
    tempValues = array
    array = []
    array = [None] * (Arrsize + 1)
    for i in range(0, Arrsize,1):
        array[i] = tempValues[i]


    for i in range(Arrsize ,posisi, -1):
        array[i] = tempValues[i-1]
    
    array[posisi] = Newvalue

    return array
#================= Main function =================#
ArrSize = int(input("Masukkan Array Size : "))
array = [None] * ArrSize
for i in range(0,ArrSize):
    array[i] = int(input(f"Masukkan Array indeks {i} : "))
array
posisi = 3#misal mau dibuat dinamis tinggal posisi = int(input("Masukkan Posisi : "))
newvalue = 2#misal mau dibuat dinamis tinggal newvalue = int(input("Masukkan new value : "))
print(insertArray(array,newvalue,posisi,ArrSize))

    