from tkinter import *

# === Setup Utama ===
root = Tk()
root.geometry("320x480")
root.title("Math With Daffa")
root.configure(bg="#1b1b1b")  # warna latar belakang lebih lembut

# === Entry Display ===
bar = Entry(
    root,
    font=("Nunito", 36, "bold"),
    fg="white",
    bg="#262626",
    justify=RIGHT,
    bd=0,
    insertbackground="white",
)
bar.place(x=10, y=25, width=300, height=100)

X = 80
Y = 95

# === Fungsi-Fungsi Utama ===
def insert(num):
    """Masukkan angka atau operator"""
    bar["fg"] = "white"
    text = bar.get()

    # Jika belum ada teks dan user langsung menekan operator
    if text == "" and num in ["+", "-", "*", "/", ")", "."]:
        return

    # Cegah double operator
    if text.endswith(("+", "-", "*", "/", ".")) and num in ["+", "-", "*", "/", "."]:
        return

    bar.insert(END, num)


def BackSpace():
    """Hapus 1 karakter terakhir"""
    bar["fg"] = "white"
    text = bar.get()
    if text:
        bar.delete(len(text) - 1, END)


def Delete():
    """Clear semua teks"""
    bar["fg"] = "white"
    bar.delete(0, END)


def BracketCheck():
    """Periksa keseimbangan tanda kurung"""
    text = str(bar.get())
    return text.count("(") - text.count(")")


def Answer():
    """Hitung hasil"""
    text = str(bar.get())

    # Tambahkan kurung penutup otomatis
    add = BracketCheck()
    if add > 0:
        bar.insert(END, add * ")")

    try:
        answer = eval(text)
        Delete()
        bar.insert(0, round(answer, 10))  # hasil dibulatkan agar rapi
        bar["fg"] = "#00FF80"  # hasil = warna hijau
    except:
        bar["fg"] = "red"


# === Desain Tombol ===
button_cfg = {
    "font": ("Nunito", 18, "bold"),
    "bd": 0,
    "bg": "#000000",
    "activebackground": "#333333",
    "activeforeground": "#FF9D0C",
    "fg": "white",
    "width": 4,
    "height": 2,
}

# === Baris Tombol Atas ===
Button(root, text="AC", fg="#FF9D0C", command=Delete, **button_cfg).place(x=10, y=140)
Button(root, text="←", fg="#FF9D0C", command=BackSpace, **button_cfg).place(x=90, y=140)
Button(root, text="(", fg="#FF9D0C", command=lambda: insert("("), **button_cfg).place(x=170, y=140)
Button(root, text=")", fg="#FF9D0C", command=lambda: insert(")"), **button_cfg).place(x=250, y=140)

# === Baris Angka dan Operator ===
angka = [
    ("7", 10, 235),
    ("8", 90, 235),
    ("9", 170, 235),
    ("4", 10, 325),
    ("5", 90, 325),
    ("6", 170, 325),
    ("1", 10, 415),
    ("2", 90, 415),
    ("3", 170, 415),
    ("0", 90, 505),
    (".", 10, 505),
]

for (text, x, y) in angka:
    Button(root, text=text, command=lambda t=text: insert(t), **button_cfg).place(x=x, y=y)

# === Operator ===
ops = [
    ("÷", "/", 250, 235),
    ("×", "*", 250, 325),
    ("−", "-", 250, 415),
    ("+", "+", 250, 505),
]
for (label, val, x, y) in ops:
    Button(root, text=label, fg="#FF9D0C", command=lambda v=val: insert(v), **button_cfg).place(x=x, y=y)

# === Tombol Sama Dengan ===
Button(
    root,
    text="=",
    font=("Nunito", 18, "bold"),
    bg="#FF9D0C",
    fg="white",
    activebackground="#ffaa1f",
    activeforeground="white",
    bd=0,
    width=18,
    height=2,
    command=Answer,
).place(x=10, y=590 - 80)

root.mainloop()
