#1
'''
Создать программно файл в текстовом формате, записать в него построчно данные,
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''


f_1 = open("my_homework_file.txt", 'w')
line = input("Введите текст \n")
while line:
    f_1.writelines(line)
    line = input("Введите текст \n")
    if not line:
        break
f_1.close()
f_1 = open("my_homework_file.txt", 'r')
content = f_1.readlines()
print(content)
f_1.close()


##2

my_list = ['Home\n', 'Work\n', 'Five\n']
with open("my_homework_file_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("my_homework_file_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")


#3

with open("my_homework_file_3.txt", 'r') as my_file:
    salary = []
    penny = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           penny.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {penny}, средний оклад {sum(map(int, salary)) / len(salary)}')

#4

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('my_homework_file_4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('my_homework_file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

5

def summary():
    try:
        with open('my_homework_file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

#6


subjects = {}

try:
    with open("my_homework_file_6.txt", 'r') as fh:
        for line in fh.readlines():
            data = line.replace('(', ' ').split()

            subjects[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
except IOError as e:
    print(e)
except ValueError:
    print("Неконсистентные данные")

print(subjects)


#7

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('my_homework_file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('my_homework_file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

