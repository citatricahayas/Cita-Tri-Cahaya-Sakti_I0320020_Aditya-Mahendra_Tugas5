#Input Data
print("===============SELAMAT DATANG===============", "\n")
nama = input('Halo! silahkan masukkan nama kamu : ')
nilai = int(input('Silahkan masukkan nilai kamu = '))
result = 'Halo, ' + nama + '! Nilai kamu setelah dikonversi adalah '

print("\n", "===============NILAI HASIL KONVERSI===============", "\n")
#Proses Konversi Nilai
if 0 <= nilai < 60:
    print(result + 'E')
elif 60 <= nilai <= 64:
    print(result + 'C')
elif 64 < nilai <= 69:
    print(result + 'C+')
elif 69 < nilai <= 74:
    print(result + 'B')
elif 74 < nilai <= 79:
    print(result + 'B+')
elif 79 < nilai <= 84:
    print(result + 'A-')
elif 84 < nilai <= 100:
    print(result + 'A')
else:
    print("Nilai Tidak valid")
