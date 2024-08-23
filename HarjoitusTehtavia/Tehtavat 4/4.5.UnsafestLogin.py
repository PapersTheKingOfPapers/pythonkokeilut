password = "rules"
username = "python"

tries: int = 0

while tries < 5:
    inputUsername = input("Käyttäjänimi: ")
    inputPassword = input("Salasana: ")
    if inputUsername == username and inputPassword == password:
        print("Tervetuloa")
        break
    else:
        tries+=1
if tries >= 5:
    print("Pääsy evätty")