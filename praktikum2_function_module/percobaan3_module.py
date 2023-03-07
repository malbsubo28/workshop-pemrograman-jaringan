def hitung_bilangan(bilangan):
  ganjil = []
  genap = []
  for i in bilangan.split(','):
    if int(i) % 2 == 0: ganjil.append(int(i))
    else: genap.append(int(i))

  if ganjil.__len__() != 0:
    print("Jumlah bilangan ganjil :",
          ganjil.__len__(), "yaitu ", end="")
    for i in ganjil:
      print(i, "", end="")
  print()
  if genap.__len__() != 0:
    print("Jumlah bilangan genap :",
          genap.__len__(), "yaitu ", end="")
    for i in genap:
      print(i, "", end="")
  print()
