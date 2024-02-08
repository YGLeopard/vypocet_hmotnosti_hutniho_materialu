# Program pro propočítávání hmotnosti ocelových polotovarů na základě zadaných hodnot.
# 1. Program po zadání informací od uživatele, které budou výška, šířka a hloubka materiálu, bude umět spočítat celkovou hmotnost zadaného rozměru, na základě koeficientu a výpočtu.
# 2. Program ve svém rozhraní bude nabízet pro výpočet čtyři druhy materiálu. Kulatina, Plech, Trubka, Jekl.



def vyber_materialu():
    print("Vyberte druh materiálu!")
    print("1. Kulatina")
    print("2. Plech")
    print("3. Trubka")
    print("4. Jekl")
    
    volba_uzivatele = input("Zadejte číslo odpovídající druhu materiálu! ")

    if volba_uzivatele == "1":
        return "Kulatina"
    elif volba_uzivatele == "2":
        return "Plech"
    elif volba_uzivatele == "3":
        return "Trubka"
    elif volba_uzivatele == "4":
        return "Jekl"
    else:
        print("Neplatná volba materiálu. Zadejte prosím platné číslo: ")
        return vyber_materialu
    
#test
vybrany_material = vyber_materialu()
print(f"Vybrán materiál: {vybrany_material}")

def vypocet_hmotnosti_plechu(sirka_mm, delka_mm, tloustka_mm):
    #převedení rozměru na metry
    sirka_metry = sirka_mm / 1000
    delka_metry = delka_mm / 1000
    tloustka_metry = tloustka_mm / 1000
    #výpočet plochy v metrech čtverečních
    plocha = sirka_metry * delka_metry
    #hustota oceli v kg/m3
    hustota_oceli = 7850
    #vypočet hmotnosti plechu
    hmotnost = plocha * tloustka_metry * hustota_oceli

    return hmotnost

def vypocet_hmotnosti_kulatiny(prumer, delka):
    # Převedení průměru na poloměr
    polomer = prumer / 2
    # Výpočet objemu kulatiny
    objem = (3.141592653589793 * (polomer ** 2)) * delka
    # Hustota oceli v kg/m^3
    hustota_oceli = 7850
    # Výpočet hmotnosti kulatiny
    hmotnost = objem * hustota_oceli

    return hmotnost

def vypocet_hmotnosti_trubky(prumer, delka, tloustka):
    # Převedení průměru na poloměr
    polomer = prumer / 2
    # Výpočet vnějšího poloměru trubky
    vnitrni_polomer = polomer - tloustka
    # Výpočet objemu trubky
    objem = (3.141592653589793 * (polomer ** 2 - vnitrni_polomer ** 2)) * delka
    # Hustota oceli v kg/m^3
    hustota_oceli = 7850
    # Výpočet hmotnosti trubky
    hmotnost = objem * hustota_oceli

    return hmotnost

def vypocet_hmotnosti_jeklu(rozmer1, rozmer2, delka, tloustka_steny):
    # Výpočet plochy průřezu obdélníkového profilu
    plocha_prurezu = (rozmer1 - 2 * tloustka_steny) * (rozmer2 - 2 * tloustka_steny)
    # Výpočet objemu obdélníkového profilu
    objem = plocha_prurezu * delka
    # Hustota oceli v kg/m^3
    hustota_oceli = 7850
    # Výpočet hmotnosti obdélníkového profilu (Jeklu)
    hmotnost = objem * hustota_oceli
    return hmotnost

def dalsi_vypocet():
    volba = input("Chcete provést další výpočet? (ano/ne): ")
    return volba.lower() == "ano"

#Hlavní část programu
while True:
    vybrany_material = vyber_materialu()

    if vybrany_material == "Plech":
        sirka_plechu = float(input("Šířka plechu v mm: "))
        delka_plechu = float(input("Délka plechu v mm: "))
        tloustka_plechu = float(input("Tloušťka plechu v mm: "))
        hmotnost_plechu = vypocet_hmotnosti_plechu(sirka_plechu, tloustka_plechu, delka_plechu)
        print(f"Celková hmotnost plechu: {hmotnost_plechu: .2f} kg")
    elif vybrany_material == "Kulatina":
        prumer_kulatiny = float(input("Zadejte průměr kulatiny v mm: "))
        delka_kulatiny = float(input("Zadejte délku kulatiny v mm: "))
        hmotnost_kulatiny = vypocet_hmotnosti_kulatiny(prumer_kulatiny, delka_kulatiny)
        print(f"Celková hmotnost kulatiny: {hmotnost_kulatiny: .2f} kg")
    elif vybrany_material == "Trubka":
        prumer_trubky = float(input("Zadejte průměr trubky (v mm): "))
        delka_trubky = float(input("Zadejte délku trubky (v mm): "))
        tloustka_trubky = float(input("Zadejte tloušťku trubky (v mm): "))
        hmotnost_trubky = vypocet_hmotnosti_trubky(prumer_trubky, delka_trubky, tloustka_trubky)
        print(f"Celková hmotnost trubky: {hmotnost_trubky:.2f} kg")
    elif vybrany_material == "Jekl":
        rozmer1_jeklu = float(input("Zadejte první rozměr Jeklu (v mm): "))
        rozmer2_jeklu = float(input("Zadejte druhý rozměr Jeklu (v mm): "))
        delka_jeklu = float(input("Zadejte délku Jeklu (v mm): "))
        tloustka_jeklu = float(input("Zadejte tloušťku Jeklu (v mm): "))
        # Volání funkce pro výpočet hmotnosti Jeklu
        hmotnost_profilu = vypocet_hmotnosti_jeklu(rozmer1_jeklu, rozmer2_jeklu, delka_jeklu, tloustka_jeklu)
        print(f"Celková hmotnost Jeklu: {hmotnost_profilu:.2f} kg")
    else:
        print("Nepodporovaný druh materiálu.")
    
    pokracovat = dalsi_vypocet()
    if not pokracovat:
        break