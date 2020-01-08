flat_number = int(input("Input flat number:  "))
if flat_number > 0 or flat_number <= 4 * 9 * 4:
    access = (flat_number + 35) // 36
    floor = ((flat_number - 36 * (access - 1)) + 3) // 4
    print("Access = ", access)
    print("Floor = ", floor)
else:
    print("Sorry but you input wrong flat number")