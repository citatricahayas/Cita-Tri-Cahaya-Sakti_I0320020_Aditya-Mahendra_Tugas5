#Penggunaan if untuk tiga kasus
#Inputkan koordinat
print("Masukkan koordinat!")
x = int(input('Input nilai x = '))
y = int(input('Input nilai y = '))
info = 'koodinat (' + str(x) + ',' + str(y) + ' ) berada pada kuadran '
#Memeriksa bilangan
if x > 0 and y > 0:
    print(info + 'I')
elif x < 0 and y > 0:
    print(info + 'II')
elif x < 0 and y < 0:
    print(info + 'III')
elif x > 0 and y < 0:
    print(info + 'IV')
else:
    pass
