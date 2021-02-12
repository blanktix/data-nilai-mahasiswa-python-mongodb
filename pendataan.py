from os import system
from mongoengine import *
from functools import reduce
from model.model import *
# ============================================================================= #
# Penggunaan closure untuk melihat nilai mahasiswa pada matkul tertentu
def cek_nilai_matkul(data):
    nilai=dict()
    for mhs in data:
        nilai[mhs.nim.nama]=mhs.nilai
    def predikat(nama):
        skor = int(nilai[nama])   
        if (skor>80):
            return ("Nilai dari {} adalah {}, predikat A".format(nama, skor))
        elif (70<skor<=80):
            return ("Nilai dari {} adalah {}, predikat B".format(nama, skor))
        elif (60<skor<=70):
            return ("Nilai dari {} adalah {}, predikat C".format(nama, skor))
        elif (50<skor<=60):
            return ("Nilai dari {} adalah {}, predikat C-".format(nama, skor))
        else:
            return ("Nilai dari {} adalah {}, predikat D".format(nama, skor))
    return predikat
# ============================================================================= #
# Penggunaan closure untuk melihat nilai mahasiswa pada setiap matkul
def cek_nilai_mhs(data):
    nilai=dict()
    for mhs in data:
        nilai[mhs.kode_matkul]=mhs.nilai
    def predikat(kode):
        skor = int(nilai[kode])   
        if (skor>80):
            return ("Nilai matkul {} adalah {}, predikat A".format(kode.nama, skor))
        elif (70<skor<=80):
            return ("Nilai matkul {} adalah {}, predikat B".format(kode.nama, skor))
        elif (60<skor<=70):
            return ("Nilai matkul {} adalah {}, predikat C".format(kode.nama, skor))
        elif (50<skor<=60):
            return ("Nilai matkul {} adalah {}, predikat C-".format(kode.nama, skor))
        else:
            return ("Nilai matkul {} adalah {}, predikat D".format(kode.nama, skor))
    return predikat
# ============================================================================= #
# Penggunaan first class function
def ucapan_semangat(data):
    nilai=dict()
    for mhs in data:
        nilai[mhs.nim.nama]=mhs.nilai
    def apresiasi():
        for nama in nilai:
            if(int(nilai[nama])>80):
                print("Selamat {} pertahankan prestasimu".format(nama))
            elif(70<int(nilai[nama])<=80):
                print("{}, tingkatkan terus prestasimu".format(nama))
            else:
                print("Tidak mengapa {}, teruslah belajar meskipun kamu lambat memahami".format(nama))
    return apresiasi
# ============================================================================= #
# Penerapan decorator untuk menghasilkan output ucapan atas perolehan nilai mhs
def konversi_nilai(func):
    def fungsinya(data):
        func(data)
    return fungsinya
@konversi_nilai
def nilai_rentang_4(data):
    if(int(data.nilai>80)):
        print("Nilai {} dalam rentang 0-4: 4".format(str(data.nim.nama)))
    elif(int(data.nilai)>70):
        print("Nilai {} dalam rentang 0-4: 3.5".format(str(data.nim.nama)))
    elif(int(data.nilai)>60):
        print("Nilai {} dalam rentang 0-4: 3".format(str(data.nim.nama)))
    elif(int(data.nilai)>50):
        print("Nilai {} dalam rentang 0-4: 2.5".format(str(data.nim.nama)))
    else:
        print("Nilai {} dalam rentang 0-4: 2".format(str(data.nim.nama)))
# ============================================================================= #
def jml_nilai_mhs(arr_nilai, n):
    # Recursive function untuk menghitung total nilai
    if(len(arr_nilai)==1):
        return arr_nilai[0]
    else:
        return arr_nilai[0] + jml_nilai_mhs(arr_nilai[1:],n)
# ============================================================================= #
def rata_mhs(data):
    # Pure function untuk enghitung rata2 nilai mahasiswa
    # dari hasil pemanggilan function jml_nilai_mhs
    return (jml_nilai_mhs(data, len(data)))/len(data)
# ============================================================================= #
def rata_matkul(data):
    # Penggunaan function reduce dan lambda
    # untuk menghitung nilai rata2 matkul
    return (reduce(lambda x,y: int(x)+int(y), data))/len(data)
# ============================================================================= #
def tambah():
    # Pure function untuk menambahkan data nilai mahasiswa
    system('clear')
    nim=int(input("Masukkan NIM [232 s.d 277]: "))
    matkul=int(input("Masukkan kode matkul [1-8]: "))
    nilai=int(input("Masukkan nilai [0-100]: "))
    mhs=Nilai(nim=nim, kode_matkul=matkul, nilai=nilai).save()
# ============================================================================= #
def lihat_nilai():
    # # Pure function yang memanggil cek_nilai_matkul, cek_nilai_mhs, nilai_rentang_4
    system('clear')
    pil=int(input("1. Berdasar matkul\n2. Berdasar mahasiswa\nPilih [1|2]: "))
    if pil==1:
        kode=int(input("Masukkan kode mata kuliah: "))
        cek=cek_nilai_matkul(Nilai.objects(kode_matkul=kode))
        system('clear')
        print(*map(cek, list([mhs.nim.nama for mhs in Nilai.objects(kode_matkul=kode)])), sep="\n")
        print(*map(nilai_rentang_4, [mhs for mhs in Nilai.objects(kode_matkul=kode)]))
    else:
        nim=int(input("Masukkan NIM mahasiswa: "))
        cek=cek_nilai_mhs(Nilai.objects(nim=nim))
        system('clear')
        print(*map(cek, list([mhs.kode_matkul for mhs in Nilai.objects(nim=nim)])), sep="\n")
        print(*map(nilai_rentang_4, [mhs for mhs in Nilai.objects(nim=nim)]))
# ============================================================================= #
def cetak_ket():
    # Pure function yang memanggil first class function ucapan_semangat
    system('clear')
    kode=int(input("Masukkan kode mata kuliah [1-8]: "))
    berisemangat=ucapan_semangat(Nilai.objects(kode_matkul=kode))
    berisemangat()
# ============================================================================= #
def rata_mahasiswa():
    # # Pure function yang memanggil jml_nilai_mhs
    system('clear')
    nim=int(input("Masukkan NIM [232-277]: "))
    data=list([mhs.nilai for mhs in Nilai.objects(nim=nim)])
    rata=jml_nilai_mhs(data, len(data))
    print("Rata2 nilai mahasiswa tersebut: {}".format(str(rata/len(data))))
# ============================================================================= #
def rata_mata_kuliah():
    # Pure function yang memanggil rata_matkul
    system('clear')
    kode=int(input("Masukkan kode mata kuliah [1-8]: "))
    rata=rata_matkul(list([x.nilai for x in Nilai.objects(kode_matkul=kode)]))
    print("Rata2 mata kuliah: {}".format(rata))
# ============================================================================= #
def main():
    # Pure function, fungsi utama dengan pilihan menu
    # Infinite loop 
    while True:
        print(
        """
    MENU
    1. Tambah Data Mahasiswa\n
    2. Lihat Nilai Mahasiswa\n
    3. Cetak Keterangan Kelulusan\n
    4. Rata2 kelas\n
    5. Rata2 mahasiswa\n
    6. Keluar
        """
        )
        pil=int(input("Pilih Menu: "))
        if pil==1:
            tambah()
        elif pil==2:
            lihat_nilai()
        elif pil==3:
            cetak_ket()
        elif pil==4:
            rata_mata_kuliah()
        elif pil==5:
            rata_mahasiswa()
        else:
            exit(0)
main()   