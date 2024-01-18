def baba(faila_nosauk):
    with open(faila_nosauk, "r", encoding="utf8") as fails:
        rinda = fails.readlines()

        if len(rinda) == 3:
            tr_rinda = rinda[2]
            print(tr_rinda)
        
fails = "tekstins.txt"
baba(fails)
        