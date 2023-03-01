from percobaan2_module import hitung_total

jumlah_barang = int(input("Jumlah barang : "))
nama_barang = []
banyak_barang = []

for i in range(jumlah_barang):
  print("Nama Barang", i+1, ": ", end='')
  nama_barang.append(input())
  print("Jumlah     ", i+1, ": ", end='')
  banyak_barang.append(int(input()))

hitung_total(jumlah_barang, nama_barang, banyak_barang)
