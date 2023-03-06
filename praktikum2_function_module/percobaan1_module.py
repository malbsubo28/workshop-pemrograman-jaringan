def fungsi_nilai_huruf(nilai):
  nilai_huruf = ''
  if 81 <= nilai <= 100: nilai_huruf = 'A'
  elif 71 <= nilai <= 80: nilai_huruf = 'AB'
  elif 66 <= nilai <= 70: nilai_huruf = 'B'
  elif 61 <= nilai <= 65: nilai_huruf = 'BC'
  elif 56 <= nilai <= 60: nilai_huruf = 'C'
  elif 41 <= nilai <= 55: nilai_huruf = 'D'
  elif 0 <= nilai <= 40: nilai_huruf = 'E'
  return nilai_huruf

