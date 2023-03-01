import statistics

input_data = input("Masukkan 10 data pisahkan dengan ',' : ")
data = []

for i in input_data.split(','):
  data.append(int(i))

# nilai rata-rata
rata_rata = 0
for i in input_data.split(','):
  rata_rata += int(i)
rata_rata = rata_rata/10

# nilai modus
modus = statistics.mode(data)

# nilai median
median = statistics.median(data)

print("Rata-rata =", rata_rata,
      "\nModus =", modus,
      "\nMedian =", median)
