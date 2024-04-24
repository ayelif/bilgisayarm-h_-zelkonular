def tersine_cevir(metin):
    return metin[::-1]

def zigzag_desenine_yaz(metin, satir_sayisi):
    desen = [''] * satir_sayisi
    satir = 0
    yon = 1

    for harf in metin:
        desen[satir] += harf
        satir += yon

        if satir == satir_sayisi - 1:
            yon = -1
        elif satir == 0:
            yon = 1

    return ''.join(desen)

def zigzag_sifrele_ve_ters_cevir(metin, satir_sayisi):
    sifreli_metin = zigzag_desenine_yaz(metin, satir_sayisi)
    ters_metin = tersine_cevir(sifreli_metin)
    return sifreli_metin, ters_metin

def zigzag_sifreyi_coz(sifreli_metin):
    satir_sayisi = int(input("Zigzag deseninde kaç satır kullanıldığını girin: "))
    ters_metin = tersine_cevir(sifreli_metin)
    duz_metin = ''
    boyut = len(ters_metin)
    matris = [['' for _ in range(boyut)] for _ in range(satir_sayisi)]

    satir, sira = 0, 0

    for harf in ters_metin:
        if satir == 0:
            asagi_yon = True
        elif satir == satir_sayisi - 1:
            asagi_yon = False

        matris[satir][sira] = '*'
        sira += 1

        if asagi_yon:
            satir += 1
        else:
            satir -= 1

    index = 0
    for i in range(satir_sayisi):
        for j in range(boyut):
            if matris[i][j] == '*':
                matris[i][j] = ters_metin[index]
                index += 1

    for j in range(boyut):
        for i in range(satir_sayisi):
            if matris[i][j] != '':
                duz_metin += matris[i][j]

    return duz_metin


metin = input("Lütfen şifrelemek veya çözmek istediğiniz metni girin: ")
secenek = input("Şifrelemek için '1', çözmek için '2' girin: ")

if secenek == '1':
    satir_sayisi = int(input("Zigzag deseninde kaç satır kullanmak istediğinizi girin: "))
    sifreli_metin, ters_metin = zigzag_sifrele_ve_ters_cevir(metin, satir_sayisi)
    print("Şifreli Metin: ", ters_metin)
elif secenek == '2':
    cozulmus_metin = zigzag_sifreyi_coz(metin)
    print("Çözülmüş Metin: ", cozulmus_metin)
else:
    print("Geçersiz seçenek.")




