# Dictionary awal daftar kontak
contacts = {
    "Ari": "081267888",
    "Dina": "087677776"
}

# 1. Tampilkan kontak Ari
print("Kontak Ari:", contacts["Ari"])

# 2. Tambah kontak baru (Riko)
contacts["Riko"] = "087654544"

# 3. Ubah kontak Dina
contacts["Dina"] = "088999776"

# 4. Tampilkan semua Nama
print("Semua Nama:", list(contacts.keys()))

# 5. Tampilkan semua Nomor
print("Semua Nomor:", list(contacts.values()))

# 6. Tampilkan daftar Nama dan Nomornya
print("Daftar lengkap kontak:")
for nama, nomor in contacts.items():
    print(nama, ":", nomor)

# 7. Hapus kontak Dina
contacts.pop("Dina")

# Lihat hasil akhir
print("Kontak setelah Dina dihapus:", contacts)
