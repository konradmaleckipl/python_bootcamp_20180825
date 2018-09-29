import tkinter


def zlacz_napisy():
    a = a_entry.get()
    b = b_entry.get()
    wynik_label.configure(text=f'Wynik: {a+b}')

def czysc_napisy():
    print(locals())
    print(globals())
    wynik_label.configure(text="Wynik: - ")


root = tkinter.Tk()
root.columnconfigure(1, weight=1)
root.title('Prosty kalkulator')

a_label = tkinter.Label(master=root, text='a')
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text='b')
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

dodaj_button = tkinter.Button(master=root, text='Dodaj', command=zlacz_napisy)
dodaj_button.grid(row=3, column=0)

czysc_button = tkinter.Button(master=root, text='Czysc napisy', command=czysc_napisy)
czysc_button.grid(row=3, column=1)

wynik_label = tkinter.Label(master=root, text='Wynik: - ')
wynik_label.grid(row=4, column=0)



root.mainloop()