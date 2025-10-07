from tkinter import *

# === Kalkulator gaya iOS/Mac ===
root = Tk()
root.title("Nfldfa's Calculator")
root.configure(bg="#1C1C1C")

# Tampilan Entry (layar hasil)
bar = Entry(root, font=("Nunito", 36, "bold"), justify=RIGHT,
            fg="white", bg="#1C1C1C", bd=0, insertbackground="white")
bar.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Fungsi untuk menambahkan karakter ke layar
def insert_val(num):
    text = bar.get()
    if text == "" and num in ["+", "*", "/", "%", "."]:
        return
    if text.endswith(("+", "-", "*", "/", "%", ".")) and num in ["+", "*", "/", "%", "."]:
        return
    bar["fg"] = "white"
    bar.insert(END, num)

# Fungsi AC (hapus seluruh input)
def clear_all():
    bar.delete(0, END)
    bar["fg"] = "white"

# Fungsi backspace (hapus satu karakter terakhir)
def backspace():
    text = bar.get()
    if text:
        bar.delete(len(text)-1, END)
        bar["fg"] = "white"

# Fungsi plus/minus (flip tanda angka terakhir)
def plus_minus():
    text = bar.get()
    if not text or text[-1] in "+-*/%":
        return
    # cari operator terakhir (abaikan minus yang merupakan tanda unary)
    pos = len(text) - 1
    while pos > 0:
        c = text[pos]
        if c in "+-*/%":
            if not (c == '-' and text[pos-1] in "+-*/%"):
                break
        pos -= 1
    if pos <= 0:
        # toggle tanda di awal
        if text.startswith("-"):
            bar.delete(0)
        else:
            bar.insert(0, "-")
        return
    op = text[pos]
    head = text[:pos]
    tail = text[pos+1:]
    if op == '-':
        new_text = head + "+" + tail
    elif op == '+':
        new_text = head + "-" + tail
    else:  # *, /
        if tail.startswith("-"):
            new_text = head + op + tail[1:]
        else:
            new_text = head + op + "-" + tail
    bar.delete(0, END)
    bar.insert(0, new_text)

# Fungsi persen
def percent():
    text = bar.get()
    if not text:
        return
    try:
        value = eval(text)
        result = value / 100
        bar.delete(0, END)
        bar.insert(0, str(result))
    except:
        bar["fg"] = "red"

# Fungsi evaluate (=)
def evaluate():
    text = bar.get()
    try:
        result = eval(text)
        result = round(result, 10)
        bar.delete(0, END)
        bar.insert(0, str(result))
        bar["fg"] = "white"
    except:
        bar.delete(0, END)
        bar.insert(0, "Error")
        bar["fg"] = "red"

# Atur grid untuk tombol (agar proporsional)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Definisi tombol: (teks, baris, kol, fungsi, warna latar, warna teks, [span])
buttons = [
    ("AC", 1, 0, clear_all, "#D4D4D2", "black"),
    ("±", 1, 1, plus_minus, "#D4D4D2", "black"),
    ("%", 1, 2, percent, "#D4D4D2", "black"),
    ("÷", 1, 3, lambda: insert_val("/"), "#FF9500", "white"),
    ("7", 2, 0, lambda: insert_val("7"), "#505050", "white"),
    ("8", 2, 1, lambda: insert_val("8"), "#505050", "white"),
    ("9", 2, 2, lambda: insert_val("9"), "#505050", "white"),
    ("×", 2, 3, lambda: insert_val("*"), "#FF9500", "white"),
    ("4", 3, 0, lambda: insert_val("4"), "#505050", "white"),
    ("5", 3, 1, lambda: insert_val("5"), "#505050", "white"),
    ("6", 3, 2, lambda: insert_val("6"), "#505050", "white"),
    ("−", 3, 3, lambda: insert_val("-"), "#FF9500", "white"),
    ("1", 4, 0, lambda: insert_val("1"), "#505050", "white"),
    ("2", 4, 1, lambda: insert_val("2"), "#505050", "white"),
    ("3", 4, 2, lambda: insert_val("3"), "#505050", "white"),
    ("+", 4, 3, lambda: insert_val("+"), "#FF9500", "white"),
    ("0", 5, 0, lambda: insert_val("0"), "#505050", "white", 2),
    (".", 5, 2, lambda: insert_val("."), "#505050", "white"),
    ("=", 5, 3, evaluate, "#FF9500", "white")
]

for (text, row, col, cmd, bg, fg, *extra) in buttons:
    span = extra[0] if extra else 1
    Button(root, text=text, font=("Nunito", 18, "bold"),
           bd=0, bg=bg, fg=fg,
           activebackground=("#FFA500" if bg == "#FF9500" else "#A6A6A6"),
           command=cmd, width=4, height=2
           ).grid(row=row, column=col, columnspan=span,
                  sticky="nsew", padx=1, pady=1)

root.mainloop()
