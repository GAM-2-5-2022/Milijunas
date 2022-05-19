from tkinter import *


prozor_programa = Tk()

prozor_programa.geometry('1270x652+0+0')
prozor_programa.title('Tko želi biti milijunaš?')


prozor_programa.config(bg='black')

lijevi_okvir = Frame(prozor_programa)
lijevi_okvir.grid(row = 0, column = 0)

gornji_okvir = Frame(lijevi_okvir)
gornji_okvir.grid()

sredisnji_okvir = Frame(lijevi_okvir)
sredisnji_okvir.grid(row = 1, column = 0)

donji_okvir = Frame(lijevi_okvir)
donji_okvir.grid(row = 2, column = 0)

desni_okvir = Frame(prozor_programa)
desni_okvir.grid(row = 0, column = 1)

slika50_50 = PhotoImage(file = '50-50.png')

gumb50_50 = Button(gornji_okvir, image = slika50_50)
gumb50_50.grid(row = 0, column = 0)

pitaj_publiku = PhotoImage(file = 'pitajpubliku.png')

gumb_pitaj_publiku = Button(gornji_okvir, image = pitaj_publiku)
gumb_pitaj_publiku.grid(row = 0, column = 1)

joker_zovi = PhotoImage(file = 'jokerzovi.png')

gumb_joker_zovi = Button(gornji_okvir, image = joker_zovi)
gumb_joker_zovi.grid(row = 0, column = 3)


prozor_programa.mainloop()
