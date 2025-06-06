import random

isimler = ["duygu", "özge", "betül", "ali", "merve", "metin"]

def hediye_cekilisi():
    alanlar = isimler.copy()
    verenler = isimler.copy()
    eslesmeler = []

    while len(alanlar) > 0:
        alici = random.choice(alanlar)
        uygun_verenler = [v for v in verenler if v != alici]

        if not uygun_verenler:
            # Geçerli eşleşme mümkün olmadıysa yeniden başlat.
            print("Geçerli çekiliş yapılamadı, yeniden başlatılıyor...")
            return hediye_cekilisi()

        verici = random.choice(uygun_verenler)
        eslesmeler.append((verici, alici))
        alanlar.remove(alici)
        verenler.remove(verici)

    # Eşleşmeleri yazdır
    print("Hediye Çekilişi Sonuçları:")
    for verici, alici in eslesmeler:
        print(f"{verici} -> {alici}")

hediye_cekilisi()
