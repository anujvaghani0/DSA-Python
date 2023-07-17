n = 5
# for i in range(n):
#     for j in range(i + 1):
#         print("X", end="")
#     print(end="\n")
#
#
# # Path: pattern/p2.py
# for i in range(n):
#     for j in range(n - i):
#         print("X ", end=" ")
#     print(end="\n")
# #
# Path: pattern/p4.py
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print(end="\n")
#
# Path: pattern/p5.py
# for i in range(0, n * 2):
#     if i < n:
#         for j in range(i + 1):
#             print("X", end=" ")
#     else:
#         for j in range(n * 2 - i - 1):
#             print("X", end=" ")
#     print(end="\n")
#
# # Path: pattern/p6.py
# for i in range(n):
#     for space in range(0, n - i - 1):
#         print(" ", end=" ")
#     for j in range(i + 1, 0, -1):
#         print("X", end=" ")
#     print()
#
# Path: pattern/p7.py
# for i in range(n):
#     for space in range(0, i):
#         print(" ", end=" ")
#     for j in range(n - i, 0, -1):
#         print("X", end=" ")
#     print()
#
# Path: pattern/p8.py
# for i in range(n):
#     for space in range(n - i - 1):
#         print(" ", end=" ")
#     for j in range(i + 1):
#         print("X", end=" ")
#     for j in range(i, 0, -1):
#         print("X", end=" ")
#     print()
#
# Path: pattern/p9.py
# for i in range(n):
#     for space in range(0, i):
#         print(" ", end=" ")
#     for j in range(n - i):
#         print("X", end=" ")
#     for j in range(n - i - 1, 0, -1):
#         print("X", end=" ")
#     print()
#
# Path: pattern/p10.py
# for i in range(1, n + 1):
#     c = 65
#     for j in range(1, i + 1):
#         print(chr(c + (n - j)), end=" ")
#     print(end="\n")
#
# Path: pattern/p11.py
# check = True
# lower = 97
# upper = 65
#
# for i in range(n):
#     for j in range(i + 1):
#         if check:
#             print(chr(lower + j), end=" ")
#             check = False
#         else:
#             print(chr(upper + j), end=" ")
#             check = True
#         lower += 1
#         upper += 1
#     print()
#
# Path: pattern/p12.py
# for i in range(n):
#     for j in range(n - i):
#         print(chr(65 + (n - j - 1)), end=" ")
#     print()
#
# Path: pattern/p13.py
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for space in range((n * 2) - i - 2):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#
# Path: pattern/p14.py
# for i in range(1, n + 1):
#     for space in range(n * 2 - i):
#         print(" ", end=" ")
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     for j in range(2, i + 1):
#         print(j, end=" ")
#     print()