import random
isimler=["duygu","özge","betül","ali","merve","metin"]

def hediye_cekilisi():
    alanlar=isimler.copy()
    verenler=isimler.copy()
    
    alici_index=random.randint(0,len(alanlar - 1))
    verici_index=random.randint(0,len(verenler - 1))

    print(alici_index,"Şu kişiye hediye alacak:",verici_index)