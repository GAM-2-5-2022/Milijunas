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
           'Što označava akronim WiFi?',
           'Koja računalna mreža slijedi nakon mreže PAN?',        
           'Koja je poznata izreka filozofa, fizičara i matematičara Renea Descartesa?',
           'Koji je hrvatski pisac napisao djelo Dubravka?',
           'Koji skladatelj nije bečki klasičar?',
           'Kako se zvao prvi hrvatski kralj?',
           'Koji je prvi Microsoft Office koji na datotečnom nastavku sadrži slovo x?',
           'Tko umire posljednji?',
           'Koji je programski jezik Guido van Rossum stvorio 1991 godine?',
           'Čije je djelo Google proširenje e-Dnevnik+?',
           'Kako glasi broj 78 u binarnom obliku?',
           'Tko je u hrvatskom Milijunašu jedini osvojio 1 000 000 kn?']

prva_opcija = ['MS Word','Johannes Kepler','Bill Gates','WiiFilms',
               'MAN','Cogito, ergo sum.','Ivan Bunić Vučić','W. A. Mozart',
               'Zvonimir','MS Office 2003','Strah','C++',
               'Ivan Ćilić','11000010','Mima Zidarić']

druga_opcija = ['MS PowerPoint','Isaac Newton','Steve Jobs','Wireless Film',
                'LAN','Id est.','Ivan Gundulić','J. S. Bach',
                'Branimir','MS Office XP','Požuda','JavaScript',
                'Marko Tadić','11011111','Mirjana Hrga']

treca_opcija = ['MS Excel','Georg Simon Ohm','Jeff Bezos','Wireless Fidelity',
                'WAN','Nota Bene.','Antun Kanižlić','L. van Beethoven',
                'Tomislav','MS Office 2007','Jad','Python',
                'Boris Šimić','10100001','Mira Bićanić']

cetvrta_opcija = ['MS Paint','Alessandro Volta','Elon Musk','World Finder',
                  'DAN','Ante Meridiem.','Marin Držić','J. Haydn',
                  'Zdeslav','MS Office 365','Nada','Java',
                  'Kristijan Rosandić','01001110','Mirko Miočić']
           
    
prostor_za_pitanja = Text(donji_okvir)
prostor_za_pitanja.place(x = 70, y = 10)

prozor_programa.mainloop()

