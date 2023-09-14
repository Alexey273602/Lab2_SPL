def is_anagramm(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    str2.sort()
    str1.sort()
    if str1 == str2:
        print("Данные строки являются анаграммами")
    else:
        print("No")


stroka1 = input()
stroka2 = input()
is_anagramm(stroka1, stroka2)
