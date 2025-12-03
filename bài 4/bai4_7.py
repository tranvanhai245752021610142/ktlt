S = input('Nhap chuoi: ')
ket_qua = ''

for ch in S:
    if not ch.isdigit():     
        ket_qua += ch       

print('Chuoi sau khi loai bo chu so:', ket_qua)
