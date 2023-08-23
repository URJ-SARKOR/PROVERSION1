# def spammer(message: list) -> int:
#     return len(message)
# print(spammer([1, 65, 'str', ['test']]))
# print(spammer(55))



# m  =  43
# spam = 'Hello'
# summa = None


# try это "БЛОК"
# try:
#     summa = m + spam
# except TypeError:
#     print("Передай норм значения")
# print(summa)




# a = (10, 12, 234)
#
# try:
#     a.append(678)
# except Exception:
#     print('Дай норм значения')
#     print(a)


# spammer = (12, 54, 104)
# summa = None
#
# try:
#     summa = spammer.a(15)
# except (TypeError, AttributeError):
#     print("Передай норм значение")







import logging

logging.basicConfig(filemode='w', level=logging.DEBUG, format="%(name)s  %(levelname)s  %(process)d  %(asctime)s  %(message)s" , filename='my_logs.log')


m = int
spam = 'Привет'
summa = None

try:
    logging.info('Двойной привет')
    summa = m * spam
except Exception:
    logging.error('error;(')