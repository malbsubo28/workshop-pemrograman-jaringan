def hitung_total(jumlah_barang, nama_barang, banyak_barang):
  total_harga = 0
  harga = []
  sepb = []
  for i in range(jumlah_barang):
    harga_barang = 0
    if nama_barang[i] == "Pasta gigi":
      harga_barang = 4000
      sepb.append("\t")
    if nama_barang[i] == "Gula":
      harga_barang = 7500
      sepb.append("\t\t")
    if nama_barang[i] == "Garam":
      harga_barang = 2000
      sepb.append("\t\t")
    harga.append(banyak_barang[i]*harga_barang)
  
  print("\nNama\t\tJumlah\t\tHarga")
  for i in range(jumlah_barang):
    print(nama_barang[i], sepb[i], banyak_barang[i], "\t\t",
          harga[i], sep='')
    total_harga += harga[i]

  print("Total pembelian :", total_harga)

