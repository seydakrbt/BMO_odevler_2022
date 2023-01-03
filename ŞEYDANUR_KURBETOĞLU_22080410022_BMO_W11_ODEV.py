sinav_sonuc={'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B'],
    'cinsiyet':['K','E','E','E','K','K'],
    'matematik':[80,60,77,25,36,75],
    'turkce':[90,50,53,100,98,66],
}

count_e=0
count_k=0
matOrt_k=0
matOrt_e=0
turkceOrt=0
enYuksekTurkceNot_e=0
enYuksekTurkceNot_k=0

for i in range(len(sinav_sonuc['isim'])):
    
    if sinav_sonuc['cinsiyet'][i]=='E':
        # bu bölüm cinsiyete göre matematik ortalamasını hesaplamak için..
        count_e+=1
        matOrt_e=matOrt_e+sinav_sonuc['matematik'][i]
        #bu bölüm erkek öğrenciler arasında en yüksek türkçe notu hesaplamak için..
        turkceNot_e=sinav_sonuc['turkce'][i]
        if turkceNot_e>enYuksekTurkceNot_e:
            enYuksekTurkceNot_e=sinav_sonuc['turkce'][i]
    else:
        count_k+=1
        matOrt_k=matOrt_k+sinav_sonuc['matematik'][i]
        #bu bölüm kadın öğrenciler arasında en yüksek türkçe notu hesaplamak için..
        turkceNot_k=sinav_sonuc['turkce'][i]
        if turkceNot_k>enYuksekTurkceNot_k:
            enYuksekTurkceNot_k=sinav_sonuc['turkce'][i]
    
    # bu bölüm türkçe sınıf ortalaması hesaplamak için..
    turkceOrt=turkceOrt+sinav_sonuc['turkce'][i]
    
print("Erkek matematik ortalaması : ",matOrt_e/count_e)
print("Kadın matematik ortalaması : ",matOrt_k/count_k)
print("Türkçe dersi sınıf ortalaması : ",turkceOrt/(count_e+count_k))
print("En yüksek erkek türkçe notu : ",enYuksekTurkceNot_e)
print("En yüksek kadın türkçe notu : ",enYuksekTurkceNot_k)