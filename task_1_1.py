# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#



duration = int(input('Введите число'))
duration_sec = duration % 60
duration_min = duration // 60
duration_hour = duration // 3600
duration_day = duration // 86400

if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    duration_min = duration // 60
    print(duration_min, 'мин', duration_sec, 'сек')
elif duration < 86400:
    duration_min = duration_min % 60
    print(duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')
else:
    duration_min = duration_min % 60
    duration_hour = duration_hour % 24
    print(duration_day, 'дн', duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')