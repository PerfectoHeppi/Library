# =====================================================
#  НОМЫН САН — nom_san.py
#
#  Файлын мөр:        ner,zohiolch,une
#  Ангилал (tuple):   ("uran", "shinjleh", "huuhed")
#  Ажиллуулахдаа: python nom_san.py
# =====================================================

FAIL = "nomuud.txt"
ANGILAL = ("uran", "shinjleh", "huuhed")
ZEEL_FAIL = "zeeldsen_nomuud.txt"

# nom_unshih(fail)

def nom_unshih(fail):
    hariu = []
    dugaar = 0
    with open(fail, "r", encoding="utf-8") as f:
        for mur in f:
            mur = mur.strip()
            if mur == "":
                continue
            heseg = mur.split(",")
            angilal = ANGILAL[dugaar % len(ANGILAL)]
            hariu.append({
                "ner": heseg[0],
                "zohiolch": heseg[1],
                "une": int(heseg[2]),
                "angilal": angilal
            })
            dugaar += 1
    return hariu

def zeel_unshih(fail):
    with open(fail, "a", encoding="utf-8"):
        pass  # file baihgui bol shineer uusgene
    return nom_unshih(fail)

# nom_haruulah(nomuud)

def nom_haruulah(nomuud):
    dugaar = 1
    print(f"{'Dugaar':<8}{'Ner':<28}{'Zohiolch':<30}{ 'Une':<10}{'Angilal':<10}")
    for nom in nomuud:
        print(f"{dugaar:<8}{nom['ner']:<28}{nom['zohiolch']:<30}{nom['une']:<10}{nom['angilal']:<10}")
        dugaar += 1


# nom_haih(nomuud, ner)

def nom_haih(nomuud, utga):
    utga = utga.lower()
    hariu = []
    for nom in nomuud:
        if utga in nom["ner"].lower() or utga in nom["zohiolch"].lower():
            hariu.append(nom)
    return hariu

# angilaltai(nomuud, angilal)

def angilaltai(nomuud, angilal):
    hariu = []
    for nom in nomuud:
        if nom["angilal"] == angilal:
            hariu.append(nom["ner"])
    return hariu

# zeeld_avah(zeel, nomuud, ner)

def zeeld_avah(zeel, nomuud, ner):
    for nom in nomuud:
        if nom["ner"] == ner:
            zeel.append(nom)
            nomuud.remove(nom)
            return nom
    return False


# nom_mur_bichih(nom,fail)

def shine_mur_bicheh(nom, fail):
    with open(fail, "a", encoding="utf-8") as f:
        f.write(nom["ner"] + "," + nom["zohiolch"] + "," + str(nom["une"]) + "\n")
    return fail

# zeel_faild_bicheh(nom, fail)

def zeel_failand_bicheh(nom, fail):
    with open(fail, "a", encoding="utf-8") as f:
        f.write(nom["ner"] + "," + nom["zohiolch"] + "," + str(nom["une"]) + "\n")
    return fail
 
# nom_butsaah(zeel ner)

def nom_butsaah(zeel, nomuud, ner):
    for nom in zeel:
        if nom["ner"] == ner:
            zeel.remove(nom)
            nomuud.append(nom)
            return nom
    return False

# shine_nom_nemeh(nomuud, fail, ner, zohiolch, une)

def shine_nom_nemeh(nomuud, fail, ner, zohiolch, une, angilal):
    shine_nom = {
        "ner": ner,
        "zohiolch": zohiolch,
        "une": une,
        "angilal": angilal
    }
    nomuud.append(shine_nom)
    with open(fail, "a", encoding="utf-8") as f:
        f.write(ner + "," + zohiolch + "," + str(une) + "\n")
    return shine_nom

def nom_faild_baigaa_esekh(fail, ner):
    with open(fail, "r", encoding="utf-8") as f:
        for mur in f:
            mur = mur.strip()
            if mur == "":
                continue
            heseg = mur.split(",")
            if heseg[0] == ner:
                return True
    return False


def nom_faild_ustgah(fail, ner):
    murnuud = []
    with open(fail, "r", encoding="utf-8") as f:
        for mur in f:
            mur = mur.strip()
            if mur != "":
                murnuud.append(mur)

    shine_murnuud = []
    ustgasan = False
    for mur in murnuud:
        heseg = mur.split(",")
        if not ustgasan and heseg[0] == ner:
            ustgasan = True
            continue
        shine_murnuud.append(mur)

    with open(fail, "w", encoding="utf-8") as f:
        for mur in shine_murnuud:
            f.write(mur + "\n")

    return ustgasan


# niit_une(zeel)

def niit_une(zeel):
    dun = 0
    for nom in zeel:
        dun = dun + nom["une"]
    return dun


def ajilluulah():
    nomuud = nom_unshih(FAIL)
 
    if not nomuud:
        print("Ном уншигдсангүй. nom_unshih функцээ шалгана уу.")
        return
 
    zeel = zeel_unshih(ZEEL_FAIL)
 
    while True:
        print()
        print("===== НОМЫН САН =====")
        print("1 - Бүх ном харах")
        print("2 - Ангиллаар харах")
        print("3 - Нэр/Зохиолчоор хайх")
        print("4 - Зээлд авах")
        print("5 - Ном буцаах")
        print("6 - Зээлсэн номууд харах")
        print("7 - Шинэ ном нэмэх")
        print("0 - Гарах")
 
        songolt = input("Сонголт: ").strip()
 
        if songolt == "1":
            nom_haruulah(nomuud)
 
        elif songolt == "2":
            dugaar = 1
            angilal = input("Ангилал (uran / shinjleh / huuhed): ").strip()
            neruud = angilaltai(nomuud, angilal)
            if neruud:
                for ner in neruud:
                    print(f"{dugaar}. ", ner)
                    dugaar += 1
            else:
                print("Ийм ангилал алга.")
 
        elif songolt == "3":
            utga = input("Хайх нэр эсвэл зохиолч: ").strip()
            oldsonuud = nom_haih(nomuud, utga)
            if oldsonuud:
                for nom in oldsonuud:
                    print(" -", nom["ner"], "|", nom["zohiolch"], "|", nom["une"], "|", nom["angilal"])
            else:
                print("Тохирох ном олдсонгүй.")
 
        elif songolt == "4":
            ner = input("Номын нэр: ").strip()
            zeelsen_nom = zeeld_avah(zeel, nomuud, ner)
            if zeelsen_nom:
                shine_mur_bicheh(zeelsen_nom, ZEEL_FAIL)
                nom_faild_ustgah(FAIL, ner)
                print("Зээлд авлаа:", ner)
            else:
                print("Ийм ном байхгүй байна.")
 
        elif songolt == "5":
            ner = input("Буцаах номын нэр: ").strip()
            butsaasan_nom = nom_butsaah(zeel, nomuud, ner)
            if butsaasan_nom:
                if not nom_faild_baigaa_esekh(FAIL, ner):
                    shine_mur_bicheh(butsaasan_nom, FAIL)
                nom_faild_ustgah(ZEEL_FAIL, ner)
                print("Буцаалаа:", ner)
            else:
                print("Энэ ном таны зээлийн жагсаалтад алга байна.")
 
        elif songolt == "6":
            if not zeel:
                print("Зээлсэн ном алга байна.")
            else:
                for nom in zeel:
                    print(" -", nom["ner"], nom["zohiolch"], nom["une"])
                print("Нийт:", niit_une(zeel), "төгрөг")
 
        elif songolt == "7":
            ner = input("Шинэ номын нэр: ").strip()
            zohiolch = input("Зохиолч: ").strip()
            une_str = input("Үнэ: ").strip()
            angilal = input("Ангилал (uran / shinjleh / huuhed): ").strip()
            while angilal not in ANGILAL:
                print("Ангилал зөвхөн", ANGILAL, "эдгээрийн нэг байх ёстой.")
                angilal = input("Ангилал (uran / shinjleh / huuhed): ").strip()
            if une_str.isdigit():
                shine_nom_nemeh(nomuud, FAIL, ner, zohiolch, int(une_str), angilal)
                print("Нэмэгдлээ:", ner)
            else:
                print("Үнийг зөвхөн тоогоор оруулна уу.")

        elif songolt == "0":
            print("Баяртай.")
            break
 
        else:
            print("Буруу сонголт.")
 
 
if __name__ == "__main__":
    ajilluulah()