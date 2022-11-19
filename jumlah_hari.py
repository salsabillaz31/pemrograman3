<<<<<<< HEAD
#menentukan tahun kabisat
#sebelum tahun 1582 menggunakan kalender julian
def isLeapYear(year):
    if year > 1582:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return year % 4 == 0

#menentukan jumlah hari dalam satu bulan
def daysInMonth(year, month):
    if(year == 1582 and month == 10):
        return 21  #tanggal 5 s.d 14 oktober 1582 dihapus dari kalender
    elif month == 2: #februari
        return 28 + isLeapYear(year) #28 tahun biasa, tambah sehari untuk kabisat
    #untuk selain februari, bulan yang sisa ganjil ketika dibagi tujuh memiliki 31
    #untuk mengkompensasi dalam perhitungan sengaja bulan dikurangi satu
    else:
        return(31 - (((month -1) %7)%2))

#menentukan urutan haari tanggal tertentu dalam satu tahun
def dayOfYear(year, month, day):
    if (day < 1 or month < 1 or month > 12 or year < 1):
        return None
    elif day > daysInMonth(year, month):
        return None
    else:
        count = 1
        days = day
        while count < month:
            days += daysInMonth(year, count)
            count += 1
        return days
=======
def jumlah_hari(bulan):
    hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= bulan <= 12:
        return hari[bulan-1]
    else:
        return -1

bulan = int(input())
tahun = int(input())
if (bulan == 1):
    hari = 31
elif(bulan == 2):
    if((tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0):
        hari = 29
    else:
        hari=28

elif(bulan == 3):
    hari = 31
elif(bulan == 4):
    hari = 30
elif(bulan == 5):
    hari = 31
elif(bulan == 6):
    hari = 30
elif(bulan == 7):
    hari = 31
elif(bulan == 8):
    hari = 31
elif(bulan == 9):
    hari = 30
elif(bulan == 10):
    hari = 31
elif(bulan == 11):
    hari = 30
elif(bulan == 12):
    hari = 31
else:
    hari = -1
print(hari)
>>>>>>> caca
