#%%
import random as rd

#a Lag en funksjon som trekker vinnertall (altså syv tall pluss ett tilleggstall).
# Tallene er fra 1–34, og ingen tall brukes to ganger. Kall funksjonen.

def trekke_vinnertall():
    vinnertall = [] 
    while len(vinnertall) < 7: #løkke som kjører til vi har 7 vinnertall i listen
        tilfeldig = rd.randint(1, 34)
        if tilfeldig not in vinnertall:
            vinnertall.append(tilfeldig)
    tilleggstall = rd.randint(1, 34)
    return vinnertall, tilleggstall


vinnertall, tilleggstall = trekke_vinnertall()

print(f"Vinnertallene er: {vinnertall}")
print(f"Tilleggstallet er: {tilleggstall}")




#b Lag en funksjon som tar inn en lottokupong (altså tallene en person har valgt ut)
#og sjekker hvor mange riktige personen har fått (sammenlign med vinnertallene du fant i a).

def lag_lottokupong():
    kupong = []
    print("Velg 7 tall mellom 1 og 34.")
    for i in range(7):
        while True:
            try:
                tall = int(input(f"Skriv inn tall {i + 1}: "))
                if 1 <= tall <= 34:
                    if tall not in kupong:
                        kupong.append(tall)
                        break
                    else:
                        print("Tallet er allerede valgt. Prøv igjen.")
                else:
                    print("Tallet må være mellom 1 og 34. Prøv igjen.")
            except ValueError:
                print("Dette er ikke et gyldig tall. Prøv igjen.")
    return kupong

kupong = lag_lottokupong()
print("Din lottokupong:", kupong)

def sjekk_lottokupong(kupong, vinnertall, tilleggstall):
    riktige_tall = 0
    for tall in kupong:
        if tall in vinnertall:
            riktige_tall += 1
    if tilleggstall in kupong:
        riktige_tall += 1
    return riktige_tall
   
#kall funksjon
riktige_antall = sjekk_lottokupong(kupong, vinnertall, tilleggstall)
print(f"Antall riktige: {riktige_antall}")



#c Lag en funksjon som genererer et antall rekker tilfeldig, basert på brukerinput. Kall funksjonen.
import random as rd

def generer_lottokuponger(antall_rekker):
    lottokuponger = [] #tom liste til alle kupongene samlet
    for x in range(antall_rekker):
        kupong = [] #en kupong
        while len(kupong) < 7: 
            tilfeldig_tall = rd.randint(1, 34)
            if tilfeldig_tall not in kupong:
                kupong.append(tilfeldig_tall)
        lottokuponger.append(kupong)
    return lottokuponger

antall_rekker = int(input("Hvor mange lottorekker vil du generere? "))
genererte_rekker = generer_lottokuponger(antall_rekker)

print(f"\n{antall_rekker} tilfeldig genererte lottorekker:")

for i, rekke in enumerate(genererte_rekker): #enumerate er en funksjon i python som gir både verdi og indeks til 
    print(f"Rekke {i + 1}: {rekke}")#hvert element i sekvensen (i, sekvens (starter på 0, derfor +1). rekke, element)

# %%
