import tkinter as tk

def pritisnuto(dugme):
    global izraz
    izraz = izraz + str(dugme)
    polje.set(izraz)

def izracunaj():
    global izraz
    try:
        rezultat = str(eval(izraz))
        polje.set(rezultat)
        izraz = rezultat
    except:
        polje.set("Greška")
        izraz = ""

def obrisi():
    global izraz
    izraz = ""
    polje.set("")

# Kreiraj Tkinter prozor
prozor = tk.Tk()
prozor.title("Kalkulator")

izraz = ""

# Kreiraj StringVar za prikaz rezultata
polje = tk.StringVar()

# Kreiraj Entry polje za prikaz rezultata
rezultat_polje = tk.Entry(prozor, textvariable=polje, font=("Arial", 18), bd=5, insertwidth=4, width=20, justify="right")
rezultat_polje.grid(row=0, column=0, columnspan=4)

# Definiraj dugmadi za brojeve i operacije
dugmadi = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Kreiraj dugmadi
for (simbol, red, kolona) in dugmadi:
    tk.Button(prozor, text=simbol, font=("Arial", 18), command=lambda s=simbol: pritisnuto(s)).grid(row=red, column=kolona)

# Dugme za brisanje
tk.Button(prozor, text='C', font=("Arial", 18), command=obrisi).grid(row=5, column=0, columnspan=3)
# Dugme za izračunavanje
tk.Button(prozor, text='=', font=("Arial", 18), command=izracunaj).grid(row=5, column=3)

prozor.mainloop()
