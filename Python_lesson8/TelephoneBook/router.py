# связть между view и dataBase

from view import *
from dataBase import *

def main():
    while True:
        res = select_op()
        match res:
            case 1:
                add_info(get_info())
            case 2:
                killer_ficha(search())
            case 3:
                replace_data(search())
            case 4:
                search_info(search())
            case 5:
                print(book_view())
            case 6:
                break


main()