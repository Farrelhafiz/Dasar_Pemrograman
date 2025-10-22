print('       PROGRAM HITUNG GAJI KARYAWAN')
gakok=300000
kryw=input('Nama Karywawan: ')
gol=int(input('Golongan karyawan: '))
pdk=(input('Pendidikan: '))
jk=int(input('Jam Kerja: '))
if gol==1:
    tunjg_jb=int(0.05*gakok)
elif gol==2:
    tunjg_jb=int(0.1*gakok)
elif gol==3:
    tunjg_jb=int(0.15*gakok)
else:
    tunjg_jb=0

if pdk=='SMA' or pdk=='Sma'or pdk=='sma':
    tunjg_pdk=int(0.025*gakok)
elif pdk=='D1'or pdk=='d1':
    tunjg_pdk=int(0.05*gakok)
elif pdk=='D3'or pdk=='d3':
    tunjg_pdk=int(0.2*gakok)
elif pdk=='S1'or pdk=='s1':
    tunjg_pdk=int(0.3*gakok)
else:
    tunjg_pdk=0

if jk>8:
    hasil_lmbr=(jk-8)*3500
else:
    hasil_lmbr=0

tg=gakok+tunjg_jb+tunjg_pdk+hasil_lmbr

print('Karyawan yang bernama',(kryw))
print('Honor yang diterima ')
print('    Tunjangan Jabatan       Rp'+str(tunjg_jb))
print('    Tunjangan Pendidikan    Rp'+str(tunjg_pdk))
print('    Honor Lembur            Rp'+str(hasil_lmbr))
print('                            _______________+')
print('    Total Gaji              Rp'+str(tg))
