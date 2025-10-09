from tkinter import *
from tkinter import ttk, messagebox

# ======================================================
#   KELAS STACK UNTUK KASIR
# ======================================================
class StackKasir:
    def __init__(self):
        self.stack = []  # tumpukan item belanja (LIFO)

    def push(self, nama, harga):
        """Menambahkan item ke atas stack"""
        self.stack.append({"nama": nama, "harga": harga})

    def pop(self):
        """Menghapus item terakhir dari stack"""
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        """Melihat item terakhir tanpa menghapus"""
        if not self.stack:
            return None
        return self.stack[-1]

    def total(self):
        """Menghitung total harga seluruh item"""
        return sum(item["harga"] for item in self.stack)

    def all_items(self):
        """Mengembalikan seluruh item dalam urutan LIFO"""
        return list(reversed(self.stack))

    def clear(self):
        """Mengosongkan seluruh stack"""
        self.stack.clear()


# ======================================================
#   KELAS GUI APLIKASI
# ======================================================
class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack Kasir Minimalist")
        self.root.geometry("520x580")
        self.root.configure(bg="#f5f6fa")

        self.kasir = StackKasir()
        self.setup_ui()

    # --------------------------------------------------
    def setup_ui(self):
        # Judul
        Label(
            self.root,
            text="🛍️  Kasir Stack System",
            bg="#f5f6fa",
            fg="#222222",
            font=("Poppins", 18, "bold")
        ).pack(pady=20)

        # Frame input
        input_frame = Frame(self.root, bg="white", bd=0, relief=FLAT)
        input_frame.pack(padx=20, pady=10, fill=X)

        Label(input_frame, text="Nama Item", bg="white", fg="#333", font=("Poppins", 10)).grid(row=0, column=0, sticky=W, padx=10, pady=5)
        self.nama_var = StringVar()
        Entry(input_frame, textvariable=self.nama_var, font=("Poppins", 10), bd=1, relief=SOLID).grid(row=0, column=1, sticky=EW, padx=10, pady=5)

        Label(input_frame, text="Harga (Rp)", bg="white", fg="#333", font=("Poppins", 10)).grid(row=1, column=0, sticky=W, padx=10, pady=5)
        self.harga_var = StringVar()
        Entry(input_frame, textvariable=self.harga_var, font=("Poppins", 10), bd=1, relief=SOLID).grid(row=1, column=1, sticky=EW, padx=10, pady=5)

        input_frame.grid_columnconfigure(1, weight=1)

        # Tombol aksi
        btn_frame = Frame(self.root, bg="#f5f6fa")
        btn_frame.pack(pady=10)

        self.create_button(btn_frame, "➕ Tambah", self.tambah_item).grid(row=0, column=0, padx=5)
        self.create_button(btn_frame, "↩️ Batalkan", self.batal_item).grid(row=0, column=1, padx=5)
        self.create_button(btn_frame, "💰 Total", self.tampilkan_total).grid(row=0, column=2, padx=5)
        self.create_button(btn_frame, "🗑️ Reset", self.reset_transaksi).grid(row=0, column=3, padx=5)

        # Tabel daftar belanja
        table_frame = Frame(self.root, bg="white")
        table_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("nama", "harga"),
            show="headings",
            height=10
        )
        self.tree.heading("nama", text="Nama Item")
        self.tree.heading("harga", text="Harga (Rp)")
        self.tree.column("nama", anchor=W, width=250)
        self.tree.column("harga", anchor=E, width=100)
        self.tree.pack(fill=BOTH, expand=True)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=28,
                        fieldbackground="white",
                        font=("Poppins", 10))
        style.configure("Treeview.Heading",
                        background="#e0e0e0",
                        foreground="#222",
                        font=("Poppins", 10, "bold"))
        style.map("Treeview", background=[("selected", "#c3f1e8")])

        # Label total
        self.total_label = Label(
            self.root,
            text="Total: Rp0",
            bg="#f5f6fa",
            fg="#009879",
            font=("Poppins", 14, "bold")
        )
        self.total_label.pack(pady=15)

        # Label preview item terakhir
        self.preview_label = Label(
            self.root,
            text="Belum ada item ditambahkan",
            bg="#f5f6fa",
            fg="#555",
            font=("Poppins", 10)
        )
        self.preview_label.pack()

    # --------------------------------------------------
    def create_button(self, frame, text, command):
        btn = Button(
            frame,
            text=text,
            command=command,
            font=("Poppins", 10, "bold"),
            bg="#009879",
            fg="white",
            activebackground="#007b63",
            activeforeground="white",
            relief=FLAT,
            padx=10,
            pady=5,
            cursor="hand2"
        )
        return btn

    # --------------------------------------------------
    def refresh_tabel(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.kasir.all_items():
            self.tree.insert("", "end", values=(item["nama"], f"Rp{item['harga']:,}"))

        total = self.kasir.total()
        self.total_label.config(text=f"Total: Rp{total:,}")

        # Update preview (peek)
        top_item = self.kasir.peek()
        if top_item:
            self.preview_label.config(text=f"Item terakhir: {top_item['nama']} - Rp{top_item['harga']:,}")
        else:
            self.preview_label.config(text="Belum ada item ditambahkan")

    # --------------------------------------------------
    def tambah_item(self):
        nama = self.nama_var.get().strip()
        harga = self.harga_var.get().strip()

        if not nama or not harga:
            messagebox.showwarning("Input Tidak Lengkap", "Masukkan nama dan harga item.")
            return
        try:
            harga = int(harga)
        except ValueError:
            messagebox.showerror("Input Salah", "Harga harus berupa angka.")
            return

        self.kasir.push(nama, harga)
        self.refresh_tabel()
        self.nama_var.set("")
        self.harga_var.set("")

    # --------------------------------------------------
    def batal_item(self):
        batal = self.kasir.pop()
        if batal is None:
            messagebox.showinfo("Info", "Tidak ada item untuk dibatalkan.")
        else:
            messagebox.showinfo("Item Dibatalkan", f"Item '{batal['nama']}' telah dibatalkan.")
        self.refresh_tabel()

    # --------------------------------------------------
    def tampilkan_total(self):
        total = self.kasir.total()
        if total == 0:
            messagebox.showinfo("Total Belanja", "Keranjang masih kosong.")
        else:
            messagebox.showinfo("Total Belanja", f"💰 Total belanja: Rp{total:,}")

    # --------------------------------------------------
    def reset_transaksi(self):
        if messagebox.askyesno("Konfirmasi", "Apakah yakin ingin mengosongkan keranjang?"):
            self.kasir.clear()
            self.refresh_tabel()


# ======================================================
#   MENJALANKAN APLIKASI
# ======================================================
if __name__ == "__main__":
    root = Tk()
    app = KasirApp(root)
    root.mainloop()
