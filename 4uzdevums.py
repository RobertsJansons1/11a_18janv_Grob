def lasitajs(fail_nosauk):
    try:
        with open(fail_nosauk, "r", encoding="utf8") as fails:
            saturs = fails.read()
            print("Fails satur:")
            print(saturs)
    except FileNotFoundError:
        print("Fails neeksistē.")

def puce():
    try:
        fail_nosauk = input("Ieraksti faila nosaukumu!:")
        formats = input("Ievadi faila formātu!:")
        pilnais_nosauk = f"{fail_nosauk}.{formats}"

        lasitajs(pilnais_nosauk)
    except FileNotFoundError:
        print("Fails neeksistē.")

if __name__ == "__puce__":
    puce()


    

