ordo = input("Masukkan ordo matriks [ex.3x3,3x2...] : ")
baris_kolom = []
matriks_a = [[], []]
matriks_b = [[], []]
hasil_matriks = [[], []]

for i in ordo.split('x'):
  baris_kolom.append(int(i))

# input data matriks
for data in range(2):
  if data == 0: matriks = 'A'
  else: matriks = 'B'
  print("Masukkan elemen-elemen matriks", matriks)
  for i in range(baris_kolom[0]):
    for j in range(baris_kolom[1]):
      print(matriks,"[",i+1,"][",j+1,"] = ", sep='', end='')
      if data == 0: matriks_a[i].append(float(input()))
      else: matriks_b[i].append(float(input()))

# penjumlahan kedua matriks
for i in range(baris_kolom[0]):
  for j in range(baris_kolom[1]):
    hasil = matriks_a[i][j] + matriks_b[i][j]
    hasil_matriks[i].append(hasil)

# output matriks
for data in range(3):
  if data == 0: output = matriks_a; print("\nMatriks A :")
  elif data == 1: output = matriks_b; print("Matriks B :")
  else: output = hasil_matriks; print("Hasil penjumlahan matriks A+B")
  for i in range(baris_kolom[0]):
    print("[ ", sep='', end='')
    for j in range(baris_kolom[1]):
      print(output[i][j], "", end='')
    print("]")
