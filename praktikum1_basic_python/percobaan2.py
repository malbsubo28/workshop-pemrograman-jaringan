input_x = float(input("Masukkan nilai x : "))

def fungsi(x):
  hasil = 2*(x*x*x) + 2*x + (15/x)
  print("f(",x,")"," = 2.x^3 + 2.x + 15/x = ",hasil, sep='')

fungsi(input_x)
