import json
with open("body.json", "r", encoding="utf=8") as body_file:
    data = json.load(body_file)
    Vysledek_zkousky = {}
    for jmeno,body in data.items():
        if body >= 60:
            Vysledek_zkousky[jmeno] = "Pass"
        else:
            Vysledek_zkousky[jmeno] = "Fail"


with open("prospech.json", "w") as vysledek_file: 
    json.dump(Vysledek_zkousky, vysledek_file)
