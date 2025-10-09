from tkinter import *
from tkinter import ttk, messagebox

# ==========================================
#   KELAS STACK UNTUK KASIR
# ==========================================
class StackKasir:
    def __init__(self):
        self.stack = []

    def tambah_item(self, nama, harga):
        self.stack.append({"nama": nama, "harga": harga})

    def batal_item(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def total_harga(self):
        return sum(item["harga"] for item in self.stack)

    def daftar_item(self):
        return list(reversed(self.stack))  # item terakhir di atas

    def kosongkan(self):
        self.stack.clear()


# ==========================================
#   GUI UTAMA TKINTER
# ==========================================
class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💳 Kasir Stack System")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e2f")

        self.kasir = StackKasir()
        self.setup_ui()

    # --------------------------------------
    def setup_ui(self):
        # === Judul Aplikasi ===
        Label(
            self.root,
            text="🛒 STACK KASIR SYSTEM",
            bg="#1e1e2f",
            fg="#ffffff",
            font=("Poppins", 18, "bold"),
        ).pack(pady=15)

        # === Frame Input ===
        input_frame = Frame(self.root, bg="#252539", bd=2, relief=RIDGE)
        input_frame.pack(pady=10, padx=20, fill=X)

        Label(input_frame, text="Nama Item:", bg="#252539", fg="white", font=("Poppins", 11)).grid(
            row=0, column=0, padx=10, pady=8, sticky=W
        )
        self.nama_var = StringVar()
        Entry(input_frame, textvariable=self.nama_var, font=("Poppins", 11)).grid(
            row=0, column=1, padx=10, pady=8, sticky=EW
        )

        Label(input_frame, text="Harga (Rp):", bg="#252539", fg="white", font=("Poppins", 11)).grid(
            row=1, column=0, padx=10, pady=8, sticky=W
        )
        self.harga_var = StringVar()
        Entry(input_frame, textvariable=self.harga_var, font=("Poppins", 11)).grid(
            row=1, column=1, padx=10, pady=8, sticky=EW
        )

        input_frame.grid_columnconfigure(1, weight=1)

        # === Tombol Aksi ===
        btn_frame = Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        style = ttk.Style()
        style.configure(
            "TButton",
            font=("Poppins", 11, "bold"),
            padding=6,
            background="#2b2b40",
            foreground="white",
        )

        ttk.Button(btn_frame, text="➕ Tambah Item", command=self.tambah_item).grid(
            row=0, column=0, padx=8
        )
        ttk.Button(btn_frame, text="↩️ Batalkan Item", command=self.batal_item).grid(
            row=0, column=1, padx=8
        )
        ttk.Button(btn_frame, text="🧾 Lihat Total", command=self.tampilkan_total).grid(
            row=0, column=2, padx=8
        )
        ttk.Button(btn_frame, text="🗑️ Reset", command=self.reset_transaksi).grid(
            row=0, column=3, padx=8
        )

        # === Tabel Keranjang ===
        self.tree = ttk.Treeview(
            self.root,
            columns=("nama", "harga"),
            show="headings",
            height=12,
        )
        self.tree.heading("nama", text="Nama Item")
        self.tree.heading("harga", text="Harga (Rp)")
        self.tree.column("nama", width=250, anchor=W)
        self.tree.column("harga", width=100, anchor=E)
        self.tree.pack(padx=20, pady=10, fill=BOTH, expand=True)

        # Style tabel
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2b2b40",
            foreground="white",
            rowheight=28,
            fieldbackground="#2b2b40",
            font=("Poppins", 10),
        )
        style.configure("Treeview.Heading", background="#38385e", foreground="white", font=("Poppins", 11, "bold"))
        style.map("Treeview", background=[("selected", "#4545a5")])

        # === Label Total ===
        self.total_label = Label(
            self.root,
            text="Total: Rp0",
            bg="#1e1e2f",
            fg="#00ffcc",
            font=("Poppins", 16, "bold"),
        )
        self.total_label.pack(pady=15)

    # --------------------------------------
    def refresh_tabel(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.kasir.daftar_item():
            self.tree.insert("", "end", values=(item["nama"], f"Rp{item['harga']:,}"))

        total = self.kasir.total_harga()
        self.total_label.config(text=f"Total: Rp{total:,}")

    # --------------------------------------
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

        self.kasir.tambah_item(nama, harga)
        self.refresh_tabel()

        self.nama_var.set("")
        self.harga_var.set("")

    # --------------------------------------
    def batal_item(self):
        batal = self.kasir.batal_item()
        if batal is None:
            messagebox.showinfo("Info", "Tidak ada item untuk dibatalkan.")
        else:
            messagebox.showinfo("Item Dibatalkan", f"Item '{batal['nama']}' dihapus dari keranjang.")
        self.refresh_tabel()

    # --------------------------------------
    def tampilkan_total(self):
        total = self.kasir.total_harga()
        if total == 0:
            messagebox.showinfo("Total Belanja", "Keranjang masih kosong.")
        else:
            messagebox.showinfo("💰 Total Belanja", f"Total yang harus dibayar: Rp{total:,}")

    # --------------------------------------
    def reset_transaksi(self):
        confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin mengosongkan keranjang?")
        if confirm:
            self.kasir.kosongkan()
            self.refresh_tabel()


# ==========================================
#   MENJALANKAN APLIKASI
# ==========================================
if __name__ == "__main__":
    root = Tk()
    app = KasirApp(root)
    root.mainloop()
