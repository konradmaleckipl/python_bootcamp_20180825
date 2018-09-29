import tkinter
from tkinter import messagebox

def oblicz():
    try:
        dystans = float(a_entry.get())
        spalanie = float(b_entry.get())
        cena_paliwa = float(c_entry.get())
        wynik_label.configure(text=f'Koszt przejazdu: {str((dystans/100)*spalanie*cena_paliwa)} PLN')
    except ValueError:
        messagebox.showerror('Błędne dane', 'Musisz poprawić dane wejściowe...')

def czysc_napisy():
    a_entry.delete(0, len(a_entry.get()))
    b_entry.delete(0, len(b_entry.get()))
    c_entry.delete(0, len(c_entry.get()))
    wynik_label.configure(text="Koszt przejazdu: - ")


root = tkinter.Tk()
#root.columnconfigure(1, weight=1)
root.title('Prosty kalkulator')

a_label = tkinter.Label(master=root, text='Dystans: ')
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text='Spalanie na 100km: ')
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

c_label = tkinter.Label(master=root, text='Cena paliwa za litr: ')
c_label.grid(row=2, column=0)
c_entry = tkinter.Entry(master=root)
c_entry.grid(row=2, column=1)

oblicz_button = tkinter.Button(master=root, text='Oblicz', command=oblicz)
oblicz_button.grid(row=3, column=0)

czysc_button = tkinter.Button(master=root, text='Czysc', command=czysc_napisy)
czysc_button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text='Koszt przejazdu: - ')
wynik_label.grid(row=4, column=0)



root.mainloop()