def deleteArray(values,posisi,arrSize):
    tempValues = [None] * arrSize
    for i in range(posisi,arrSize-1,1):
        values[i] = values[i + 1]
    tempValues = values
    values = [None] * (arrSize - 1)
    
    for i in range(0,arrSize-1,1):
        values[i] = tempValues[i]
    return values
#================= Main function =================#
ArrSize = int(input("Masukkan Array Size : "))
array = [None] * ArrSize
for i in range(0,ArrSize):
    array[i] = int(input(f"Masukkan Array indeks {i} : "))
array
posisi = 4#misal mau dibuat dinamis tinggal posisi = int(input("Masukkan Posisi : "))
print(deleteArray(array,posisi,ArrSize))