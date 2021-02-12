from model.model import *

mhs=open('mhs.txt','r').readlines()
nim=open('nim.txt','r').readlines()

for nama, no in zip(mhs, nim):
    Mahasiswa(nim=int(no),nama=str(nama).replace('\n','')).save()

mata_kuliah={
    1:"Pemrograman Web",
    2:"Pemrograman Mobile",
    3:"Kalkulus",
    4:"Aljabar Linear",
    5:"Statistika",
    6:"Metode Numerik",
    7:"Algoritma Pemrograman",
    8:"Struktur Data"
}

for k,v in mata_kuliah.items():
    Matkul(kode=k, nama=v).save()