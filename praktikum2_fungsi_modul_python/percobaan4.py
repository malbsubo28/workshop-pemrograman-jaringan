import percobaan4_module as module1

jumlah_data = int(input("Masukkan jumlah data : "))
data = []
nilai_akhir = []

for i in range(jumlah_data):
  print("Data",i+1)
  data.append([input("Masukkan nama mahasiswa : "),
             int(input("Masukkan nilai tugas \t: ")),
             int(input("Masukkan nilai kuis \t: ")),
             int(input("Masukkan nilai uts \t: ")),
             int(input("Masukkan nilai uas \t: ")),])

module1.output(jumlah_data, data)
