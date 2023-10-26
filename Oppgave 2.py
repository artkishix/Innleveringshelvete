#%%
ord="funksjon"
def minfunksjon(tekst):
    ord=tekst
    return ord #Sender funksjonens resultat tilbake til den som kaller på den


print(minfunksjon("Hei"))
print(ord)

#du får ikke printet ut hei to ganger fordi funksjonen ikke endrer variabelen "hei", men kun endrer den inni funksjonen. 
#ord er derfor bare lik parameter når funksjonen kjøres, og når du bare skriver print(ord), ser den bort ifra minFunksjon, den kjøres ikke og ord blir ikke lik tekst
