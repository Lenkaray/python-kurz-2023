morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
morse_code[" "] = "/" # Přidám nový klíč a hodnotu pro mezeru - zobrazí se jako pomlčka
uzivatel_zadani = input("Zadejte prosím, co chcete konvertovat do Morseovy abecedy: ")
morseovka_vysledek = [] # Vytvořený list, aby se do něj ukládaly jednotlivé znaky
for pismena in uzivatel_zadani:
    for klic, hodnota in morse_code.items():
        if klic == pismena:
            morseovka_vysledek.append(hodnota) #v rámci každého klíče se přidá do listu morseovka_vysledek jedno pismeno. To tam bude uloženo jako string, item
           
print(" ".join(morseovka_vysledek), end=" ") # .join přemění list na string a end nevím, proč tam je vlastně? 

    