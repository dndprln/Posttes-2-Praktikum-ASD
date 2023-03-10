# Nama: Adinda Apriliani
# NIM: 2209116024
# Kelas: A Sistem Informasi 2022


# Soal:
# var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Buatlah sebuah program python yang dapat mencari data-data yang sudah di sediakan dengan output
# 1. Arsel di Index 0, Avivah di Index 1, Daiva di Index 2
# 2. Wahyu di Index 3 pada kolom 0
# 3. Wibi di Index 3 pada kolom 1

# Ketentuan 
# 1. Menggunakan algoritma searching yang sudah dipelajari ataupun algoritma lain untuk poin tambahan.
# 2. Buatlah Dokumentasi yang meliputi informasi yang menjelaskan cara kerja program, fungsionalitas program, 
#    algoritma yang digunakan, dan setiap elemen yang digunakan dalam program.
# 3. Kumpulkan dalam bentuk link repository github masing-masing.
# 4. Dokumentasi dapat berupa notion, README.md pada github, ataupun video. (PDF TIDAK DIPERBOLEHKAN)

# Tambahan
# 1. Menggunakan 2 atau lebih algoritma akan mendapatkan nilai tambahan.
# 2. Dokumentasi berupa video akan mendapatkan nilai tambahan.


#Listnya
variabel = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
data2 = []

# Elemen yang akan dicari
x1 = "Arsel"
x2 = "Avivah"
x3 = "Daiva"
x4 = "Wahyu"
x5 = "Wibi"


# ========== 1. Fungsi Mencari Arsel ==========
def searching_Arsel(variabel, x1):
    n = len(variabel)
    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x1 (input)
    prev = 0
    while variabel[min(step, n) - 1] < x1:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while variabel[prev] < x1:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if variabel[prev] == x1:
        return prev

    return -1

# === Fungsi Hasil dari Searching Arsel ===
def result_1():
    result1 = searching_Arsel(variabel, x1)
    if result1 == -1:
        print(f"Elemen {x1} tidak ditemukan")
    else:
        print(f"Elemen Arsel ditemukan pada index ke - {result1}")
    back()


# ========== 2. Fungsi Mencari Avivah ==========
def searching_Avivah(variabel, x2):
    n = len(variabel)
    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x2 (input)
    prev = 0
    while variabel[min(step, n) - 1] < x2:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while variabel[prev] < x2:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if variabel[prev] == x2:
        return prev

    return -1

# === Fungsi Hasil dari Searching Avivah ===
def result_2():
    result2 = searching_Avivah(variabel, x2)
    if result2 == -1:
        print(f"Elemen {x2} tidak ditemukan")
    else:
        print(f"Elemen Avivah ditemukan pada index ke - {result2}")
    back()


# ========== 3. Fungsi Mencari Daiva ==========
def searching_daiva(variabel, x3):
    n = len(variabel)
    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x3 (input)
    prev = 0
    while str(variabel[min(step, n)-1]) < x3 :
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while variabel[prev] < x3:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if variabel[prev] == x3:
        return prev

    return -1

# === Fungsi Hasil dari Searching Daiva ===
def result_3():
    result3 = searching_daiva(variabel, x3)
    if result3 == -1:
        print(f"Elemen {x3} tidak ditemukan")
    else:
        print(f"Elemen Daiva ditemukan pada index ke - {result3}")
    back()


# ========== 4. Fungsi Mencari Wahyu ==========
def searching_wahyu(variabel, x4):
    n = len(variabel)
    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x4 (input)
    prev = 0
    while variabel[min(step, n) - 1] < x4:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while variabel[prev] < x4:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if variabel[prev] == x4:
        return prev

    return -1

# === Fungsi Hasil dari Searching Wahyu ===
def search4():
    print("Hasil dari pencaharian Wahyu: ")
    for i in range(len(variabel)):
        if type(variabel[i]) == list :
            isinya = searching_wahyu(variabel[i], x4)
            print("Elemen Wahyu ditemukan pada index ke - ", i, "Kolom", isinya)
        else:
            if variabel[i] == x4:
                print("Wahyu ditemukan pada index ke - ",i)
    
    back()


# ========== 5. Fungsi Mencari Wibi ==========
def searching_wibi(variabel, x5):
    n = len(variabel)
    step = int(n ** 0.5)

    # Mencari block yang berisi elemen x5 (input)
    prev = 0
    while variabel[min(step, n) - 1] < x5:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    # Melakukan linearing di block tersebut
    while variabel[prev] < x5:
        prev += 1

        if prev == min(step, n):
            return -1

    # Cek apakah elemen yang dicari adalah elemen yang sesuai 
    if variabel[prev] == x5:
        return prev

    return -1

# === Fungsi Hasil dari Searching Wibi ===
def search5():
    print("Hasil dari pencaharian Wibi: ")
    for i in range(len(variabel)):
        if type(variabel[i]) == list :
            isinya = searching_wahyu(variabel[i], x5)
            print("Elemen Wibi ditemukan pada index ke - ", i, "Kolom", isinya)
        else:
            if variabel[i] == x5:
                print("Elemen Wibi ditemukan pada index ke - ",i)
    
    back()

# Fungsi untuk menu run program nya
def menu():
    pilih = int(input("Masukkan Pilihan Anda: "))
    if pilih == 1:
        result_1()
    elif pilih == 2:
        result_2()
    elif pilih == 3:
        result_3()
    elif pilih == 4:
        search4()
    elif pilih == 5:
        search5()
    else :
        print("Terimakasih sudah menjalankan program")
    exit()

# Fungsi untuk menu run program nya
def menu1 ():
    print("""
    =============================================
    |                   M E N U                 |
    =============================================
    |   1. Menampilkan Index Arsel              |
    |   2. Menampilkan Index Avivah             |
    |   3. Menampilkan Index Daiva              |
    |   4. Menampilkan Index dan Kolom Wahyu    |
    |   5. Menampilkan Index dan Kolom Wibi     | 
    =============================================
    """)

# Fungsi untuk kembali ke Tampilan Menu
def back():
    print()
    print("===== Pilihan Kembali =====")
    print ("[1] Ya")
    print ("[2] Tidak")
    back = int(input("Apakah Anda ingin kembali ke Menu? [1/2]: "))
    if back == 1 :
        menu1()
        menu()
    else:
        print("Terimakasih sudah menjalankan program")
    exit()

# Program Berjalan
menu1()
menu()