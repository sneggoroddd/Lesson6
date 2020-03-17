from functions import salary, hello_who

'''проверяем отдельно функцию'''
print(hello_who('Max'))
print(salary(2, 10))
if salary(2,10) != 40:
    print('failed')
if hello_who('Max') != 'Hello, Max':
    print('Failed')
print('ok')

