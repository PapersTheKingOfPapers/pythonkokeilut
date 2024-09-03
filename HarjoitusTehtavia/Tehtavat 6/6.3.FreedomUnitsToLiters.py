def GallonToLiters(gallons):
    return gallons*3.785

userInput = float(input("Anna bensiinin määrä nestegallonoina: "))

while userInput >= 0:
    print(f"{userInput} gallonia on {GallonToLiters(userInput)} litraa.")
    userInput = float(input("Anna bensiinin määrä nestegallonoina: "))