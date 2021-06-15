import tkinter as tk

class personel:
    def information():
        information1 = tk.Tk()
        information1.title("Kılavuz")
        information1.geometry('500x500+650+350')
        information1.resizable(width="FALSE", height="FALSE")
        information1.configure(background='white')
        def cikis_yap():
            information1.destroy()

        information_label = tk.Label(information1,text="Kullanım Amacı",bg="white",fg="red",font=('Formul',9,'bold')).pack()

        information_label2 = tk.Label(information1,text="FuriPyTop ağırlıkları ÇKKV yöntemlerinden AHP yöntemi kullanılarak\n"
                                                       "elde edilmiş ağırlıkları, personel alımı sırasında kararsızlık yaşanan\n"
                                                       "veya birbirine yakın personeller arasında seçim yapılmasında TOPSIS yöntemi\n"
                                                       "ile farklı bir bakış açısı katmak için tasarlanmıştır. ",
                                      bg ="white",fg="black",font=('Formul',9,'bold')).pack()

        information_label3 = tk.Label(information1, text="Kullanım Adımları", bg="white", fg="red", font=('Formul', 9, 'bold')).pack()

        information_label4 = tk.Label(information1, text="Adım 1 : Personel sayısına göre alternatif hesaplama butonuna tıkla.\n"
                                                         "Adım 2 : Karşına gelen pencere de, alternatif personellerin karşılarına\n kriterlerine göre puan gir.\n"
                                                         "Adım 3 : Kriter puanlarını girdikten sonra hesapla tuşuna bas, sonuç ekranını\n karşına gelecektir.\n"
                                                         "",
                                      bg="white", fg="black", font=('Formul', 9, 'bold')).pack()
        #["MO", "YP", "SK", "TY", "BB", "REF", "TED", "PGS", "KDS", "YSE", "OYB", "KB"]
        information_label5 = tk.Label(information1, text="Kriter Açılımları", bg="white", fg="red", font=('Formul', 9, 'bold')).pack()
        information_label5 = tk.Label(information1, text="MG =Mezun Olunan Okul   , YB =Yapılan Projeler  , SK = Seminer ve Klüpler\n"
                                                         "TY =Tecrübe Yılı , BB = Bilgi ve Başarı Geçmişi , REF = Referanslar\n"
                                                         "TED= Takım Uyumu, Etkili iletişim, Duyarlılık , PGS=Prezantabl ve Sosyal Olma\n"
                                                         "KDS =Kendini ve Düşüncelerini iyi ifade edebilme, YSE = Yabancı Dil Sertifika\n"
                                                         "OYB = Y. Dil Okuma ve Yazma , KB = Y. Dil Konuşma Becerisi\n"
                                                        , bg="white", fg="#0c2a0a", font=('Formul', 9, 'bold')).pack()
        information_label5 = tk.Label(information1, text=" UYARI ", bg="white", fg="red", font=('Formul', 9, 'bold')).pack()
        information_label5 = tk.Label(information1, text="Tam sayı kullanmalısınız\n"
                                                         "Kriterlere açılan pencerelerde kriterler kısmına tıkladığınızda ulaşabilirsiniz\n"
                                                         "Hatalarla ilgili iletişim kısmından dönüş yapabilirsiniz.\n", bg="white", fg="black", font=('Formul', 9, 'bold')).pack()

        quit_button  = tk.Button(information1,text="Tamam ",command=lambda: cikis_yap()).pack()
        information1.mainloop()

    def iletisim():
        iletisim = tk.Tk()
        iletisim.title("Kılavuz")
        iletisim.geometry('300x150+650+350')
        iletisim.resizable(width="FALSE", height="FALSE")
        iletisim.configure(background='white')
        def iletisimclose():
            iletisim.destroy()

        information_label = tk.Label(iletisim, text="İletişim ", bg="white", fg="red", font=('Formul', 9, 'bold')).pack()
        information_label = tk.Label(iletisim, text="Linkedin : https://www.linkedin.com/in/eerenaydin/ \n"
                                                        "Gmail : sonfurinar@gmail.com\n"
                                                        "Github : https://github.com/furinar ", bg="white", fg="black", font=('Formul', 9, 'bold')).pack()
        cikisbuttoniletisim = tk.Button(iletisim, text="Tamam ", command=lambda: iletisimclose()).pack()

        iletisim.mainloop()

    def kriter():

        kriterinfo = tk.Tk()
        kriterinfo.title("Kriter ve Puanları")
        kriterinfo.geometry('470x250+250+250')

        kriterinfo.configure(bg= "white")
        def kriterinfoclose():
            kriterinfo.destroy()

        # [0.23982, 0.23982, 0.07994, 0.03564, 0.10692, 0.10692, 0.04091, 0.01364, 0.04091, 0.01, 0.06081, 0.02466]
        kriterinfo_label = tk.Label(kriterinfo, text="MG =Mezun Olunan Okul(0.23982) \n"
                                                     " YP =Yapılan Projeler(0.23982)\n"
                                                        " SK = Seminer ve Klüpler(0.07994)\n"
                                                         "TY =Tecrübe Yılı(0.03564)\n"
                                                     " BB = Bilgi ve Başarı Geçmişi(0.10692)\n"
                                                     "  REF = Referanslar(0.10692)\n"
                                                         "TED= Takım Uyumu, Etkili iletişim, Duyarlılık(0.04091)\n"
                                                     " PGS=Prezantabl ve Sosyal Olma(0.01364)\n"
                                                         "KDS =Kendini ve Düşüncelerini iyi ifade edebilme(0.04091)\n"
                                                     " YSE = Yabancı Dil Sertifika(0.01)\n"
                                                         "OYB = Y. Dil Okuma ve Yazma(0.06081) \n"
                                                     " KB = Y. Dil Konuşma Becerisi(0.02466)\n"
                                      , bg="white", fg="#0c2a0a", font=('Formul', 9, 'bold')).pack()


        cikisbutton = tk.Button(kriterinfo, text="Tamam ", command=lambda: kriterinfoclose()).pack()

        kriterinfo.mainloop()


