def rp(angka):
    return f"Rp{int(angka):,}".replace(",",".")
class TagihanLaoundry:
    def __init__(self, nama, layanan, berat):
        self.nama = nama
        self.layanan = layanan.capitalize()
        self.berat = float(berat)
    def validasi(self):
        if self.layanan not in ["Reguler", "Kilat"]:
            print("Error: Layanan hanya Reguler atau Kilat!")
            return False
        if self.berat <= 0:
            print("Error: Berat cucian harus lebih dari 0!")
            return False
        return True
    def hitung_subtotal(self):
        tarif = 12000 if self.layanan == "Kilat" else 8000
        return int(self.berat * tarif)
    def get_diskon_persen(self):
        if self.berat >= 10:
            return 15
        elif self.berat >= 5:
            return 10
        return 0
    def hitung_potongan(self):
        return int(self.hitung_subtotal() * self.get_diskon_persen() / 100)
    def hitung_total(self):
        return self.hitung_subtotal() - self.hitung_potongan()
    def cetak_nota(self):
        tarik = 12000 if self.layanan == "Kilat" else 8000
        print(":NOTA PEMBAYARAN LAUNDRY:")
        print(f"Pelanggan : {self.nama}")
        print(f"Layanan   : {self.layanan} ({rp(tarik)}/kg)")
        print(f"Berat     : {self.berat} kg")
        print(f"Subtotal  : {rp(self.hitung_subtotal())}")
        print(f"Diskon    : {self.get_diskon_persen()}%")
        print(f"Potongan  : {rp(self.hitung_potongan())}")
        print(f"Total     : {rp(self.hitung_total())}")
print(" LAUNDRY CLEAN & FRESH ")
nama = input("Nama pelanggan : ")
layanan = input("Jenis layanan : ")
berat = float(input("Berat cucian : "))
nota = TagihanLaoundry(nama, layanan, berat)
if nota.validasi():
    nota.cetak_nota()