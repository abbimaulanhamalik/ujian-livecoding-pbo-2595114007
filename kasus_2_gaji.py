def rp(angka):
    return f"Rp{int (angka):,}".replace(",",".")
class GajiKaryawan:
    def __init__(self, id_kar, nama, jam):
        self.id_kar = id_kar
        self.nama = nama
        self.jam = int(jam)
    def validasi(self):
        if self.jam < 1 or self.jam > 80:
            print("Error: Jam kerja harus antara 1 sampai 80 jam!")
            return False
        return True
    def hitung_gaji_pokok(self):
        jam_reg = 40 if self.jam > 40 else self.jam
        return jam_reg * 30000
    def hitung_lembur(self):
        jam_lembur = (self.jam - 40) if self.jam > 40 else 0
        return jam_lembur * 45000
    def hitung_kotor(self):
        return self.hitung_gaji_pokok() + self.hitung_lembur()
    def hitung_pajak(self):
        if self.hitung_kotor() >= 1500000:
            return int(self.hitung_kotor() * 0.05)
        return 0
    def hitung_bersih(self):
        return self.hitung_kotor() - self.hitung_pajak()
    def cetak_slip(self):
        jam_reg = 40 if self.jam > 40 else self.jam
        jam_lembur = (self.jam - 40) if self.jam > 40 else 0
        p_teks = "5%" if self.hitung_kotor() >= 1500000 else "0%"
        print("Slip Gaji Karyawan")
        print(f"ID Karyawan : {self.id_kar}")
        print(f"Nama        : {self.nama}")
        print(f"Jam Reguler : {jam_reg} jam ({rp(self.hitung_gaji_pokok())})")
        print(f"Jam Lembur  : {jam_lembur} jam ({rp(self.hitung_lembur())})")
        print(f"Pajak ({p_teks}) : {rp(self.hitung_pajak())}")
        print(f"Total Bersih: {rp(self.hitung_bersih())}")
print(" SISTEM PENGGAJIAN HONORER ")
id_kar = input("ID Karyawan : ")
nama = input ("Nama        : ")
jam = int(input("Jam Kerja    :"))
slip = GajiKaryawan(id_kar, nama, jam)
if slip.validasi():
    slip.cetak_slip()