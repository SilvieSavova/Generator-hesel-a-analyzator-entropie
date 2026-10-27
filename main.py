import random
import string
import math

def vyber_znaky():
    znaky = string.ascii_lowercase

    velka_pismena = input("Chcete pouzit velka pismena? (a/n): ").strip().lower()

    while(velka_pismena != "a" and velka_pismena != "n"):
        print("Zadejte pouze a nebo n!")
        velka_pismena = input("Chcete pouzit velka pismena? (a/n): ").strip().lower()

    if velka_pismena == "a":
        znaky += string.ascii_uppercase

    cislice = input("Chcete pouzit cislice? (a/n): ").strip().lower()

    while(cislice != "a" and cislice != "n"):
        print("Zadejte pouze a nebo n!")
        cislice = input("Chcete pouzit cislice? (a/n): ").strip().lower()

    if cislice == "a":
        znaky += string.digits

    specialni_znaky = input("Chcete pouzit specialni znaky? (a/n): ").strip().lower()

    while(specialni_znaky != "a" and specialni_znaky != "n"):
        print("Zadejte pouze a nebo n!")
        specialni_znaky = input("Chcete pouzit specialni znaky? (a/n): ").strip().lower()

    if specialni_znaky == "a":
        znaky += string.punctuation

    return znaky

def ziskej_delku():
    while True:
        try:
            delka = int(input("Zadejte delku (min 12, max 64): "))

            if delka < 12:
                print("Heslo musi mit alespon 12 znaku!")
            elif delka > 64:
                print("Heslo muze mit maximalne 64 znaku!")
            else:
                return delka

        except ValueError:
            print("Zadejte prosim cele cislo!")

def vygeneruj_heslo(delka, znaky):
    heslo = ""

    for i in range(delka):
        heslo += random.choice(znaky)

    return heslo

def vypocitej_entropii(delka, znaky):
    H = delka * math.log2(len(znaky))

    return H

znaky = vyber_znaky()
delka = ziskej_delku()

i = 1

while True:
    heslo = vygeneruj_heslo(delka, znaky)
    print(f"{i}. {heslo}")

    H = vypocitej_entropii(delka, znaky)
    print(f"Entropie hesla: {H: .4f} bitu")

    pokracovat = input("\nChcete vygenerovat dalsi heslo? (a/n)\n" \
                       "a - Se stejnymi parametry\n" \
                       "b - S novymi parametry\n" \
                       "n - Ukoncit program\n" \
                       "Vase volba: ").strip().lower()

    while pokracovat != "a" and pokracovat != "b" and pokracovat != "n":
        print("Zadejte pouze a, b nebo n!")
        pokracovat = input("Vase volba: ").strip().lower()

    if pokracovat == "n":
        print("Program byl ukoncen.")
        break
    elif pokracovat == "b":
        znaky = vyber_znaky()
        delka = ziskej_delku()

    i += 1