# вывести четыре символа из центра строки

print("Предложение:«Мы обязательно научимся программировать!».")

i = 'Мы обязательно научимся программировать!'

k = len(i) // 2 -2 

j = len(i) // 2 + 2 

print("Длинна строки: ", k )

print("Четыре символа из центра строки:", i[k:j])