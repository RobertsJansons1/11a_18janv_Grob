def ieraksti_vardu(vards, fails):
    try:
        with open(fails, "a", encoding="utf8") as faila_o:
            faila_o.write(vards)
        print(f"Vārds "{vards}" tika ierakstīts "{fails}".")
    except FileNotFoundError:
        print("Fails netika atrasts!")
    except Exception:
        print("Kļūda, izņēmums!")

def puce():
    try:
        vards = input("Ievadi savu vārdu!:")
        fails = "vardi.txt"

        ieraksti_vardu(vards, fails)
    except FileExistsError:
        print("Fails jau ir!")

    __name__ = "__puce__":
    fails

    vards = ievad_vardu()

    
    