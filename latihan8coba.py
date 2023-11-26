import sqlite3
import tkinter as tk

def simpan_data_ke_sqlite(NamaSiswa, Biologi, Fisika, Inggris, PrediksiFakultas):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect("TugasDB.db")
    cursor = conn.cursor()
# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi2 
                   (NoUrut INTEGER PRIMARY KEY AUTOINCREMENT,
                   NamaSiswa TEXT,
                   Biologi INTEGER, 
                   Fisika INTEGER,
                   Inggris INTEGER, 
                   PrediksiFakultas TEXT)''')
# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi2 (NamaSiswa, Biologi, Fisika, Inggris, PrediksiFakultas) VALUES (?, ?, ?, ?, ?)", 
                   (NamaSiswa, Biologi, Fisika, Inggris, PrediksiFakultas))
# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

#Fungsi Prediksi fakultas
def Prediksi_Fakultas(Biologi, Fisika, Inggris):
    if Biologi > Fisika and Biologi > Inggris:
        print("Kedokteran") 
        hasil = "Kedokteran"
    elif Fisika > Biologi and Fisika > Inggris:
        print("Teknik")
        hasil = "Teknik"
    else:
        print("Bahasa")
        hasil = "Bahasa"
    return hasil
        

#Fungsi untuk menampilkan 
def tampilkan():
    NamaSiswa = E1.get()
    Biologi = int(E2.get())
    Fisika = int(E3.get())
    Inggris = int(E4.get())
    
    Prediksi = Prediksi_Fakultas(Biologi,Fisika,Inggris)

    hasilMhs = f"Nama Mahasiswa : {NamaSiswa}"
    nilaiB = f"Nilai Biologi :  {Biologi}"
    nilaiF = f"Nilai Fisika :  {Fisika}"
    nialiI = f"Nilai Inggris :  {Inggris}"
    prediksi_hasil = f"Prediksi Fakultas :  {Prediksi}"

    label_hasilnama.config(text=hasilMhs)
    label_hasilnilaiB.config(text=nilaiB)
    label_hasilnilaiF.config(text=nilaiF)
    label_hasilnilaiI.config(text=nialiI)
    label_hasilPrediksi.config(text=prediksi_hasil)

    
    if not Biologi and not Fisika and not Inggris and not NamaSiswa:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlite(NamaSiswa, Biologi, Fisika, Inggris, Prediksi)
        



top = tk.Tk()
top.title("Prediksi Fakultas")

inputframe=tk.LabelFrame(top, labelanchor="n", padx=10, pady=10)
inputframe.pack()

#Membuat judul
var = tk.Label(top, text="Aplikasi Prediksi Fakultas Pilihan")
var.pack()

#Input nama
Input_NamaMhs= tk.Label(inputframe, text="Masukkan Nama Siswa: ")
Input_NamaMhs.grid(row=0, column=0, pady=10)
E1= tk.Entry(inputframe)
E1.grid(row=0,column=1)

#Input nilai Biologi
Input_NilaiBio= tk.Label(inputframe, text="Masukkan Nilai Biologi: ")
Input_NilaiBio.grid(row=1, column=0, pady=10)
E2= tk.Entry(inputframe)
E2.grid(row=1,column=1)

#Input nilai Fisika
Input_NilaiFis= tk.Label(inputframe, text="Masukkan Nilai Fisika: ")
Input_NilaiFis.grid(row=2, column=0, pady=10)
E3= tk.Entry(inputframe)
E3.grid(row=2,column=1)

#Input nilai Inggris
Input_NilaiIng= tk.Label(inputframe, text="Masukkan Nilai Inggris: ")
Input_NilaiIng.grid(row=3, column=0, pady=10)
E4= tk.Entry(inputframe)
E4.grid(row=3, column=1)

#button
button_submit = tk.Button(top, text="Submit", command=tampilkan)
button_submit.pack()

frame_hasil = tk.LabelFrame(top,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

#label hasil
label_hasilnama = tk.Label(frame_hasil, text="")
label_hasilnama.pack()

label_hasilnilaiB = tk.Label(frame_hasil, text="")
label_hasilnilaiB.pack()

label_hasilnilaiF = tk.Label(frame_hasil, text="")
label_hasilnilaiF.pack()

label_hasilnilaiI = tk.Label(frame_hasil, text="")
label_hasilnilaiI.pack()

label_hasilPrediksi = tk.Label(frame_hasil, text="")
label_hasilPrediksi.pack()

top.mainloop()
