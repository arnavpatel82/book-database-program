from models import (Base, session, Book, engine) 
import csv
import datetime


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

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)



def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')

        for row in data:
            pass

    



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
    # app()
    clean_date('October 25, 2017')

