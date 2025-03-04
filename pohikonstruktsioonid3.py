#-----------------------
#MILAN PETROVSKI TARPV24


from datetime import *
from calendar import *
import math

tana = date.today() #datetime
print(f"Tere! T�na on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/%Y")
print(f"Tere! T�na on {tana_}")

# # December 27, 2022
# tana_ = tana.strftime("%B %d, %y")
# print(f"Tere! T�na on {tana_}")

# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# print(f"Tere! T�na on {tana}")

# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# print(f"Tere! T�na on {tana}")


#-----------------------
#�L 1
print("\n-----�L1-----")

paevadekogus = monthrange(2025, 1)[1]
print(f"Jaanuaris on {paevadekogus} p�eva!")

paevad = tana.day
onjaanud = paevadekogus - paevad
print(f"Jaanuaris on jaanud {onjaanud} p�eva!")

aastatoday = int(tana.strftime("%Y"))
aastalopuni = 365 - monthrange(aastatoday,1)[1] + onjaanud
print(f"Aasta l�puni on jaanud {aastalopuni} p�eva!")


#-----------------------
#�L 2
print("\n-----�L2-----")

arvutus1 = 3 + 8 / (4 - 2) * 4
print(f"sulgudega = {arvutus1}")
arvutus1 = 3 + 8 / 4 - 2 * 4
print(f"sulgudeta = {arvutus1}")


#-----------------------
#�L 3
print("\n-----�L3-----")

try:
    Raadius = float(input("Sisestage Raadius: "))
    Pindala_Ruut = round(math.sqrt(2*Raadius), 2)
    Pindala_Ring = round(math.pi * math.sqrt(Raadius), 2)
    umberm��t_ruut = round(8 * Raadius, 2)
    umberm��t_ring = round(2 * math.pi * Raadius, 2)
    print(f"\nRuudu pindala   = {Pindala_Ruut} | Ringi pindala   = {Pindala_Ring}")
    print(f"Ruudu �mberm��t = {Pindala_Ruut} | Ringi �mberm��t = {umberm��t_ring}")
except:
    print("Sisesta ujukomaarud!")


#-----------------------
#�L4
print("\n-----�L4-----")

d = 2.575 #m�ndi d sm
maaR = 6378 #maa raadius km
maaR *= 100000 #maa radius sm
Pmaa = 2 * math.pi * maaR #maa umberm��t
kogus = Pmaa / d
eur = kogus * 2

print(f"Maa ekvaatori �mberm��t on {Pmaa} km.")
print(f"Selle katmiseks l�heks vaja umbes {int(kogus): ,d} 2 euro m�ndi.")
print(f"See maksab {int(eur): ,d}  euro.")


#-----------------------
#�L5
print("\n-----�L5-----")

a ="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2, b, a*2, b, a*4)


#-----------------------
#�L6
print("\n-----�L6-----")

laulusonad_1 = """Rong see s�itis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?"""

laulusonad_2 = """Rong see s�itis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""

print(laulusonad_1.upper())
print()
print(laulusonad_2.upper())


#-----------------------
#�L7
print("\n-----�L7-----")
try:
    pikkus = float(input("Sisesta ristk�liku pikkus: "))
    laius = float(input("Sisesta ristk�liku laius: "))
    if pikkus > 0 and laius > 0:
        print("Pindala ja �mberm��du arvutamine: ")
        umermood = 2 * (pikkus + laius)
        pindala = pikkus * laius
        print(f"Ristk�liku �mberm��t on {umermood}")
        print(f"Ristk�liku pindala on {pindala}")
    else:
        print("Arvud peavad olema suurem kui 0!")
except ValueError:
    print("Sisesta ujukomaarud!")


#-----------------------
#�L8
print("\n-----�L8-----")

try:
    benz = float(input("Sisestage tangitud k�tuse liitrid: "))
    kml�bi = float(input("Sisestage l�bitud kilomeetrid: "))
    if benz > 0 and kml�bi < 1:
        print("Teil on auk bensiinipaagis.")
    else:
        keskmine_rais = (benz / kml�bi) * 100

        print(f"Teie keskmine rais on {keskmine_rais} L, 100km kohta. ")
except:
    print("Sisestage ainult arvud / ujukomaarvud ")


#-----------------------
#�L9
print("\n-----�L9-----")

try:
    kiirus = 29.9
    MINS = float(input("Sisestage aeg minutites (M): "))

    if MINS > 0:
        kaugus = round(kiirus * (MINS / 60), 2)
        print(f"Rulluisutaja j�uab {kaugus} km {MINS} minutiga.")
    else:
        print("Aeg peab olema positiivne arv!")
except:
    print("Palun sisestage ainult arvud!")


#-----------------------
#�L10
print("\n-----�L10-----")

try:
    MINS2 = int(input("Sisestage aeg minutites (M): "))
    if MINS2 > 0:
        tundid = MINS2 // 60
        minutid = MINS2 % 60
        print(f"Aeg on {tundid}:{minutid}")
    else:
        print("Aeg peab olema positiivne arv!")
except:
    print("Palun sisestage �iged arvud!") 