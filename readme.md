# Ujian Praktik Live Coding - Pemrograman Berorientasi Objek (PBO) Paket 2

## A. Identitas Peserta

* **Nama Lengkap** : Abbi Maulanha Malik
* **NIM** : 2595114007
* **Kelas** : TI-A
* **Program Studi** : S1 Teknik Informatika
* **Fakultas / Instansi** : Fakultas Teknologi Informasi - Universitas Hasyim Asy'ari Tebuireng

## B. Kasus Pilihan yang Diselesaikan

1. **Kasus 1** : Sistem Tagihan Laundry Kiloan (`kasus_1_laundry.py`)
2. **Kasus 2** : Sistem Penggajian Karyawan Honorer (`kasus_2_gaji.py`)

## C. Lembar Pencatatan Waktu Ujian & Tautan Bukti

* **Tanggal Pengerjaan** : Senin, 19 Oktober 2026
* **Waktu Mulai** : 14:14:00 WIB
* **Waktu Selesai** : 16:15:00 WIB
* **Total Durasi Pengerjaan** : 02:01:00 (2 jam 1 menit)
* **Link Rekaman Layar (YouTube)** : <https://www.youtube.com/watch?v=hcos9_8Qx4s>

## D. Petunjuk Menjalankan Program

Pastikan Python 3 telah terpasang di sistem. Buka terminal (PowerShell / Command Prompt) pada direktori proyek ini, lalu jalankan perintah berikut:

### 1. Menjalankan Kasus 1 (`kasus_1_laundry.py`)

```bash
python kasus_1_laundry.py
```

* **Skenario Uji Normal (Sesuai Soal):**
  * Nama pelanggan : `Citra`
  * Jenis layanan  : `Kilat`
  * Berat cucian   : `6.5`
* **Skenario Uji Validasi (Input Tidak Valid):**
  * Masukkan layanan selain Reguler/Kilat (misal: `Express`) atau berat `<= 0` (misal: `-5`).

### 2. Menjalankan Kasus 2 (`kasus_2_gaji.py`)

```bash
python kasus_2_gaji.py
```

* **Skenario Uji Normal (Sesuai Soal):**
  * ID Karyawan : `H-104`
  * Nama        : `Hendra`
  * Jam Kerja   : `48`
* **Skenario Uji Validasi (Input Tidak Valid):**
  * Masukkan jam kerja di luar rentang 1 s.d. 80 jam (misal: `0` atau `90`).

## E. Format Data Pengumpulan Tugas

```text
PENGUMPULAN UJIAN LIVE CODING PBO
Nama lengkap      : Abbi Maulanha Malik
NIM               : 2595114007
Kelas             : TI-A
Kasus dikerjakan  : Kasus 1 dan Kasus 2
Waktu mulai       : 14:14:00 WIB
Waktu selesai     : 16:15:00 WIB
Durasi stopwatch  : 02:01:00
Repository GitHub : https://github.com/abbimaulanhamalik/ujian-livecoding-pbo-2595114007
Rekaman layar     : https://www.youtube.com/watch?v=hcos9_8Qx4s
```

## F. Catatan Refleksi & Permohonan Maaf kepada Dosen Pengampu

Kepada Yth. Dosen Pengampu Mata Kuliah PBO,

Melalui lembar ini, saya menyampaikan permohonan maaf yang sebesar-besarnya terkait durasi pengerjaan saya yang cukup panjang (total 2 jam 1 menit) dan atas keterbukaan saya selama proses live coding.

Seluruh baris kode program dan alur logikanya saya ketik secara manual sendiri. Namun, dalam proses debugging, saya sempat mengalami kesulitan memahami pesan error terminal (seperti *syntax error* saat REPL aktif, *name error*, dan *type error* pada pemanggilan method). Karena keterbatasan pemahaman saya dalam menganalisis *traceback* error tersebut secara mandiri, saya sempat memanfaatkan AI semata-mata untuk menanyakan letak tanda baca atau tanda kurung yang keliru agar program dapat berjalan normal.

Saya menyadari hal ini menjadi evaluasi besar bagi kemampuan debugging mandiri saya. Ke depannya, saya berkomitmen untuk lebih giat berlatih membaca pesan *traceback* error terminal secara mandiri tanpa bergantung pada alat bantu apa pun. Terima kasih atas pengertian dan bimbingan Bapak Dosen.
