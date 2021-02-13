class Okul():
    def __init__(self,okul_adi,okul_turu, ogretmen_sayisi, ogrenci_sayisi, sinif_sayisi, calisan_sayisi, ders_suresi):
        self.okul_adi = okul_adi
        self.okul_turu  = okul_turu
        self.ogretmen_sayisi = ogretmen_sayisi
        self.ogrenci_sayisi = ogrenci_sayisi
        self.sinif_sayisi = sinif_sayisi
        self.calisan_sayisi = calisan_sayisi
        self.ders_suresi = ders_suresi

a=Okul("19 Mayıs İlköğretim Okulu", 
"Okulun Türü = ilköğretim Okulu",
"Öğretmen Sayısı =  20",
"Öğrenci Sayısı = 300",
"Sınıf Sayısı = 15",
"Çalışan Sayısı = 5",
"Ders Süresi= 40 dk\n"
)

b=Okul("Fethiye Kemal Mumcu Anadolu Lisesi", 
"Okulun Türü = anadolu lisesi", 
"Öğretmen Sayısı = 30",
"Öğrenci Sayısı = 400",
"Sınıf Sayısı = 30",
"Çalışan Sayısı = 10",
"Ders Süresi= 50 dk\n",
)

c=Okul("Gazi Üniversitesi", 
"Okulun Türü = üniversite",
"Öğretmen Sayısı = 40",
"Öğrenci Sayısı = 500",
"Sınıf Sayısı = 45",
"Çalışan Sayısı = 15",
"Ders Süresi=1 saat")

Okullar = [a,b,c]                
for okul in Okullar:
    print(okul.okul_adi,
     okul.okul_turu,
     okul.ogretmen_sayisi,
     okul.ogrenci_sayisi, 
     okul.sinif_sayisi, 
     okul.calisan_sayisi, 
     okul.ders_suresi)

