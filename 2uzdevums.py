import csv

def bubo(fails_nosauk):
    with open(fails_nosauk, "r", encoding="utf8") as fails:
    
        csvlasitajs=csv.reader(csvfile)
        for rinda in csvlasitajs:
            print(rinda)
    
