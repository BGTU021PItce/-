# расчитываем сколько полных часов и минут находиться секундах

print("Ваша задача ввести кол-во секунд:")
n = int(input())

if n < 0:
    print("Секунды не могут быть отрицательными клоун.")
else:
    m = n // 60 #расчитываем минуты
    c = m // 60 #расчитываем часы
    s = n - c * 60 - m * 60 #расчитываем секунды
print("В ", n ,"секундах содержится", c , "часов,", m , "минут, ", s , "Секунд.") 