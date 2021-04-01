#Input Data
nama = input("Halo, silahkan masukkan nama anda: ")
gender = input("Silahkan masukkan jenis kelamin anda (P/L) = ")   #Keterangan:
salam = 'Selamat datang, '                                        #P = Perempuan
                                                                  #L = Laki-laki
#Proses Memberi Ucapan
if gender == 'P' or gender == 'p':
    print(salam + 'Nyonya' + ' ' + nama + '!')
elif gender == 'L' or gender == 'l':
    print(salam + 'Tuan' + ' ' + nama + '!')
else:
    pass