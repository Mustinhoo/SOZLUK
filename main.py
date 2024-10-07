modern_to_traditional = {
    "selfie": "kendi fotoğrafını çekmek",
    "hashtag": "bir kelimenin önüne '#' işareti eklenerek konu başlığı oluşturma",
    "influencer": "internet üzerinde başkalarını etkileyen kişi",
    "dm": "doğrudan mesaj",
    "emoji": "duyguları ifade eden küçük simgeler",
    "viral": "hızla yayılan içerik",
    "stream": "çevrimiçi içerik izlemek veya dinlemek",
    "meme": "internette hızla yayılan ve genellikle komik içerik",
    "lol": "komik bir şeye verilen cevap",
    "sheesh": "onaylamamak",
    "aggro". "agresifleşmek/sinirlenmek",

}



kelime = input("Anlamını öğrenmek istediğiniz modern kelimeyi girin: ")


if kelime in modern_to_traditional:
    print(f"'{kelime}' kelimesinin geleneksel açıklaması: {modern_to_traditional[kelime]}")
else:
    print(f"'{kelime}' için bir açıklama bulunamadı.")
