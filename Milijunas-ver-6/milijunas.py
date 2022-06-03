from tkinter import *

#-----------------------------------------------------------------------------------------------------------------Glavni prozor--------------------------------------------------------------------------------------------------------------

prozor_programa = Tk()

prozor_programa.geometry('1270x652+0+0')
prozor_programa.title('Tko želi biti milijunaš?')

logo_prozora = PhotoImage(file = 'sredisnjaslika.png')
prozor_programa.iconphoto(False, logo_prozora)

prozor_programa.config(bg='black')

#--------------------------------------------------------------------------------------------------------------------Okviri------------------------------------------------------------------------------------------------------------------

lijevi_okvir = Frame(prozor_programa, bg = 'black', padx = 90)
lijevi_okvir.grid(row = 0, column = 0)

gornji_okvir = Frame(lijevi_okvir, bg = 'black', pady = 15)
gornji_okvir.grid()

sredisnji_okvir = Frame(lijevi_okvir, bg = 'black', pady = 15)
sredisnji_okvir.grid(row = 1, column = 0)

donji_okvir = Frame(lijevi_okvir)
donji_okvir.grid(row = 2, column = 0)

desni_okvir = Frame(prozor_programa, bg = 'black', pady = 25, padx = 50)
desni_okvir.grid(row = 0, column = 1)

#--------------------------------------------------------------------------------------------------------------------Jokeri------------------------------------------------------------------------------------------------------------------

slika50_50 = PhotoImage(file = '50-50.png')

gumb50_50 = Button(gornji_okvir, image = slika50_50, bg = 'black', bd = 0, activebackground = 'black', width = 180, height = 80)
gumb50_50.grid(row = 0, column = 0)

pitaj_publiku = PhotoImage(file = 'pitajpubliku.png')

gumb_pitaj_publiku = Button(gornji_okvir, image = pitaj_publiku, bg = 'black', bd = 0, activebackground = 'black', width = 180, height = 80)
gumb_pitaj_publiku.grid(row = 0, column = 1)

joker_zovi = PhotoImage(file = 'jokerzovi.png')

gumb_joker_zovi = Button(gornji_okvir, image = joker_zovi, bg = 'black', bd = 0, activebackground = 'black', width = 180, height = 80)
gumb_joker_zovi.grid(row = 0, column = 2)

#----------------------------------------------------------------------------------------------------------------Središnji dio---------------------------------------------------------------------------------------------------------------

sredisnja_slika = PhotoImage(file = 'sredisnjaslika.png')

logo_oznaka = Label(sredisnji_okvir, image = sredisnja_slika, bg = 'black', width = 300, height = 200)
logo_oznaka.grid(row = 0, column = 0)

#------------------------------------------------------------------------------------------------------------------Nagrade-------------------------------------------------------------------------------------------------------------------

iznos_0_kn = PhotoImage(file = '0kn.png')

iznos_oznaka = Label(desni_okvir, image = iznos_0_kn, bg = 'black')
iznos_oznaka.grid(row = 0, column = 0)

#--------------------------------------------------------------------------------------------------------Sučelje za odabir odgovora----------------------------------------------------------------------------------------------------------

sucelje_za_odabir_odgovora = PhotoImage(file = 'okvir.png')

sucelje_za_odabir_odgovora_oznaka = Label(donji_okvir, image = sucelje_za_odabir_odgovora, bg = 'black')
sucelje_za_odabir_odgovora_oznaka.grid(row = 0, column = 0)

#------------------------------------------------------------------------------------------------------------------Pitanja-------------------------------------------------------------------------------------------------------------------

pitanja = ['Koji program ne spada u Microsoft Office paket?',
           'Kako se zove poznati fizičar kojem je na glavu pala jabuka?',
           'Tko je osnovao Microsoft?',
           'Tko je osnovao Apple?',
           'Koja računalna mreža slijedi nakon mreže PAN?',        
           'Što označava kratica N. B. u hrvatskom jeziku?',
           'Koji je hrvatski pisac napisao djelo Dubravka?',
           'Koji skladatelj nije bečki klasičar?',
           'Kako se zvao prvi hrvatski kralj?',
           'Koji je prvi Microsoft Office koji na datotečnom nastavku sadrži slovo x?',
           'Tko umire posljednji?',
           'Koji je programski jezik Guido van Rossum stvorio 1991 godine?',
           'Čije je djelo Google proširenje e-Dnevnik+?',
           'Kako glasi broj 78 u binarnom obliku?',
           'Tko je u hrvatskom Milijunašu jedini osvojio 1 000 000 kn?']

prva_opcija = ['MS Word','J. Kepler','Bill Gates','Steve',
               'MAN','Pamti dobro','I. B. Vučić','W. A. Mozart',
               'Zvonimir','MS Office 03','Strah','C++',
               'I. Ćilić','11000010','M. Zidarić']

druga_opcija = ['MS PPT','I. Newton','Steve Jobs','Alex',
                'LAN','Uči dobro','I. Gundulić','J. S. Bach',
                'Branimir','MS Office XP','Požuda','JavaScript',
                'M. Tadić','11011111','M. Hrga']

treca_opcija = ['MS Excel','G. S. Ohm','Jeff Bezos','Steve Jobs',
                'WAN','Budi dobro','A. Kanižlić','L. van B.',
                'Tomislav','MS Office 07','Jad','Python',
                'B. Šimić','10100001','M. Bićanić']

cetvrta_opcija = ['MS Paint','A. Volta','Elon Musk','Herobrine',
                  'DAN','Čitaj dobro','M. Držić','J. Haydn',
                  'Zdeslav','MS Office 365','Nada','Java',
                  'K. Rosandić','01001110','M. Miočić']

tocni_odgovori =['MS Paint','I. Newton','Bill Gates','Steve Jobs',
                 'LAN','Pamti dobro','I. Gundulić','J. S. Bach',
                 'Tomislav','MS Office 07','Nada','Python',
                 'K. Rosandić','01001110','M. Bićanić']

           
#-----------------------------------------------------------------------------------------------------------Prostor za pitanja----------------------------------------------------------------------------------------------------------------

prostor_za_pitanja = Text(donji_okvir, font = ('arial', 18, 'bold'), width = 34, height = 2, wrap = 'word', bg = 'black', fg = 'white', bd = 0)
prostor_za_pitanja.place(x = 70, y = 10)

prostor_za_pitanja.insert(END, pitanja[0])

#Prva opcija

opcija_A = Label(donji_okvir, text = 'A:', bg = 'black', fg = 'white', font = ('arial',16, 'bold'))

opcija_A.place(x = 60, y = 110)


prva_opcija_gumb = Button(donji_okvir, text = prva_opcija[0], font = ('arial',18, 'bold'), bg = 'black', fg = 'white', bd = 0, activebackground = 'black', activeforeground = 'white', cursor = 'hand2')
prva_opcija_gumb.place(x = 100, y = 100)


#Druga opcija

opcija_B = Label(donji_okvir, text = 'B:', bg = 'black', fg = 'white', font = ('arial',16, 'bold'))

opcija_B.place(x = 330, y = 110)


druga_opcija_gumb = Button(donji_okvir, text = druga_opcija[0], font = ('arial',18, 'bold'), bg = 'black', fg = 'white', bd = 0, activebackground = 'black', activeforeground = 'white', cursor = 'hand2')
druga_opcija_gumb.place(x = 370, y = 100)


#Treća opcija

opcija_C = Label(donji_okvir, text = 'C:', bg = 'black', fg = 'white', font = ('arial',16, 'bold'))

opcija_C.place(x = 60, y = 190)


treca_opcija_gumb = Button(donji_okvir, text = treca_opcija[0], font = ('arial',18, 'bold'), bg = 'black', fg = 'white', bd = 0, activebackground = 'black', activeforeground = 'white', cursor = 'hand2')
treca_opcija_gumb.place(x = 100, y = 180)


#Četvrta opcija

opcija_D = Label(donji_okvir, text = 'D:', bg = 'black', fg = 'white', font = ('arial',16, 'bold'))

opcija_D.place(x = 330, y = 190)


cetvrta_opcija_gumb = Button(donji_okvir, text = cetvrta_opcija[0], font = ('arial',18, 'bold'), bg = 'black', fg = 'white', bd = 0, activebackground = 'black', activeforeground = 'white', cursor = 'hand2')
cetvrta_opcija_gumb.place(x = 370, y = 180)

def opcija(dogadaj):

    b = dogadaj.widget
    vrijednost = b['text']
    
    for i in range(15):
        if vrijednost == tocni_odgovori[i]:
            prostor_za_pitanja.delete(1.0, END)
            prostor_za_pitanja.insert(END, pitanja[i+1])

            prva_opcija_gumb.config(text = prva_opcija[i+1])
            druga_opcija_gumb.config(text = druga_opcija[i+1])
            treca_opcija_gumb.config(text = treca_opcija[i+1])
            cetvrta_opcija_gumb.config(text = cetvrta_opcija[i+1])



    
prva_opcija_gumb.bind('<Button-1>', opcija)
druga_opcija_gumb.bind('<Button-1>', opcija)
treca_opcija_gumb.bind('<Button-1>', opcija)
cetvrta_opcija_gumb.bind('<Button-1>', opcija)






prozor_programa.mainloop()

