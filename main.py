import random
import string
import math

def vyber_znaky():
    znaky = string.ascii_lowercase

    velka_pismena = input("Chcete pouzit velka pismena? (ano/ne): ").strip().lower()

    while(velka_pismena != "ano" and velka_pismena != "ne"):
        print("Zadejte pouze ano nebo ne!")
        velka_pismena = input("Chcete pouzit velka pismena? (ano/ne): ").strip().lower()

    if velka_pismena == "ano":
        znaky += string.ascii_uppercase

    cislice = input("Chcete pouzit cislice? (ano/ne): ").strip().lower()

    while(cislice != "ano" and cislice != "ne"):
        print("Zadejte pouze ano nebo ne!")
        cislice = input("Chcete pouzit cislice? (ano/ne): ").strip().lower()

    if cislice == "ano":
        znaky += string.digits

    specialni_znaky = input("Chcete pouzit specialni znaky? (ano/ne): ").strip().lower()

    while(specialni_znaky != "ano" and specialni_znaky != "ne"):
        print("Zadejte pouze ano nebo ne!")
        specialni_znaky = input("Chcete pouzit specialni znaky? (ano/ne): ").strip().lower()

    if specialni_znaky == "ano":
        znaky += string.punctuation

    return znaky

def ziskej_delku():
    while True:
        try:
            delka = int(input("Zadejte delku: "))

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

heslo = vygeneruj_heslo(delka, znaky)
print(heslo)

H = vypocitej_entropii(delka, znaky)
print(f"Entropie hesla: {H:.4f} bitu")