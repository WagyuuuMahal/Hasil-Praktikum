# 1. Variabel dan Tipe Data
print("=== 1. Variabel dan Tipe Data ===")
a = 10              # int
b = 3.14            # float
c = "Belajar Python" # str
d = [1, 2, 3]       # list

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 2. List dan Manipulasi
print("\n=== 2. List dan Manipulasi ===")
belanja = ["beras", "minyak", "telur"]

def tambah_item(item):
    belanja.append(item)

tambah_item("gula")
tambah_item("kopi")

print("Daftar belanja:")
for item in belanja:
    print("-", item)

# 3. Dictionary
print("\n=== 3. Dictionary ===")
harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

total = sum(harga.values())
print("Harga belanjaan:")
for barang, h in harga.items():
    print(f"- {barang}: {h}")
print("Total belanja =", total)

# 4. Fungsi menghitung luas dan keliling lingkaran
print("\n=== 4. Fungsi Lingkaran ===")
import math

def hitung_lingkaran(r):
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    return luas, keliling

r = 7
luas, keliling = hitung_lingkaran(r)
print(f"Jari-jari = {r}")
print(f"Luas = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")

# 5. Percabangan
print("\n=== 5. Percabangan ===")
usia = int(input("Masukkan usia: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia > 50:
    print("Lansia")
else:
    print("Usia tidak valid")