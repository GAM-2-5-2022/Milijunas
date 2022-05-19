from tkinter import *

#-----------------------------------------------------------------------------------------------------------------Glavni prozor--------------------------------------------------------------------------------------------------------------

prozor_programa = Tk()

prozor_programa.geometry('1270x652+0+0')
prozor_programa.title('Tko želi biti milijunaš?')


prozor_programa.config(bg='black')

#--------------------------------------------------------------------------------------------------------------------Okviri------------------------------------------------------------------------------------------------------------------

lijevi_okvir = Frame(prozor_programa, bg = 'black')
lijevi_okvir.grid(row = 0, column = 0)

gornji_okvir = Frame(lijevi_okvir, bg = 'black')
gornji_okvir.grid()

sredisnji_okvir = Frame(lijevi_okvir, bg = 'black')
sredisnji_okvir.grid(row = 1, column = 0)

donji_okvir = Frame(lijevi_okvir)
donji_okvir.grid(row = 2, column = 0)

desni_okvir = Frame(prozor_programa)
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

#-----------------------------------------------------------------------------------------------------------------Središnji dio---------------------------------------------------------------------------------------------------------------

sredisnja_slika = PhotoImage(file = 'sredisnjaslika.png')

logo_oznaka = Label(sredisnji_okvir, image = sredisnja_slika, bg = 'black', width = 300, height = 200)
logo_oznaka.grid(row = 0, column = 0)

prozor_programa.mainloop()
