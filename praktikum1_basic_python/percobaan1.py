nilai = int(input("Masukkan nilai ? "))
kriteria = ''
info=""
bobot=""
kategori=""

if 81 <= nilai <= 100: kriteria = 'A'; bobot = 4; kategori = "Istimewa"
elif 71 <= nilai <= 80: kriteria = 'AB'; bobot = 3.5; kategori = "Sangat baik"
elif 66 <= nilai <= 70: kriteria = 'B'; bobot = 3; kategori = "Baik"
elif 61 <= nilai <= 65: kriteria = 'BC'; bobot = 2.5; kategori = "Cukup baik"
elif 56 <= nilai <= 60: kriteria = 'C'; bobot = 2; kategori = "Cukup"
elif 41 <= nilai <= 55: kriteria = 'D'; bobot = 1; kategori = "Kurang"
elif 0 <= nilai <= 40: kriteria = 'E'; bobot = 0; kategori = "Sangat kurang"
else: info="Nilai harus dalam range 0 - 100 !!!"

if info == "": print("Kriteria nilai =", kriteria, "\n" + "Bobot =", bobot,"\n" + "Kategori =", kategori)
else: print(info)
