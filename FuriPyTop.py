import tkinter as tk
from personelclass import personel
from topsisclass import TOPSIS
import numpy as np
from tkinter import messagebox
from tkinter import PhotoImage



class interface_class :

    def interface():
        """ana arayüzde kapatma fonks."""
        def cikis(etkin):
            interface_.destroy()

        """  ------PERSONEL2-------- """

        def personel2():

            interface_.destroy()
            def gericagirma():
                content2.destroy()

                interface_class.interface()
            """P2 ARAYÜZ ÖZELLİKLERİ"""
            content2 = tk.Tk()
            content2.title("2 Personel ")
            content2.geometry('500x350+750+350')
            content2.resizable(width="FALSE", height="FALSE")
            content2.configure(bg="#b22222")

            "# Personel2 için gerekli label ve button imageleri"
            personel2iconfile = PhotoImage(file=".img\\2personel.png")
            anamenu2icon_label = tk.Label(content2, image=personel2iconfile)
            anamenu2icon_label.configure(bg="#b22222",cursor="hand2")
            anamenu2icon_label.place(x=150, y=50)

            personel2butonfile = PhotoImage(file=".img\\anamenuicon.png")
            anamenuicon_button = tk.Button(content2, image=personel2butonfile,command = lambda : gericagirma())
            anamenuicon_button.configure(bg="#b22222",cursor="hand2")
            anamenuicon_button.place(x=175, y=280)

            personel2hesapiconfile = PhotoImage(file=".img\\hesaplamaicon.png")
            hesapicon_button = tk.Button(content2, image=personel2hesapiconfile, command=lambda: solvecontrol2())
            hesapicon_button.configure(bg="#b22222",cursor="hand2")
            hesapicon_button.place(x=270, y=220)

            personel2temizleiconfile = PhotoImage(file=".img\\temizleicon.png")
            temizlemeicon_button = tk.Button(content2, image=personel2temizleiconfile, command=lambda: solve2cleaner())
            temizlemeicon_button.configure(bg="#b22222",cursor="hand2")
            temizlemeicon_button.place(x=80, y=220)
            "# Kriter listesi for döng. "
            kriterliste2 = []
            kriterlist2 = ["MO", "YP", "SK", "TY", "BB", "REF", "TED", "PGS", "KDS", "YSE", "OYB", "KB"]
            for i in range(len(kriterlist2)):
                kriterliste2.append(tk.Label(content2, text=kriterlist2[i], font=('Forum', 8, 'bold'), bg="#0c2a0a", fg="white"))

            sayac = 0
            for i in range(1, 13):
                kriterliste2[sayac].place(x=70 + i * 30, y=100)
                sayac += 1
            "# personel2 verileri temizleme "
            def solve2cleaner():
                a1, a2, a3, a4, a5 = a11.delete(0, tk.END), a12.delete(0, tk.END), a13.delete(0, tk.END), a14.delete(0, tk.END), a15.delete(0, tk.END)
                a6, a7, a8, a9, a1100, a1110, a11120 = a16.delete(0, tk.END), a17.delete(0, tk.END), a18.delete(0, tk.END), a19.delete(0, tk.END), a110.delete(0, tk.END), a111.delete(0,tk.END), a112.delete(0, tk.END)

                b1, b2, b3, b4, b5, b6 = a21.delete(0, tk.END), a22.delete(0, tk.END), a23.delete(0, tk.END), a24.delete(0, tk.END), a25.delete(0, tk.END), a26.delete(0, tk.END)
                b7, b8, b9, b10, b110, b112 = a27.delete(0, tk.END), a28.delete(0, tk.END), a29.delete(0, tk.END), a210.delete(0, tk.END), a211.delete(0, tk.END), a212.delete(0, tk.END)
            "# personel2 girdi kontrol fonks."
            def solvecontrol2():
                try:
                    solve2()
                except:
                    gosterge = messagebox.showerror("UYARI", "LÜTFEN GİRİŞLERİ TAM SAYI veya GİRİŞLERDEKİ EKSİKLERİ GİRİNİZ")

            def solve2():
                A11_deger, A12_deger, A13_deger, A14_deger = float(a11.get()), float(a12.get()), float(a13.get()), float(a14.get())
                A15_deger, A16_deger, A17_deger, A18_deger = float(a15.get()), float(a16.get()), float(a17.get()), float(a18.get())
                A19_deger, A110_deger, A111_deger, A112_deger = float(a19.get()), float(a110.get()), float(a111.get()), float(a112.get())

                A21_deger, A22_deger, A23_deger, A24_deger = float(a21.get()), float(a22.get()), float(a23.get()), float(a24.get())
                A25_deger, A26_deger, A27_deger, A28_deger = float(a25.get()), float(a26.get()), float(a27.get()), float(a28.get())
                A29_deger, A210_deger, A211_deger, A212_deger = float(a29.get()), float(a210.get()), float(a211.get()), float(a212.get())

                evaluation = np.array(
                    [[A11_deger, A12_deger, A13_deger, A14_deger, A15_deger, A16_deger, A17_deger, A18_deger, A19_deger,
                      A110_deger, A111_deger, A112_deger],
                     [A21_deger, A22_deger, A23_deger, A24_deger, A25_deger, A26_deger, A27_deger, A28_deger, A29_deger,
                      A210_deger, A211_deger, A212_deger]])
                weights = [0.23982, 0.23982, 0.07994, 0.03564, 0.10692, 0.10692, 0.04091, 0.01364, 0.04091, 0.01, 0.06081, 0.02466]
                criterion = np.array([True, True, True, True, True, True, True, True, True, True, True, True])
                value2 = TOPSIS(evaluation, weights, criterion)
                value2.hesaplama()

                "## Personel2 SONUÇ ÇIKTILARI"
                bilgi2 = tk.Tk()
                bilgi2.title("SONUÇLAR")
                bilgi2.geometry('300x200+850+450')
                bilgi2.configure(bg="#b22222")


                alternatiflist2 = value2.alternatifsiralamasi()
                ekranbilgi2 = tk.Label(bilgi2, text=" SONUÇ KISMI ",font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")
                ekranbilgi2.pack()
                siralamabilgisi3 = tk.Label(bilgi2, text="Personellerin sıralamaları şu şekildedir;\n "
                                                         " PERSONEL1 =>  ({}). sıradadır. \n"
                                                         " PERSONEL2 =>  ({}). sıradadır.   "

                                            .format(alternatiflist2[0], alternatiflist2[1]), font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")

                siralamabilgisi3.pack()
                def bilgi2kapatma(etkin):
                    bilgi2.destroy()
                bilgi2kapat = tk.Button(bilgi2,text="Tamam")
                bilgi2kapat.configure(cursor="hand2")
                bilgi2kapat.bind("<Button-1>", bilgi2kapatma)
                bilgi2kapat.pack()

            a11, a12, a13, a14, a15, a16 = tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3)
            a11.place(x=100, y=130), a12.place(x=130, y=130), a13.place(x=160, y=130), a14.place(x=190, y=130), a15.place(x=220, y=130), a16.place(x=250, y=130)
            a17, a18, a19, a110, a111, a112 = tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3)
            a17.place(x=280, y=130), a18.place(x=310, y=130), a19.place(x=340, y=130), a110.place(x=370, y=130), a111.place(x=400, y=130), a112.place(x=430, y=130)

            a21, a22, a23, a24, a25, a26 = tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3)
            a21.place(x=100, y=160), a22.place(x=130, y=160), a23.place(x=160, y=160), a24.place(x=190, y=160), a25.place(x=220, y=160), a26.place(x=250, y=160)
            a27, a28, a29, a210, a211, a212 = tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3), tk.Entry(content2, width=3)
            a27.place(x=280, y=160), a28.place(x=310, y=160), a29.place(x=340, y=160), a210.place(x=370, y=160), a211.place(x=400, y=160), a212.place(x=430, y=160)
            "# Personel ve kriter label buttonları "
            personelandkriter2 = tk.Button(content2, text="KRİTERLER = ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white",command = lambda :personel.kriter(),cursor="hand2").place(x=15, y=100)
            personel12 = tk.Label(content2, text="PERSONEL 1", font=('Raleway', 9, 'bold'), bg="#0c2a0a", fg="white").place(x=15, y=130)
            personel22 = tk.Label(content2, text="PERSONEL 2", font=('Raleway', 9, 'bold'), bg="#0c2a0a", fg="white").place(x=15, y=160)

            content2.mainloop()

        """  ------PERSONEL3-------- """

        def personel3():

            interface_.destroy()

            def gericagirici3():
                content3.destroy()
                interface_class.interface()
            content3 = tk.Tk()
            content3.title("3 Personel Hesaplama")
            content3.geometry('500x350+750+350')
            content3.resizable(width="FALSE", height="FALSE")
            content3.configure(bg="#b22222")

            "# Personel3 arayüzündeki gerekli label ve buttonların imageleri "
            personel3iconfile = PhotoImage(file=".img\\3personel.png")
            anamenu3icon_label = tk.Label(content3, image=personel3iconfile)
            anamenu3icon_label.configure(bg="#b22222",cursor="hand2")
            anamenu3icon_label.place(x=150, y=20)

            personel3buttonfile = PhotoImage(file=".img\\anamenuicon.png")
            anamenu3icon_button = tk.Button(content3, image=personel3buttonfile, command=lambda: gericagirici3())
            anamenu3icon_button.configure(bg="#b22222",cursor="hand2")
            anamenu3icon_button.place(x=175, y=280)

            personel3hesapiconfile = PhotoImage(file=".img\\hesaplamaicon.png")
            hesap3icon_button = tk.Button(content3, image=personel3hesapiconfile, command=lambda: solvecontrol3())
            hesap3icon_button.configure(bg="#b22222",cursor="hand2")
            hesap3icon_button.place(x=270, y=220)

            personel3temizleiconfile = PhotoImage(file=".img\\temizleicon.png")
            temizleme3icon_button = tk.Button(content3, image=personel3temizleiconfile, command=lambda: solve3cleaner())
            temizleme3icon_button.configure(bg="#b22222",cursor="hand2")
            temizleme3icon_button.place(x=80, y=220)
            "# Kriter Labelleri "
            kriterliste3 = []
            kriterlist3 = ["MO", "YP", "SK", "TY", "BB", "REF", "TED", "PGS", "KDS", "YSE", "OYB", "KB"]
            for i in range(len(kriterlist3)):
                kriterliste3.append(tk.Label(content3, text=kriterlist3[i], font=('arial', 8, 'bold'), bg="#0c2a0a", fg="white"))

            sayac = 0
            for i in range(1, 13):
                kriterliste3[sayac].place(x=70 + i * 30, y=70)
                sayac += 1
            "# Personel 3 girdileri temizleme "
            def solve3cleaner():
                a1, a2, a3, a4, a5 = a11.delete(0, tk.END), a12.delete(0, tk.END), a13.delete(0, tk.END), a14.delete(0, tk.END), a15.delete(0, tk.END)
                a6, a7, a8, a9, a1100, a1110, a11120 = a16.delete(0, tk.END), a17.delete(0, tk.END), a18.delete(0, tk.END), a19.delete(0, tk.END), a110.delete(0, tk.END), a111.delete(0,tk.END), a112.delete(0, tk.END)

                b1, b2, b3, b4, b5, b6 = a21.delete(0, tk.END), a22.delete(0, tk.END), a23.delete(0, tk.END), a24.delete(0, tk.END), a25.delete(0, tk.END), a26.delete(0, tk.END)
                b7, b8, b9, b10, b110, b112 = a27.delete(0, tk.END), a28.delete(0, tk.END), a29.delete(0, tk.END), a210.delete(0, tk.END), a211.delete(0, tk.END), a212.delete(0, tk.END)

                c1,c2,c3,c4,c5,c6 = a31.delete(0, tk.END), a32.delete(0, tk.END), a33.delete(0, tk.END), a34.delete(0, tk.END), a35.delete(0, tk.END),a36.delete(0,tk.END)
                c7,c8,c9,c110,c111,c112 =a37.delete(0, tk.END), a38.delete(0, tk.END), a39.delete(0, tk.END), a310.delete(0, tk.END), a311.delete(0, tk.END), a312.delete(0, tk.END)
            "# Personel 3 veri girdi kontrol fonksiyonu "
            def solvecontrol3():
                try:
                    solve3()
                except:
                    gosterge = messagebox.showerror("UYARI", "LÜTFEN GİRİŞLERİ TAM SAYI veya GİRİŞLERDEKİ EKSİKLERİ GİRİNİZ")
            def solve3():

                A11_deger, A12_deger, A13_deger, A14_deger = float(a11.get()), float(a12.get()), float(a13.get()), float(a14.get())
                A15_deger, A16_deger, A17_deger, A18_deger = float(a15.get()), float(a16.get()), float(a17.get()), float(a18.get())
                A19_deger, A110_deger, A111_deger, A112_deger = float(a19.get()), float(a110.get()), float(a111.get()), float(a112.get())

                A21_deger, A22_deger, A23_deger, A24_deger = float(a21.get()), float(a22.get()), float(a23.get()), float(a24.get())
                A25_deger, A26_deger, A27_deger, A28_deger = float(a25.get()), float(a26.get()), float(a27.get()), float(a28.get())
                A29_deger, A210_deger, A211_deger, A212_deger = float(a29.get()), float(a210.get()), float(a211.get()), float(a212.get())

                A31_deger, A32_deger, A33_deger, A34_deger = float(a31.get()), float(a32.get()), float(a33.get()), float(a34.get())
                A35_deger, A36_deger, A37_deger, A38_deger = float(a35.get()), float(a36.get()), float(a37.get()), float(a38.get())
                A39_deger, A310_deger, A311_deger, A312_deger = float(a39.get()), float(a310.get()), float(a311.get()), float(a312.get())

                evaluation3 = np.array(
                    [[A11_deger, A12_deger, A13_deger, A14_deger, A15_deger, A16_deger, A17_deger, A18_deger, A19_deger,
                      A110_deger, A111_deger, A112_deger],
                     [A21_deger, A22_deger, A23_deger, A24_deger, A25_deger, A26_deger, A27_deger, A28_deger, A29_deger,
                      A210_deger, A211_deger, A212_deger],
                     [A31_deger, A32_deger, A33_deger, A34_deger, A35_deger, A36_deger, A37_deger, A38_deger, A39_deger,
                      A310_deger, A311_deger, A312_deger]])
                agirlik_matrisleri3 = [0.23982, 0.23982, 0.07994, 0.03564, 0.10692, 0.10692, 0.04091, 0.01364, 0.04091, 0.01, 0.06081, 0.02466]
                kriterler3 = np.array([True, True, True, True, True, True, True, True, True, True, True, True])

                "## HESAPLAMALAR"
                value3 = TOPSIS(evaluation3, agirlik_matrisleri3, kriterler3)
                value3.hesaplama()

                "## personel3 SONUÇ ÇIKTILARI"
                bilgi3 = tk.Tk()
                bilgi3.title("SONUÇLAR")
                bilgi3.geometry('300x200+850+450')
                bilgi3.configure(bg="#b22222")
                alternatiflist3 = value3.alternatifsiralamasi()
                ekranbilgi3 = tk.Label(bilgi3, text=" SONUÇ  ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")
                ekranbilgi3.pack()
                siralamabilgisi3 = tk.Label(bilgi3, text="Personellerin sıralamaları şu şekildedir;\n "
                                                         " PERSONEL1 =>  ({}). sıradadır. \n"
                                                         " PERSONEL2 =>  ({}). sıradadır. \n"
                                                         " PERSONEL3 =>  ({}). sıradadır.   "
                                            .format(alternatiflist3[0], alternatiflist3[1], alternatiflist3[2]), font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")

                siralamabilgisi3.pack()
                def bilgi3kapatma(etkin):
                    bilgi3.destroy()
                bilgi3kapat = tk.Button(bilgi3,text="Tamam")
                bilgi3kapat.configure(cursor="hand2")
                bilgi3kapat.bind("<Button-1>", bilgi3kapatma)
                bilgi3kapat.pack()

                return A11_deger
            "# Kullanıcı girişi entryleri "
            a11, a12, a13, a14, a15, a16 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a11.place(x=100, y=100), a12.place(x=130, y=100), a13.place(x=160, y=100), a14.place(x=190, y=100), a15.place(x=220, y=100), a16.place(x=250, y=100)
            a17, a18, a19, a110, a111, a112 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a17.place(x=280, y=100), a18.place(x=310, y=100), a19.place(x=340, y=100), a110.place(x=370, y=100), a111.place(x=400, y=100), a112.place(x=430, y=100)

            a21, a22, a23, a24, a25, a26 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a21.place(x=100, y=130), a22.place(x=130, y=130), a23.place(x=160, y=130), a24.place(x=190, y=130), a25.place(x=220, y=130), a26.place(x=250, y=130)
            a27, a28, a29, a210, a211, a212 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a27.place(x=280, y=130), a28.place(x=310, y=130), a29.place(x=340, y=130), a210.place(x=370, y=130), a211.place(x=400, y=130), a212.place(x=430, y=130)

            a31, a32, a33, a34, a35, a36 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a31.place(x=100, y=160), a32.place(x=130, y=160), a33.place(x=160, y=160), a34.place(x=190, y=160), a35.place(x=220, y=160), a36.place(x=250, y=160)
            a37, a38, a39, a310, a311, a312 = tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(content3, width=3), tk.Entry(
                content3, width=3)
            a37.place(x=280, y=160), a38.place(x=310, y=160), a39.place(x=340, y=160), a310.place(x=370, y=160), a311.place(x=400, y=160), a312.place(x=430, y=160)
            "# Personel giriş labelleri"
            personel13 = tk.Label(content3, text="Personel1 ", font=('arial', 9, 'bold'), bg="#0c2a0a", fg="white").place(x=15, y=100)
            personel23 = tk.Label(content3, text="Personel2 ", font=('arial', 9, 'bold'), bg="#0c2a0a", fg="white").place(x=15, y=130)
            personel33 = tk.Label(content3, text="Personel3 ", font=('arial', 9, 'bold'), bg="#0c2a0a", fg="white").place(x=15, y=160)
            personelandkriter3 = tk.Button(content3, text="KRİTERLER = ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white", command=lambda: personel.kriter(),cursor="hand2").place(x=15, y=70)

            content3.mainloop()

        """---- PERSONEL 4 -- fonksiyonu"""

        def personel4():

            interface_.destroy()

            def gericagirici4():
                content4.destroy()
                interface_class.interface()

            content4 = tk.Tk()
            content4.title("4 Personel Hesaplama")
            content4.geometry('500x400+750+350')
            content4.resizable(width="FALSE", height="FALSE")
            content4.configure(bg="#b22222")

            " # Personel4 için gerekli label ve button imageleri"
            personel4iconfile = PhotoImage(file=".img\\4personel.png")
            anamenu4icon_label = tk.Label(content4, image=personel4iconfile)
            anamenu4icon_label.configure(bg="#b22222",cursor="hand2")
            anamenu4icon_label.place(x=150, y=20)

            personel4buttonfile = PhotoImage(file=".img\\anamenuicon.png")
            anamenu4icon_button = tk.Button(content4, image=personel4buttonfile, command=lambda: gericagirici4())
            anamenu4icon_button.configure(bg="#b22222",cursor="hand2")
            anamenu4icon_button.place(x=175, y=300)

            personel4hesapiconfile = PhotoImage(file=".img\\hesaplamaicon.png")
            hesap4icon_button = tk.Button(content4, image=personel4hesapiconfile, command=lambda: solvecontrol4())
            hesap4icon_button.configure(bg="#b22222",cursor="hand2")
            hesap4icon_button.place(x=270, y=240)

            personel4temizleiconfile = PhotoImage(file=".img\\temizleicon.png")
            temizleme4icon_button = tk.Button(content4, image=personel4temizleiconfile, command=lambda: solve4cleaner())
            temizleme4icon_button.configure(bg="#b22222",cursor="hand2")
            temizleme4icon_button.place(x=80, y=240)
            "# Kriter listesi for döngüsü ile oluşumu "
            kriterliste4 = []
            kriterlist4 = ["MO", "YP", "SK", "TY", "BB", "REF", "TED", "PGS", "KDS", "YSE", "OYB", "KB"]
            for i in range(len(kriterlist4)):
                kriterliste4.append(tk.Label(content4, text=kriterlist4[i], font=('arial', 8, 'bold'), bg="#0c2a0a", fg="white"))

            sayac = 0
            for i in range(1, 13):
                kriterliste4[sayac].place(x=70 + i * 30, y=70)
                sayac += 1
            "# Personel4 ün ekran temizleme fonksiyonu "
            def solve4cleaner():
                a1, a2, a3, a4, a5 = a11.delete(0, tk.END), a12.delete(0, tk.END), a13.delete(0, tk.END), a14.delete(0, tk.END), a15.delete(0, tk.END)
                a6, a7, a8, a9, a1100, a1110, a11120 = a16.delete(0, tk.END), a17.delete(0, tk.END), a18.delete(0, tk.END), a19.delete(0, tk.END), a110.delete(0, tk.END), a111.delete(0,tk.END), a112.delete(0, tk.END)

                b1, b2, b3, b4, b5, b6 = a21.delete(0, tk.END), a22.delete(0, tk.END), a23.delete(0, tk.END), a24.delete(0, tk.END), a25.delete(0, tk.END), a26.delete(0, tk.END)
                b7, b8, b9, b10, b110, b112 = a27.delete(0, tk.END), a28.delete(0, tk.END), a29.delete(0, tk.END), a210.delete(0, tk.END), a211.delete(0, tk.END), a212.delete(0, tk.END)

                c1,c2,c3,c4,c5,c6 = a31.delete(0, tk.END), a32.delete(0, tk.END), a33.delete(0, tk.END), a34.delete(0, tk.END), a35.delete(0, tk.END),a36.delete(0,tk.END)
                c7,c8,c9,c110,c111,c112 =a37.delete(0, tk.END), a38.delete(0, tk.END), a39.delete(0, tk.END), a310.delete(0, tk.END), a311.delete(0, tk.END), a312.delete(0, tk.END)

                d1,d2,d3,d4,d5,d6 =a41.delete(0, tk.END), a42.delete(0, tk.END), a43.delete(0, tk.END), a44.delete(0, tk.END), a45.delete(0, tk.END),a46.delete(0,tk.END)
                d7,d8,d9,d110,d111,d112 = a47.delete(0, tk.END), a48.delete(0, tk.END), a49.delete(0, tk.END), a410.delete(0, tk.END), a411.delete(0, tk.END), a412.delete(0, tk.END)
            "# Kullanıcı girişleri kontrolü ve uyarı fonk. "
            def solvecontrol4():
                try:
                    solve4()
                except:
                    gosterge4 = messagebox.showerror("UYARI", "LÜTFEN GİRİŞLERİ TAM SAYI veya GİRİŞLERDEKİ EKSİKLERİ GİRİNİZ")
            def solve4():
                """Personel 4 fonksiyon """
                A11_deger, A12_deger, A13_deger, A14_deger = float(a11.get()), float(a12.get()), float(a13.get()), float(a14.get())
                A15_deger, A16_deger, A17_deger, A18_deger = float(a15.get()), float(a16.get()), float(a17.get()), float(a18.get())
                A19_deger, A110_deger, A111_deger, A112_deger = float(a19.get()), float(a110.get()), float(a111.get()), float(a112.get())

                A21_deger, A22_deger, A23_deger, A24_deger = float(a21.get()), float(a22.get()), float(a23.get()), float(a24.get())
                A25_deger, A26_deger, A27_deger, A28_deger = float(a25.get()), float(a26.get()), float(a27.get()), float(a28.get())
                A29_deger, A210_deger, A211_deger, A212_deger = float(a29.get()), float(a210.get()), float(a211.get()), float(a212.get())

                A31_deger, A32_deger, A33_deger, A34_deger = float(a31.get()), float(a32.get()), float(a33.get()), float(a34.get())
                A35_deger, A36_deger, A37_deger, A38_deger = float(a35.get()), float(a36.get()), float(a37.get()), float(a38.get())
                A39_deger, A310_deger, A311_deger, A312_deger = float(a39.get()), float(a310.get()), float(a311.get()), float(a312.get())

                A41_deger, A42_deger, A43_deger, A44_deger = float(a41.get()), float(a42.get()), float(a43.get()), float(a44.get())
                A45_deger, A46_deger, A47_deger, A48_deger = float(a45.get()), float(a46.get()), float(a47.get()), float(a45.get())
                A49_deger, A410_deger, A411_deger, A412_deger = float(a49.get()), float(a410.get()), float(a411.get()), float(a412.get())

                evaluation4 = np.array(
                    [[A11_deger, A12_deger, A13_deger, A14_deger, A15_deger, A16_deger, A17_deger, A18_deger, A19_deger,
                      A110_deger, A111_deger, A112_deger],
                     [A21_deger, A22_deger, A23_deger, A24_deger, A25_deger, A26_deger, A27_deger, A28_deger, A29_deger,
                      A210_deger, A211_deger, A212_deger],
                     [A31_deger, A32_deger, A33_deger, A34_deger, A35_deger, A36_deger, A37_deger, A38_deger, A39_deger,
                      A310_deger, A311_deger, A312_deger],
                     [A41_deger, A42_deger, A43_deger, A44_deger, A45_deger, A46_deger, A47_deger, A48_deger, A49_deger,
                      A410_deger, A411_deger, A412_deger]
                     ])
                weights4 = [0.23982, 0.23982, 0.07994, 0.03564, 0.10692, 0.10692, 0.04091, 0.01364, 0.04091, 0.01, 0.06081, 0.02466]
                criterion4 = np.array([True, True, True, True, True, True, True, True, True, True, True, True])
                value4 = TOPSIS(evaluation4, weights4, criterion4)
                value4.hesaplama()

                "Personel sıralamasının yapıldığı pencere"
                bilgi4 = tk.Tk()
                bilgi4.title("SONUÇLAR")
                bilgi4.geometry('300x200+850+450')
                bilgi4.configure(bg="#b22222")
                alternatiflist4 = value4.alternatifsiralamasi()
                ekranbilgi4 = tk.Label(bilgi4, text=" SONUÇ ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")
                ekranbilgi4.pack()
                siralamabilgisi4 = tk.Label(bilgi4, text="Personellerin sıralamaları şu şekildedir;\n "
                                                         " PERSONEL1 =>  ({}). sıradadır. \n"
                                                         " PERSONEL2 =>  ({}). sıradadır. \n"
                                                         " PERSONEL3 =>  ({}). sıradadır. \n"
                                                         " PERSONEL4 =>  ({}). sıradadır.  "
                                                         .format(alternatiflist4[0], alternatiflist4[1], alternatiflist4[2], alternatiflist4[3]), font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")

                siralamabilgisi4.pack()
                def bilgi4kapatma(etkin):
                    bilgi4.destroy()
                bilgi4kapat = tk.Button(bilgi4,text="Tamam")
                bilgi4kapat.configure(cursor="hand2")
                bilgi4kapat.bind("<Button-1>", bilgi4kapatma)
                bilgi4kapat.pack()

                return A11_deger
            "#Kullanıcı girişi için açılan entryler"
            a11, a12, a13, a14, a15, a16 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a11.place(x=100, y=100), a12.place(x=130, y=100), a13.place(x=160, y=100), a14.place(x=190, y=100), a15.place(x=220, y=100), a16.place(x=250, y=100)
            a17, a18, a19, a110, a111, a112 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a17.place(x=280, y=100), a18.place(x=310, y=100), a19.place(x=340, y=100), a110.place(x=370, y=100), a111.place(x=400, y=100), a112.place(x=430, y=100)
            a21, a22, a23, a24, a25, a26 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a21.place(x=100, y=130), a22.place(x=130, y=130), a23.place(x=160, y=130), a24.place(x=190, y=130), a25.place(x=220, y=130), a26.place(x=250, y=130)
            a27, a28, a29, a210, a211, a212 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a27.place(x=280, y=130), a28.place(x=310, y=130), a29.place(x=340, y=130), a210.place(x=370, y=130), a211.place(x=400, y=130), a212.place(x=430, y=130)
            a31, a32, a33, a34, a35, a36 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a31.place(x=100, y=160), a32.place(x=130, y=160), a33.place(x=160, y=160), a34.place(x=190, y=160), a35.place(x=220, y=160), a36.place(x=250, y=160)
            a37, a38, a39, a310, a311, a312 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a37.place(x=280, y=160), a38.place(x=310, y=160), a39.place(x=340, y=160), a310.place(x=370, y=160), a311.place(x=400, y=160), a312.place(x=430, y=160)
            a41, a42, a43, a44, a45, a46 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a41.place(x=100, y=190), a42.place(x=130, y=190), a43.place(x=160, y=190), a44.place(x=190, y=190), a45.place(x=220, y=190), a46.place(x=250, y=190)
            a47, a48, a49, a410, a411, a412 = tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3), tk.Entry(content4, width=3)
            a47.place(x=280, y=190), a48.place(x=310, y=190), a49.place(x=340, y=190), a410.place(x=370, y=190), a411.place(x=400, y=190), a412.place(x=430, y=190)

            "# Personel satirlarinin labelleri"
            personel41 = tk.Label(content4, text="PERSONEL 1 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=100)
            personel42 = tk.Label(content4, text="PERSONEL 2 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=130)
            personel43 = tk.Label(content4, text="PERSONEL 3 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=160)
            personel44 = tk.Label(content4, text="PERSONEL 4 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=190)
            personelandkriter4 = tk.Button(content4, text="KRİTERLER = ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white", command=lambda: personel.kriter(),cursor="hand2").place(x=15, y=70)
            content4.mainloop()

        """--PERSONEL 5 FONK ------"""

        def personel5():
            interface_.destroy()

            def gericagirici5():
                content5.destroy()
                interface_class.interface()
            "# Personel 5in arayüzü"
            content5 = tk.Tk()
            content5.title("5 Personel Hesaplama")
            content5.geometry('500x400+750+350')
            content5.resizable(width="FALSE", height="FALSE")
            content5.configure(bg="#b22222")


            "# Ekrandaki label ve butonların image girişleri"
            personel5iconfile = PhotoImage(file=".img\\5personel.png")
            anamenu5icon_label = tk.Label(content5, image=personel5iconfile)
            anamenu5icon_label.configure(bg="#b22222",cursor="hand2")
            anamenu5icon_label.place(x=150, y=20)

            personel5buttonfile = PhotoImage(file=".img\\anamenuicon.png")
            anamenu5icon_button = tk.Button(content5, image=personel5buttonfile, command=lambda: gericagirici5())
            anamenu5icon_button.configure(bg="#b22222",cursor="hand2")
            anamenu5icon_button.place(x=175, y=330)

            personel5hesapiconfile = PhotoImage(file=".img\\hesaplamaicon.png")
            hesap5icon_button = tk.Button(content5, image=personel5hesapiconfile, command=lambda: solvecontrol5())
            hesap5icon_button.configure(bg="#b22222",cursor="hand2")
            hesap5icon_button.place(x=270, y=270)

            personel5temizleiconfile = PhotoImage(file=".img\\temizleicon.png")
            temizleme5icon_button = tk.Button(content5, image=personel5temizleiconfile, command=lambda: solve5cleaner())
            temizleme5icon_button.configure(bg="#b22222",cursor="hand2")
            temizleme5icon_button.place(x=80, y=270)
            "# Kriter labellerinin for döngüsü "
            kriterliste5 = []
            kriterlist5 = ["MO", "YP", "SK", "TY", "BB", "REF", "TED", "PGS", "KDS", "YSE", "OYB", "KB"]
            for i in range(len(kriterlist5)):
                kriterliste5.append(tk.Label(content5, text=kriterlist5[i], font=('arial', 8, 'bold'), fg = "white",bg="#0c2a0a"))

            sayac = 0
            for i in range(1, 13):
                kriterliste5[sayac].place(x=70 + i * 30, y=70)
                sayac += 1

            "# Alınan verilerin temizleme fonksiyonu "
            def solve5cleaner():
                a1, a2, a3, a4, a5 = a11.delete(0, tk.END), a12.delete(0, tk.END), a13.delete(0, tk.END), a14.delete(0, tk.END), a15.delete(0, tk.END)
                a6, a7, a8, a9, a1100, a1110, a11120 = a16.delete(0, tk.END), a17.delete(0, tk.END), a18.delete(0, tk.END), a19.delete(0, tk.END), a110.delete(0, tk.END), a111.delete(0,tk.END), a112.delete(0, tk.END)

                b1, b2, b3, b4, b5, b6 = a21.delete(0, tk.END), a22.delete(0, tk.END), a23.delete(0, tk.END), a24.delete(0, tk.END), a25.delete(0, tk.END), a26.delete(0, tk.END)
                b7, b8, b9, b10, b110, b112 = a27.delete(0, tk.END), a28.delete(0, tk.END), a29.delete(0, tk.END), a210.delete(0, tk.END), a211.delete(0, tk.END), a212.delete(0, tk.END)

                c1,c2,c3,c4,c5,c6 = a31.delete(0, tk.END), a32.delete(0, tk.END), a33.delete(0, tk.END), a34.delete(0, tk.END), a35.delete(0, tk.END),a36.delete(0,tk.END)
                c7,c8,c9,c110,c111,c112 =a37.delete(0, tk.END), a38.delete(0, tk.END), a39.delete(0, tk.END), a310.delete(0, tk.END), a311.delete(0, tk.END), a312.delete(0, tk.END)

                d1,d2,d3,d4,d5,d6 =a41.delete(0, tk.END), a42.delete(0, tk.END), a43.delete(0, tk.END), a44.delete(0, tk.END), a45.delete(0, tk.END),a46.delete(0,tk.END)
                d7,d8,d9,d110,d111,d112 = a47.delete(0, tk.END), a48.delete(0, tk.END), a49.delete(0, tk.END), a410.delete(0, tk.END), a411.delete(0, tk.END), a412.delete(0, tk.END)

                e1,e2,e3,e4,e5,e6 =a51.delete(0, tk.END), a52.delete(0, tk.END), a53.delete(0, tk.END), a54.delete(0, tk.END), a55.delete(0, tk.END),a56.delete(0,tk.END)
                e7,e8,e9,e110,e111,e112 =a57.delete(0, tk.END), a58.delete(0, tk.END), a59.delete(0, tk.END), a510.delete(0, tk.END), a511.delete(0, tk.END), a512.delete(0, tk.END)

            # Kontrol Yeri
            def solvecontrol5():

                try:
                    solve5()
                except:
                    gosterge5 = messagebox.showerror("UYARI", "LÜTFEN GİRİŞLERİ TAM SAYI veya GİRİŞLERDEKİ EKSİKLERİ GİRİNİZ")

            def solve5():
                "# Topsis için gerekli girişlerin alınması"
                A11_deger, A12_deger, A13_deger, A14_deger = float(a11.get()), float(a12.get()), float(a13.get()), float(a14.get())
                A15_deger, A16_deger, A17_deger, A18_deger = float(a15.get()), float(a16.get()), float(a17.get()), float(a18.get())
                A19_deger, A110_deger, A111_deger, A112_deger = float(a19.get()), float(a110.get()), float(a111.get()), float(a112.get())

                A21_deger, A22_deger, A23_deger, A24_deger = float(a21.get()), float(a22.get()), float(a23.get()), float(a24.get())
                A25_deger, A26_deger, A27_deger, A28_deger = float(a25.get()), float(a26.get()), float(a27.get()), float(a28.get())
                A29_deger, A210_deger, A211_deger, A212_deger = float(a29.get()), float(a210.get()), float(a211.get()), float(a212.get())

                A31_deger, A32_deger, A33_deger, A34_deger = float(a31.get()), float(a32.get()), float(a33.get()), float(a34.get())
                A35_deger, A36_deger, A37_deger, A38_deger = float(a35.get()), float(a36.get()), float(a37.get()), float(a38.get())
                A39_deger, A310_deger, A311_deger, A312_deger = float(a39.get()), float(a310.get()), float(a311.get()), float(a312.get())

                A41_deger, A42_deger, A43_deger, A44_deger = float(a41.get()), float(a42.get()), float(a43.get()), float(a44.get())
                A45_deger, A46_deger, A47_deger, A48_deger = float(a45.get()), float(a46.get()), float(a47.get()), float(a45.get())
                A49_deger, A410_deger, A411_deger, A412_deger = float(a49.get()), float(a410.get()), float(a411.get()), float(a412.get())

                A51_deger, A52_deger, A53_deger, A54_deger = float(a51.get()), float(a52.get()), float(a53.get()), float(a54.get())
                A55_deger, A56_deger, A57_deger, A58_deger = float(a55.get()), float(a56.get()), float(a57.get()), float(a55.get())
                A59_deger, A510_deger, A511_deger, A512_deger = float(a59.get()), float(a510.get()), float(a511.get()), float(a512.get())

                evaluation5 = np.array(
                    [[A11_deger, A12_deger, A13_deger, A14_deger, A15_deger, A16_deger, A17_deger, A18_deger, A19_deger,
                      A110_deger, A111_deger, A112_deger],
                     [A21_deger, A22_deger, A23_deger, A24_deger, A25_deger, A26_deger, A27_deger, A28_deger, A29_deger,
                      A210_deger, A211_deger, A212_deger],
                     [A31_deger, A32_deger, A33_deger, A34_deger, A35_deger, A36_deger, A37_deger, A38_deger, A39_deger,
                      A310_deger, A311_deger, A312_deger],
                     [A41_deger, A42_deger, A43_deger, A44_deger, A45_deger, A46_deger, A47_deger, A48_deger, A49_deger,
                      A410_deger, A411_deger, A412_deger],
                     [A51_deger, A52_deger, A53_deger, A54_deger, A55_deger, A56_deger, A57_deger, A58_deger, A59_deger,
                      A510_deger, A511_deger, A512_deger]
                     ])
                weights5 = [0.23982, 0.23982, 0.07994, 0.03564, 0.10692, 0.10692, 0.04091, 0.01364, 0.04091, 0.01, 0.06081, 0.02466]
                criterion5 = np.array([True, True, True, True, True, True, True, True, True, True, True, True])
                value5 = TOPSIS(evaluation5, weights5, criterion5)
                value5.hesaplama()

                # Personellerin sıralama yerleri
                bilgi5 = tk.Tk()
                bilgi5.title("SONUÇLAR")
                bilgi5.geometry('300x200+850+450')
                bilgi5.configure(bg="#b22222")
                alternatiflist5 = value5.alternatifsiralamasi()
                ekranbilgi5 = tk.Label(bilgi5, text=" SONUÇ  ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")
                ekranbilgi5.pack()
                siralamabilgisi5 = tk.Label(bilgi5, text="Sıralama şu şekildedir;\n "
                                                         " PERSONEL1 =>  ({}). sıradadır. \n"
                                                         " PERSONEL2 =>  ({}). sıradadır. \n"
                                                         " PERSONEL3 =>  ({}). sıradadır. \n"
                                                         " PERSONEL4 =>  ({}). sıradadır. \n"
                                                         " PERSONEL5 =>  ({}). sıradadır."
                                                         ".".format(alternatiflist5[0], alternatiflist5[1], alternatiflist5[2], alternatiflist5[3],alternatiflist5[4]), font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white")
                siralamabilgisi5.pack()
                def bilgi5kapatma(etkin):
                    bilgi5.destroy()
                bilgi5kapat = tk.Button(bilgi5,text="Tamam")
                bilgi5kapat.configure(cursor="hand2")
                bilgi5kapat.bind("<Button-1>", bilgi5kapatma)
                bilgi5kapat.pack()

                return A11_deger
            """Kullanıcıdan alınan girişler"""
            a11, a12, a13, a14, a15, a16 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a11.place(x=100, y=100), a12.place(x=130, y=100), a13.place(x=160, y=100), a14.place(x=190, y=100), a15.place(x=220, y=100), a16.place(x=250, y=100)
            a17, a18, a19, a110, a111, a112 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a17.place(x=280, y=100), a18.place(x=310, y=100), a19.place(x=340, y=100), a110.place(x=370, y=100), a111.place(x=400, y=100), a112.place(x=430, y=100)

            a21, a22, a23, a24, a25, a26 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a21.place(x=100, y=130), a22.place(x=130, y=130), a23.place(x=160, y=130), a24.place(x=190, y=130), a25.place(x=220, y=130), a26.place(x=250, y=130)
            a27, a28, a29, a210, a211, a212 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a27.place(x=280, y=130), a28.place(x=310, y=130), a29.place(x=340, y=130), a210.place(x=370, y=130), a211.place(x=400, y=130), a212.place(x=430, y=130)

            a31, a32, a33, a34, a35, a36 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a31.place(x=100, y=160), a32.place(x=130, y=160), a33.place(x=160, y=160), a34.place(x=190, y=160), a35.place(x=220, y=160), a36.place(x=250, y=160)
            a37, a38, a39, a310, a311, a312 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a37.place(x=280, y=160), a38.place(x=310, y=160), a39.place(x=340, y=160), a310.place(x=370, y=160), a311.place(x=400, y=160), a312.place(x=430, y=160)

            a41, a42, a43, a44, a45, a46 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a41.place(x=100, y=190), a42.place(x=130, y=190), a43.place(x=160, y=190), a44.place(x=190, y=190), a45.place(x=220, y=190), a46.place(x=250, y=190)
            a47, a48, a49, a410, a411, a412 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a47.place(x=280, y=190), a48.place(x=310, y=190), a49.place(x=340, y=190), a410.place(x=370, y=190), a411.place(x=400, y=190), a412.place(x=430, y=190)

            a51, a52, a53, a54, a55, a56 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a51.place(x=100, y=220), a52.place(x=130, y=220), a52.place(x=130, y=220), a53.place(x=160, y=220), a54.place(x=190, y=220), a55.place(x=220, y=220), a56.place(x=250, y=220)
            a57, a58, a59, a510, a511, a512 = tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3), tk.Entry(content5, width=3)
            a57.place(x=280, y=220), a58.place(x=310, y=220), a59.place(x=340, y=220), a510.place(x=370, y=220), a511.place(x=400, y=220), a512.place(x=430, y=220)
            "Personel yazı labelleri"
            personel15 = tk.Label(content5, text="PERSONEL 1 ", font=('arial', 9, 'bold'),fg = "white",bg="#0c2a0a").place(x=15, y=100)
            personel25 = tk.Label(content5, text="PERSONEL 2 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=130)
            personel35 = tk.Label(content5, text="PERSONEL 3 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=160)
            personel45 = tk.Label(content5, text="PERSONEL 4 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=190)
            personel55 = tk.Label(content5, text="PERSONEL 5 ", font=('arial', 9, 'bold'), fg = "white",bg="#0c2a0a").place(x=15, y=220)
            personelandkriter5 = tk.Button(content5, text="KRİTERLER = ", font=('Raleway', 8, 'bold'), bg="#0c2a0a", fg="white", command=lambda: personel.kriter(),cursor="hand2").place(x=15, y=70)
            content5.mainloop()

        """  ARAYÜZ """
        interface_ = tk.Tk()
        interface_.title('FuriPyTop ')
        interface_.geometry('450x500+750+350')
        interface_.configure(background='#b22222')
        interface_.resizable(False,False)
        "# Arayüz buton resimleri"
        filename = PhotoImage(file=".img\\furiana2.png")
        background_label = tk.Label(interface_, image=filename)
        background_label.pack()
        personel2hesapiconfile = PhotoImage(file=".img\\2personel.png")
        anamenui2hesapcon_ = tk.Button(interface_, image=personel2hesapiconfile, command=lambda: personel2())
        anamenui2hesapcon_.configure(bg="#b22222",cursor="hand2")
        anamenui2hesapcon_.place(x=120, y=240)

        personel3hesapiconfile = PhotoImage(file=".img\\3personel.png")
        anamenui3hesapcon_ = tk.Button(interface_, image=personel3hesapiconfile, command=lambda: personel3())
        anamenui3hesapcon_.configure(bg="#b22222",cursor="hand2")
        anamenui3hesapcon_.place(x=120, y=280)

        personel4hesapiconfile = PhotoImage(file=".img\\4personel.png")
        anamenui4hesapcon_ = tk.Button(interface_, image=personel4hesapiconfile, command=lambda: personel4())
        anamenui4hesapcon_.configure(bg="#b22222",cursor="hand2")
        anamenui4hesapcon_.place(x=120, y=320)

        personel5hesapiconfile = PhotoImage(file=".img\\5personel.png")
        anamenui5hesapcon_ = tk.Button(interface_, image=personel5hesapiconfile, command=lambda: personel5())
        anamenui5hesapcon_.configure(bg="#b22222",cursor="hand2")
        anamenui5hesapcon_.place(x=120, y=360)

        iletisimbutonfile = PhotoImage(file=".img\\iletisim.png")
        iletisimbuton = tk.Button(interface_, image=iletisimbutonfile, command=lambda: personel.iletisim())
        iletisimbuton.configure(bg="#b22222",cursor="hand2")
        iletisimbuton.place(x=300, y=410)

        kullanimbutonfile = PhotoImage(file=".img\\kilavuz.png")
        kullanimbuton = tk.Button(interface_, image=kullanimbutonfile, command=lambda: personel.information())
        kullanimbuton.configure(bg="#b22222",cursor="hand2")
        kullanimbuton.place(x=50, y=410)

        cikisbutonfile = PhotoImage(file=".img\\cikis.png")
        cikisbuton = tk.Button(interface_, image=cikisbutonfile)
        cikisbuton.configure(bg="#b22222",cursor="hand2")
        cikisbuton.place(x=175, y=430)
        cikisbuton.bind("<Button-1>", cikis)

        interface_.mainloop()
        """  ARAYÜZ """


interface_class.interface()