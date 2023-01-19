jmeno_a_prijmeni = input("Napiš svoje jméno: ")
jmeno_a_prijmeni_velke = jmeno_a_prijmeni.upper()
jmeno_a_prijmeni_male = jmeno_a_prijmeni.lower()
jmeno_a_prijmeni_prvniVelka = jmeno_a_prijmeni.title()
jmeno = jmeno_a_prijmeni.split()[0]
prijmeni = jmeno_a_prijmeni.split()[1]
inicialy = jmeno[0] + "." + prijmeni[0] + "."
#print(inicialy)
#print(jmeno_a_prijmeni_male)
#print(jmeno_a_prijmeni_prvniVelka)
#print(jmeno_a_prijmeni_velke)
jmeno, prijmeni = jmeno_a_prijmeni.split()
jmeno = jmeno[0].lower() + jmeno[1,4].upper
prijmeni = prijmeni[0].upper() + prijmeni [2,3].upper
jmeno_a_prijmeni = jmeno + " " + prijmeni
print(jmeno_a_prijmeni)
