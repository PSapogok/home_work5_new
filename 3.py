FriendsAndCash =  {'John': 20 , 'Dan': 30 , 'Lois': 14 , 'Doug': 144 }
FriendsAndCash2 = {}

def summoney():
    total = 0
    for j in FriendsAndCash.values():
        total+=j
    print('Total money we have is',total,"$")

def namemaxcash():
    k = max(FriendsAndCash, key=FriendsAndCash.get)
    print(k, FriendsAndCash[k]) 

def izmenpolog():
    for i, j in FriendsAndCash.items():
        FriendsAndCash2[j] = i
    print(FriendsAndCash2)


summoney()
namemaxcash()
izmenpolog()