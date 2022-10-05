import random

inGame = True
rooms = []
items = []
inRoom = False
n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
n4 = random.randint(0,9)

print("Üdvözöllek a Logiscool Szabadulószobában!"
      "Az egyik ajtó elvezet a szabadságodhoz."
      "Meg kell találnod egy 4 jegyú jelszót."
      "Ezeket a számokat a 8 szoba valamelyikében találhatod meg."
      "")

while inGame:
    room_number = None
    if inRoom == False:
        room_number = input("Melyik szobát szeretnéd kiválasztani? (0-8)\n")
    # items.append("zseblámpa")
    # items.append("poroltó")
    if room_number == "-1":
        print("Haladás: ")
        for i in range(len(items)):
            print("Cuccok: ", items[i])

    if room_number == "0":
        inRoom = True
        if "zseblámpa" not in items:
            print("Egy sötét szobában találod magad,"
                  "épphogy a villanykapcsolót megtaláltad."
                  "Sajnos nem múködik. Ehhez egy zseblámpára lesz szükség.")
            # room_number = input("Melyk szobát szeretnéd kiválasztani? (0-13)\n")
        if "zseblámpa" in items:
            print("Belépsz a szobába és felkapcsolod a zseblámpát. "
                  "Találsz magad előtt egy lepedővel leterített ágyat.")
            bedcheck = input("Be szeretnél alá nézni? (Igen/Nem)\n")
            while (bedcheck):
                if (bedcheck == "Igen" or bedcheck == "igen" or bedcheck == "I"):
                    print("Benézel az ágy alá, egy szörny ugrik ki alóla, amely"
                          " szétmarcangolja a tested, sajnos meghaltál.")
                    inGame = False
                    bedcheck = False
                elif (bedcheck == "Nem" or bedcheck == "nem" or bedcheck == "N"):
                    print("Nem néztél be az ágy alá, egy morgó hang jött ki alóla, "
                          "lehet hogy most jól döntöttél. Elhagyod a szobát.")
                    rooms.append(room_number)
                    bedcheck = False
                    inRoom = False
                else:
                    bedcheck = input("Be szeretnél alá nézni? (Igen/Nem)\n")
    if room_number == "1":
        inRoom = True
        print("Egy raktárban találod magad, nézz szét a polcokon, hátha találsz valami hasznosat.")
        polc = input("Melyik polcot nézed meg először? (1-4)\n")
        while polc:
            if polc == "1":
                print("Ezen a polcon nincs semmi.")
                # polc = False
                polc = input("Melyik polcot nézed meg? (1-4)\n")
            elif polc == "2":
                if "cigaretta" not in items:
                    print("Találsz egy cigaretátt.")
                    items.append("cigaretta")
                else:
                    print("Már van cigarettád.")
                # polc = False
                polc = input("Melyik polcot nézed meg? (1-4)\n")
            elif polc == "3":
                if "szobakulcs6" not in items:
                    print("Találtál egy kulcsot. A 6-os szám van rajta.")
                    items.append("szobakulcs6")
                else:
                    print("Nincs itt semmi.")
                polc = input("Melyik polcot nézed meg? (1-4)\n")
            elif polc == "4":
                print("Ezen a polcon nincs semmi.")
                polc = input("Melyik polcot nézed meg? (1-4)\n")
            elif polc == "-1":
                print("Kimész a szobából.")
                polc = False
                inRoom = False
            else:
                polc = input("Melyik polcot nézed meg először? (1-4)\n")
    if room_number == "2":
          inRoom = True
          if "poroltó" not in items:
              print("Egy lángoló szobába lépsz be, nincs nálad poroltó, így"
                    " nem tudsz tovább haladni. Kilépsz a szobából.")
              inRoom = False
          else:
              print("Eloltottad a tüzet és egy számot találtál a tűzben. "+str(n1)+ "XXX "
                    "Kimész a szobából.")
              inRoom = False
    if room_number == "3":
            inRoom = True
            print("Egy olyan szobába lépsz, ahol több minden is megtalálható, egy ágy, "
                  "egy asztal, egy szekrény, és egy polc.")
            choosenone = input("Mit nézel meg először? (ágy, asztal, szekrény, polc)\n")
            while choosenone:
                  if choosenone == "ágy":
                        if "poroltó" not in items:
                              print("Benézel az ágy alá, ott találsz egy porolót.")
                              items.append("poroltó")
                              choosenone = input("Mit nézel meg? (ágy, asztal, szekrény, polc)\n")
                        else:
                              print("Benézel az ágy alá, de nincs ott már semmi.")
                              choosenone = input("Mit nézel meg? (ágy, asztal, szekrény, polc)\n")
                  elif choosenone == "asztal":
                        opened = input("Több fiók is van az asztalon, melyiket nyitod ki? (1-3)")
                        while opened:
                              if opened == 1:
                                    print("Felrobbantál, egy C4 volt odarögzítve a fiókhoz.")
                                    inGame = False
                  else:
                        choosenone = input("Mit nézel meg? (ágy, asztal, szekrény, polc)\n")
