try:
    file1 = open("text.txt", "r", encoding="utf-8")#открываем файл для чтения
except FileNotFoundError:#исключаем ошибку
    print("Ошибка: Файл 'text.txt' не найден")#выводим ошибку если файл не найден
    exit()#выходим
file2 = open("output.txt", "w", encoding="utf-8")#открываем файл для записи
num_str = 1#задаем начальный номер строки
try:
    str1 = file1.readline()#читаем первую строку
    while str1: #цикл продолжается, пока есть строки для чтения
        str_with_num = str(num_str) + ": " + str1#формируем строку с номером
        file2.write(str_with_num)#записываем строку в выходной файл
        num_str = num_str + 1#увеличиваем номер строки
        str1 = file1.readline()#читаем следующую строку
except Exception as e:#исключаем ошибку
    print(f"Ошибка при обработке файла: {e}")#выводим ошибку при обработке файла
finally:
    file1.close()#закрываем файл
    file2.close()#закрываем файл
