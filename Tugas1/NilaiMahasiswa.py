print ("Selamat Datang di Aplikasi Perhitungan Nilai Mahasiswa")

tugas = float(input("Silahkan Masukkan Nilai Tugas Anda : "))
uts = float(input("Silahkan Masukkan Nilai UTS Anda : "))
uas = float(input("Silahkan Masukkan Nilai UAS Anda : "))

nilai_akhir = (0.25*tugas) + (0.35*uts) + (0.4*uas)
print ("Nilai Akhir Anda : ",nilai_akhir)

if nilai_akhir > 85 :
    print ("Dalam Huruf : A")
elif 80 <= nilai_akhir <= 85 :
    print ("Dalam Huruf : A-")
elif 75 <= nilai_akhir < 80 :
    print ("Dalam Huruf : B+")
elif 70 <= nilai_akhir < 75 :
    print ("Dalam Huruf : B")
elif 65 <= nilai_akhir < 70 :
    print ("Dalam Huruf : B-")
elif 60 <= nilai_akhir < 65 :
    print ("Dalam Huruf : C+")
elif 55 <= nilai_akhir < 60 :
    print ("Dalam Huruf : C")
elif 50 <= nilai_akhir < 55 :
    print ("Dalam Huruf : C-")
elif 30 <= nilai_akhir < 50 :
    print ("Dalam Huruf : D")
elif nilai_akhir < 30 :
    print ("Dalam Huruf : E")
else :
    print ("Tidak Lulus")