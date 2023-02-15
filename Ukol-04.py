
def overeni_cisla(tel_cislo: str)->bool:
    tel_cislo = tel_cislo.replace(" ","") #odebrání mezer
    if tel_cislo[:4] == "+420":
        if len(tel_cislo) == 13:
             for cislice in tel_cislo[1:]:
                 if cislice in "0123456789":
                     return True
             return False    
    elif len(tel_cislo) == 9: 
        for cislice in tel_cislo:
            if cislice in "0123456789":
                return True
        return False
    return False

def pocitat_cenu_zpravy(zprava: str)-> int:
    delka_zpravy = len(zprava)
    if delka_zpravy % 180 == 0:
        cena_zpravy = (delka_zpravy//180)*3
    else:
        cena_zpravy = (delka_zpravy//180 + 1)*3
    return cena_zpravy

tel_cislo = input("Jaké je Vaše číslo? ")
validni_cislo = overeni_cisla(tel_cislo)
if validni_cislo:
    zprava = input("Jakou zprávu si přejete zaslat? ")
    zprava_stoji = pocitat_cenu_zpravy(zprava)
    print(f"Vaše zpráva bude stát {zprava_stoji} Kč.")
else:
    print("Zadané telefonní číslo není platné.")

    
    
        