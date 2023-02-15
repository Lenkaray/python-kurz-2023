import json
# nahraje obsah souboru body.json do slovníku
with open("body.json", "r", encoding="utf=8") as body_file:
    data = json.load(body_file)

#vytvoří nový slovník s výsledkem "Prospěl, neprospěl"
    Vysledek_zkousky = {}
    for jmeno,body in data.items():
        if body >= 60:
            Vysledek_zkousky[jmeno] = "Pass"
        else:
            Vysledek_zkousky[jmeno] = "Fail"

# Uloží nový slovník s výsledky zkoušky do nového souboru - prospech.json
with open("prospech.json", "w") as vysledek_file: 
    json.dump(Vysledek_zkousky, vysledek_file)
