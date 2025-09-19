# ==========================
# Casting Tipe Data
# ==========================

# Casting dari string ke integer
str_angka = "456"
int_angka = int(str_angka)
print(f"Sebelum casting: {str_angka}, tipe datanya adalah {type(str_angka)}")
print(f"Setelah casting: {int_angka}, tipe datanya adalah {type(int_angka)}")

# Casting dari integer ke string
angka_int = 12345
angka_str = str(angka_int)
print(f"\nSebelum casting: {angka_int}, tipe datanya adalah {type(angka_int)}")
print(f"Setelah casting: {angka_str}, tipe datanya adalah {type(angka_str)}")

# Casting dari integer ke boolean
angka_bool_true = 1
print(f"\nNilai {angka_bool_true} setelah di-casting ke boolean: {bool(angka_bool_true)}, tipe datanya adalah {type(bool(angka_bool_true))}")

angka_bool_false = 0
print(f"Nilai {angka_bool_false} setelah di-casting ke boolean: {bool(angka_bool_false)}, tipe datanya adalah {type(bool(angka_bool_false))}")

# ==============================
# Operator Perbandingan
# ==============================
print("\n" + "="*25)
print("HASIL OPERATOR PERBANDINGAN")
print("="*25)
print(f"Apakah 8 sama dengan 8? {8 == 8}")
print(f"Apakah 8 tidak sama dengan 9? {8 != 9}")
print(f"Apakah 8 lebih besar dari 9? {8 > 9}")
print(f"Apakah 8 lebih kecil dari 9? {8 < 9}")
print(f"Apakah 8 lebih kecil atau sama dengan 9? {8 <= 9}")
print(f"Apakah 9 lebih besar atau sama dengan 9? {9 >= 9}")

# ==========================
# Operator Logika
# ==========================
print("\n" + "="*25)
print("HASIL OPERATOR LOGIKA")
print("="*25)
a = True
b = True
print(f"Hasil dari True AND True: {a and b}")
print(f"Hasil dari True OR True: {a or b}")
print(f"Hasil dari NOT True: {not b}")
print(f"Hasil dari 5 > 6 AND 6 < 7: {5 > 6 and 6 < 7}")

# =============================
# Operator Aritmatika
# =============================
print("\n" + "="*25)
print("HASIL OPERATOR ARITMATIKA")
print("="*25)
e = 8
f = 2
print(f"Hasil penjumlahan {e} + {f} adalah: {e + f}")
print(f"Hasil pengurangan {e} - {f} adalah: {e - f}")
print(f"Hasil perkalian {e} * {f} adalah: {e * f}")
print(f"Hasil pembagian {e} / {f} adalah: {e / f}")
print(f"Sisa bagi (modulo) {e} % {f} adalah: {e % f}")
print(f"Hasil pemangkatan {e} pangkat {f} adalah: {e ** f}")

# ==========================
# Input dan Output
# ==========================
print("\n" + "="*25)
print("INPUT & OUTPUT PENGGUNA")
print("="*25)
nama = input("Siapa nama Anda? ")
umur = int(input("Berapa usia Anda? "))

print(f"\nNama: {nama}")
print(f"Usia: {umur}")
print(f"Halo semuanya! Nama saya {nama}, usia {umur} tahun.")

# Contoh format output lainnya
print("="*30)
print("Program Kalkulator Suhu")
print("="*30)

# ==========================================

print("\n" + "="*25)
print("PENGGUNAAN KONDISIONAL")
print("="*25)

try:
    ipk_anda = float(input("Masukkan IPK Anda: "))
    if 0.0 <= ipk_anda <= 4.0:
        if 3.80 <= ipk_anda <= 4.0:
            print(f"Luar biasa! Anda meraih predikat magna cumlaude dengan IPK {ipk_anda}.")
        elif 3.50 <= ipk_anda < 3.80:
            print(f"Hebat! Anda meraih predikat cumlaude dengan IPK {ipk_anda}.")
        elif 3.00 <= ipk_anda < 3.50:
            print(f"IPK Anda cukup stabil.")
        else: # ipk_anda < 3.0
            print(f"Anda perlu meningkatkan IPK.")
    else:
        print(f"Maaf, IPK {ipk_anda} tidak valid.")
except ValueError:
    print("Harap masukkan nilai IPK yang valid (berupa angka).")

try:
    kode_status = int(input("\nMasukkan kode status: "))
    print("Kode Anda berarti:")
    match kode_status:
        case 200:
            print("Sukses!")
        case 400:
            print("Permintaan Buruk (Bad Request)")
        case 401:
            print("Tidak Sah (Unauthorized)")
        case 402:
            print("Pembayaran Dibutuhkan (Payment Required)")
        case 403:
            print("Terlarang (Forbidden)")
        case 404:
            print("Tidak Ditemukan (Not Found)")
        case 500:
            print("Kesalahan Server Internal (Internal Server Error)")
        case _: # Default case
            print("Kode status tidak dikenal.")
except ValueError:
    print("Harap masukkan kode status yang valid (berupa angka).")

angka = 3
tipe_angka = "Angka Genap" if angka % 2 == 0 else "Angka Ganjil"
print(f"\nAngka {angka} adalah: {tipe_angka}")

# ==========================
# Perulangan (Loops)
# ==========================

print("\n" + "="*25)
print("PENGGUNAAN PERULANGAN")
print("="*25)

print("Perulangan for dari 0 sampai 4:")
for i in range(5):
    print(i)

print("\nPerulangan for untuk pesan:")
for _ in range(3):
    print("Ilmu data itu mudah!")

print("\nPerulangan dengan step 2:")
for i in range(1, 5, 2):
    print(i)
    
kata = "Saya ingin menguasai ilmu data"
print(f"\nMelakukan perulangan pada string '{kata}':")
for huruf in kata:
    print(huruf, end=' ')
print() 

print("\nPerulangan menggunakan enumerate:")
for indeks, karakter in enumerate(kata):
    print(f"Indeks {indeks}: {karakter}")

print("\nPerulangan mundur dari 5 ke 1:")
for i in range(5, 0, -1):
    print(i)

print("\nPerulangan dengan break dan continue:")
for i in range(5):
    if i == 2:
        continue  
    if i == 4:
        break     
    print(i)

print("\nPerulangan while:")
hitung = 0
while hitung < 4:
    print("Semangat terus, para intern!")
    hitung += 1