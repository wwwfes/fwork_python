kv = int(input("Appartment number is :"))

e = kv/4

# Access
if e <= 9:
    print("Access = 1")
if e > 9 and e <= 18:
    print("Access = 2")
if e > 18 and e <= 27:
    print("Access = 3")
if e > 27 and e <= 36:
    print("Access = 4")

#Floor
if e <=9 and (e % 4) == 1.0:
    print("Floor = ",int(e))
elif e <= 9 and (e % 4) != 1.0:
    print("Floor = ",int(e) + 1)

elif e> 9 and e<=18 and (e % 4) == 1.0:
    print("Floor = ",int(e)-9)
elif e > 9 and e <= 18 and (e % 4) != 1.0:
    print("Floor = ",int(e) - 9+1)

elif e > 18 and e<=27 and (e % 4) == 1.0:
    print("Floor = ",int(e)-18)
elif e > 18 and e <= 27 and (e % 4) != 1.0:
    print("Floor = ",int(e) - 18+1)


elif (e)>27 and (e)<=36 and (e % 4) == 1.0:
    print("Floor = ",int(e)-27)
elif (e) > 27 and (e) <= 36 and (e % 4) != 1.0:
    print("floor = ",int(e) - 27+1)