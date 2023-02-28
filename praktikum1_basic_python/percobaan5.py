jumlah_data = int(input("Masukkan jumlah data : "))
data = [[],[]]

for i in range(jumlah_data):
  print("Data",i)
  data[i] = [input("Masukkan nama mahasiswa \t: "),
             input("Masukkan nilai tugas \t: "),
             input("Masukkan nilai kuis \t: "),
             input("Masukkan nilai uts \t: "),
             input("Masukkan nilai uas \t: "),
             input("Masukkan nilai akhir \t: ")]

print("╭────────────────────────────────────────────────────────────────────────────────╮")
print("│ No│ Nama Mhs \t│ nilai tugas │ nilai kuis │ nilai uts │ nilai uas │ nilai akhir │")
print("│───│───────────│─────────────│────────────│───────────│───────────│─────────────│")
for i in range(jumlah_data):
  print("│",i,"│",data[i][0],"\t│",
        data[i][1],"         │",
        data[i][2],"        │",
        data[i][3],"       │",
        data[i][4],"       │",
        data[i][5],"         │")

print("╰────────────────────────────────────────────────────────────────────────────────╯")
