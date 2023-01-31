# ukol-02
## Zadání
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod = input("Zadejte kód součástky: ")
if kod not in sklad:
    print("Součástka není na skladu.")
else:
    objednane_mnozstvi = int(input("Jaké si přejete množství? "))
    if sklad[kod] < objednane_mnozstvi:
        print(f"Můžeme Vám prodat jen omezené množství - {sklad[kod]} kusů.")
    else:
        print(f"Objednávka produktu {kod} bude vyřízena.")