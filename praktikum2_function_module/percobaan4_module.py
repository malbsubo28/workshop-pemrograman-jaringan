import numpy as np
import matplotlib.pyplot as plt

nilai_akhir = []
nilai_huruf = []

def kriteria_nilai(nilai):
  kriteria = ''
  if 81 <= nilai <= 100: kriteria = "A"
  elif 71 <= nilai <= 80: kriteria = "AB"
  elif 66 <= nilai <= 70: kriteria = "B"
  elif 61 <= nilai <= 65: kriteria = "BC"
  elif 56 <= nilai <= 60: kriteria = "C"
  elif 41 <= nilai <= 55: kriteria = "D"
  elif 0 <= nilai <= 40: kriteria = "E"
  return kriteria

def output(jumlah_data, data):
  print("╭────────────────────────────────────" +
        "─────────────────────────────────────╮")
  print("│No.│ Nama Mhs \t│ N.Tugas │ N.Kuis" +
        " │ N.Uts │ N.Uas │ N.Akhir    │ N.Huruf │")
  print("│───│───────────│─────────│────────" +
        "│───────│───────│────────────│─────────│")
  for i in range(jumlah_data):
    nilai_akhir.append((data[i][1]+data[i][2]+data[i][3]+data[i][4]) / 4)
    nilai_huruf.append(kriteria_nilai(nilai_akhir[i]))
    print("│",i+1,"│",data[i][0],"\t│",
          data[i][1],"\t  │",
          data[i][2],"\t   │",
          data[i][3],"   │",
          data[i][4],"   │",
          nilai_akhir[i],"\t│",
          nilai_huruf[i],"\t  │")
  print("╰────────────────────────────────────" +
        "─────────────────────────────────────╯")

  n_a=0; n_ab=0; n_b=0; n_bc=0; n_c=0; n_d=0; n_e=0

  for i in nilai_huruf:
    if i == "A": n_a += 1
    elif i == "AB": n_ab += 1
    elif i == "B": n_b += 1
    elif i == "BC": n_bc += 1
    elif i == "C": n_c += 1
    elif i == "D": n_d += 1
    elif i == "E": n_e += 1

  x = np.array([ "A", "AB", "B", "BC", "C", "D", "E"])
  y = np.array([ n_a, n_ab, n_b, n_bc, n_c, n_d, n_e])

  plt.bar(x, y)
  plt.show()
