kuhaPituus = float(input("Minkä pituisen kuhan nappasit?"))

if(kuhaPituus >= 37):
    print("Hyvä nappaus!")
else:
    print(f"Liian lyhyt, olit {37-kuhaPituus} senttiä alimmasta sallitusta pyyntimitasta. \n vapauta kuha takaisin järveen.")