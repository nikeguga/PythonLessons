# функции для работы с базой данных, запись/ чтение

def add_info(arg):
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(arg)


def search_info(arg):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = []
        count = 1
        for i in range(len(lst)):
            if arg in lst[i]:
                res.append(lst[i])
                print(f'{count}. {lst[i]}')
                count += 1
            return res

def killer_ficha(arg):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if arg in lst[i]:
                del lst[i]
                file.close
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.writelines(lst)
                                
            


def book_view():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        return file.read()


def replace_data(arg):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            if arg in lst[i]:
                sublist = lst[i].split()
                for j in range(len(sublist)):
                    if arg in sublist[j]:
                        sublist[j] = input("input new data: ")
                        lst[i] = sublist[0] + " " + sublist[1] + " " + sublist[2] + "\n"
                        file.close

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.writelines(lst)
        

