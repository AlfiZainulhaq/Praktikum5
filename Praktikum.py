data_mahasiswa = {}

def hitung_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\nProgram Input Nilai")
    print("====================")
    print("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    pilihan = input("Pilih menu: ").lower()

    # LIHAT DATA
    if pilihan == 'l':
        print("\nDaftar Nilai")
        print("============================================================")
        print("| NO |   NIM   |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
        print("============================================================")
        if not data_mahasiswa:
            print("|                  TIDAK ADA DATA                        |")
        else:
            for i, (nim, mhs) in enumerate(data_mahasiswa.items(), start=1):
                print(f"| {i} | {nim} | {mhs['nama']} | {mhs['tugas']} | {mhs['uts']} | {mhs['uas']} | {mhs['akhir']:.2f} |")
        print("============================================================")

    # TAMBAH DATA
    elif pilihan == 't':
        nim = input("NIM: ")
        nama = input("Nama: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        akhir = hitung_akhir(tugas, uts, uas)

        data_mahasiswa[nim] = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print("Data berhasil ditambah!")

    # UBAH DATA
    elif pilihan == 'u':
        nim = input("Masukkan NIM yang mau diubah: ")
        if nim in data_mahasiswa:
            nama = input("Nama baru: ")
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            akhir = hitung_akhir(tugas, uts, uas)

            data_mahasiswa[nim] = {
                "nama": nama,
                "tugas": tugas,
                "uts": uts,
                "uas": uas,
                "akhir": akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    # HAPUS DATA
    elif pilihan == 'h':
        nim = input("Masukkan NIM yang mau dihapus: ")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ada!")

    # CARI DATA
    elif pilihan == 'c':
        nim = input("Masukkan NIM yang dicari: ")
        if nim in data_mahasiswa:
            mhs = data_mahasiswa[nim]
            print("\nData ditemukan!")
            print(f"NIM   : {nim}")
            print(f"Nama  : {mhs['nama']}")
            print(f"Tugas : {mhs['tugas']}")
            print(f"UTS   : {mhs['uts']}")
            print(f"UAS   : {mhs['uas']}")
            print(f"Akhir : {mhs['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    # KELUAR
    elif pilihan == 'k':
        print("Keluar program...")
        break

    else:
        print("Pilihan tidak ada!")
