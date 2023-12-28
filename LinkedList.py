def createLinkedList(Data):
    return {'Data':Data,'Next':None}

def InsertLinkedList(linkedList, Data):
    newLinkedList = createLinkedList(Data)
    newLinkedList['Next'] = linkedlist
    return newLinkedList
def printLinkedList(linkedList):
    while linkedList:
        linkedList = linkedList ['Next']
def searchLinkedList(linkedList,key):
    while linkedList is not None:
        if linkedList['Data'] == key:
            return linkedList
        linkedList = linkedList['Next']
    return None
def countNodes(linkedlist):#jumlah node
    if not linkedlist:
        return False
    count = 1  # Count head head node
    temp = linkedlist['Next']
    while temp != None and temp != linkedlist:
        count += 1
        temp = temp['Next']
    return count
#================= Main function =================#
linkedlist = None#input linked list
batas = int(input("Batas Linkedlist : "))
for i in range(0,batas):
    i = int(input(f"Linkedlist [Data {i}] : "))
    linkedlist = InsertLinkedList(linkedlist,i)

printLinkedList(linkedlist)#cetak
print(linkedlist)

key = int(input("Key Yang di cari : "))#cari linked list
if searchLinkedList(linkedlist, key):
    print('keyword', key, 'ditemukan')
else:
    print('keyword', key, 'tidak ditemukan')
linkedlist
#hitung jumlah node

print("Jumlah node : ",countNodes(linkedlist))#jumlah node