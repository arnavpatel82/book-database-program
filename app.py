import csv
import datetime

from models import (Base, session, Book, engine) 


def menu():
    while True:
        print('''
        \nPROGRAMMING BOOKS
        \r1) Add book
        \r2) View all books
        \r3) Search for book
        \r4) Book analysis
        \r5) Exit''')

        choice = input('What would you like to do')
        if choice in ('1', '2', '3', '4', '5'):
            return choice

# add books to db
# edit books
# delete books
# search books
# data cleaning functions
# loop runs program


    



def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            # view book
            pass
        elif choice == '3':
            # search for book
            pass
        elif choice == '4':
            # book analysis
            pass
        else:
            print('Goodbye')
            app_running


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()

