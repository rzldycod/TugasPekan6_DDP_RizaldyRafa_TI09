# numbers = [
#   951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
# ]

# i = 0
# while i < len(numbers):
#     if numbers[i] %2 != 0:
#         print(numbers[i], end=" ")
#     if numbers[i] == 553:
#         break
#     i += 1

# start, end = 951, 527

# for num in range(start, end +1):
#     if num %2 !=0:
#         print(num, end=" ")

# ====================================================================

# # Meminta input jumlah baris
# jumlah_baris = int(input("Masukkan jumlah baris: "))

# # Menggunakan loop for dengan range
# for i in range(1, jumlah_baris + 1):
#     for j in range(i):
#         print("*", end="")
#     print()  # Untuk pindah ke baris berikutnya

# string = " "
# bar = 1

# x = int (input("masukkan angka = "))

# while bar <= x:
#     kol = bar

#     while kol > 0:
#         string = string + "*"
#         kol = kol - 1
#     string = string + "\n"
#     bar = bar +1
#     print(string)

    # ================================================================

jumlah = 0

for bilangan in range(1, 20, 2):
    jumlah += bilangan

print("1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 =", jumlah)

