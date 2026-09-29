for i in range(1,7):
    print(i)
    if i==6:
        break

for i in range(1,13):
    print(i)
    if i==4:
        continue
    if i==6:
        print("You hit the halfway mark!")
        pass