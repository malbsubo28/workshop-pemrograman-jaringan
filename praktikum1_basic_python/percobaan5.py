jumlah_data = int(input("Masukkan jumlah data : "))
data = []
nilai_akhir = []

for i in range(jumlah_data):
  print("Data",i+1)
  data.append([input("Masukkan nama mahasiswa \t: "),
             int(input("Masukkan nilai tugas \t: ")),
             int(input("Masukkan nilai kuis \t: ")),
             int(input("Masukkan nilai uts \t: ")),
             int(input("Masukkan nilai uas \t: ")),])

print("╭──────────────────────────────────────────" +
      "─────────────────────────────────────╮")
print("│ No│ Nama Mhs \t│ nilai tugas │ nilai kuis" +
      " │ nilai uts │ nilai uas │nilai akhir │")
print("│───│───────────│─────────────│────────────" +
      "│───────────│───────────│────────────│")
for i in range(jumlah_data):
  nilai_akhir.append((data[i][1]+data[i][2]+data[i][3]+data[i][4]) / 4)
  print("│",i+1,"│",data[i][0],"\t│",
        data[i][1],"         │",
        data[i][2],"        │",
        data[i][3],"       │",
        data[i][4],"       │",
        nilai_akhir[i],"\t│")

print("╰──────────────────────────────────────────" +
      "─────────────────────────────────────╯")
