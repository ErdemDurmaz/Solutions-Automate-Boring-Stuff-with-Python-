inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#idea1 can add the word to dictionary as value when  you encounter twice
def addtoinventory(inv,addeditems):
    for item in dragonLoot:
        if item in inv:
            inv[item] +=1
        else:
            inv[item] = 1

def displayinventory():
    print("inventory: \n")
    item_total = 0
    for k,v in inv.items():
        print(str(v) + ' ' + k)
        item_total +=v
    print ("Total number of items: "+ str(item_total) )
addtoinventory(inv, dragonLoot)
displayinventory()


