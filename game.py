import numpy as np
np = np.random.randint(1,101)
count = 0
while True:
    count+=1
    predicit_number = int(input("Enter number from 1 to 100 to select"))
    if predicit_number > np:
        print("Number must be less than", predicit_number,"  ")
    elif predicit_number < np:
        print("Number must be greater than", predicit_number,"  ")
    else:
        print(f"You have found {predicit_number} for the {count} trying")
        break

#Hello
