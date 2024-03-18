a = 15
if a > 9:
    print("Правда")
if a > 15:
    print("Правда")  # Не правда
b, c = 22, 43
if b > c:
    print("Правда")  # Не правда
if b > a and a < c:
    print("Правда")
if (c > b) and (67 > a):
    print("Правда")
if '115' > '348':
    print("Правда")  # Не правда
if '348' == '348':
    print("Правда")
if [5, 7] != [7, 5]:
    print("Правда")
d = 'ром'
e = [12, True]
# if b > d:
    #  print("Правда") ошибка: TypeError: '>' not supported between instances of 'int' and 'str'
# if e = a:
    #  print("Правда") ошибка: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if e != a:
    print("Правда")