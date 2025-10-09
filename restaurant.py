from tkinter import *
from tkinter import ttk, messagebox

# ======================================================
#   KELAS STACK UNTUK PESANAN RESTORAN
# ======================================================
class StackRestoran:
    def __init__(self):
        self.stack = []

    def push(self, nama, harga):
        """Menambahkan pesanan ke stack"""
        self.stack.append({"nama": nama, "harga": harga})

    def pop(self):
        """Menghapus pesanan terakhir"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        """Melihat pesanan terakhir"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def get_all(self):
        return list(reversed(self.stack))  # agar tampilan urut dari atas ke bawah

    def total_harga(self):
        return sum(item["harga"] for item in self.stack)


# ======================================================
#   APLIKASI UTAMA
# ======================================================
class RestoranApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍽️ Restoran Stack Manager")
        self.root.geometry("360x260")
        self.root.config(bg="#f8f9fa")

        self.stack = StackRestoran()
        self.setup_ui()

    # ==================================================
    #   SETUP UI
    # ==================================================
    def setup_ui(self):
        title = Label(
            self.root,
            text="🍴 Sistem Pesanan Restoran (Stack)",
            font=("Poppins SemiBold", 20),
            bg="#f8f9fa",
            fg="#212529",
        )
        title.pack(pady=20)

        # Frame input
        frame_input = Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        frame_input.pack(padx=20, pady=10, fill=X)

        Label(frame_input, text="Nama Menu :", font=("Poppins", 12), bg="#ffffff").grid(
            row=0, column=0, padx=10, pady=10, sticky=W
        )
        self.entry_nama = Entry(frame_input, font=("Poppins", 12), width=25)
        self.entry_nama.grid(row=0, column=1, padx=10, pady=10)

        Label(frame_input, text="Harga (Rp) :", font=("Poppins", 12), bg="#ffffff").grid(
            row=0, column=2, padx=10, pady=10, sticky=W
        )
        self.entry_harga = Entry(frame_input, font=("Poppins", 12), width=15)
        self.entry_harga.grid(row=0, column=3, padx=10, pady=10)

        Button(
            frame_input,
            text="Tambah Pesanan",
            font=("Poppins", 11, "bold"),
            bg="#28a745",
            fg="white",
            padx=12,
            command=self.tambah_pesanan,
        ).grid(row=0, column=4, padx=10)

        Button(
            frame_input,
            text="Hapus Pesanan Terakhir",
            font=("Poppins", 11, "bold"),
            bg="#dc3545",
            fg="white",
            padx=12,
            command=self.hapus_pesanan,
        ).grid(row=0, column=5, padx=10)

        # ==================================================
        #   FRAME DAFTAR PESANAN
        # ==================================================
        frame_list = Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        frame_list.pack(padx=20, pady=15, fill=BOTH, expand=True)

        Label(frame_list, text="Daftar Pesanan:", font=("Poppins SemiBold", 14), bg="#ffffff").pack(pady=10)

        columns = ("No", "Nama Menu", "Harga")
        self.tree = ttk.Treeview(frame_list, columns=columns, show="headings", height=10)
        self.tree.heading("No", text="No")
        self.tree.heading("Nama Menu", text="Nama Menu")
        self.tree.heading("Harga", text="Harga (Rp)")
        self.tree.column("No", width=50, anchor=CENTER)
        self.tree.column("Nama Menu", width=300)
        self.tree.column("Harga", width=150, anchor=E)
        self.tree.pack(fill=BOTH, expand=True, padx=10, pady=5)

        # Gaya Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Poppins SemiBold", 12), background="#007bff", foreground="black")
        style.configure("Treeview", font=("Poppins", 11), rowheight=28)

        # Label total harga
        self.label_total = Label(
            self.root,
            text="Total Harga: Rp 0",
            font=("Poppins SemiBold", 14),
            bg="#f8f9fa",
            fg="#212529",
        )
        self.label_total.pack(pady=10)

    # ==================================================
    #   FUNGSI STACK OPERASI
    # ==================================================
    def tambah_pesanan(self):
        nama = self.entry_nama.get().strip()
        harga = self.entry_harga.get().strip()

        if not nama or not harga:
            messagebox.showwarning("Peringatan", "Nama menu dan harga harus diisi!")
            return

        try:
            harga = int(harga)
        except ValueError:
            messagebox.showerror("Error", "Harga harus berupa angka!")
            return

        self.stack.push(nama, harga)
        self.entry_nama.delete(0, END)
        self.entry_harga.delete(0, END)
        self.update_tampilan()

    def hapus_pesanan(self):
        removed = self.stack.pop()
        if removed:
            messagebox.showinfo("Pesanan Dihapus", f"Pesanan '{removed['nama']}' telah dihapus dari antrian.")
        else:
            messagebox.showwarning("Kosong", "Tidak ada pesanan untuk dihapus!")
        self.update_tampilan()

    def update_tampilan(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, item in enumerate(self.stack.get_all(), start=1):
            self.tree.insert("", "end", values=(i, item["nama"], f"Rp {item['harga']:,}"))

        total = self.stack.total_harga()
        self.label_total.config(text=f"Total Harga: Rp {total:,}")


# ======================================================
#   MAIN PROGRAM
# ======================================================
if __name__ == "__main__":
    root = Tk()
    app = RestoranApp(root)
    root.mainloop()
