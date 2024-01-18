def bubo(fails_nosauk):
    try:
        with open(fails_nosauk, "r", encoding="utf8") as fails:
            print(fails.read())
    except FileNotFoundError:
        print("Fails netika atrasts!")
fails_nosauk = "tekstins.txt"
bubo(fails_nosauk)
