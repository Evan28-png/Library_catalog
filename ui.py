from main import Library
import sys

class Interface:
    def __init__(self):
        self.library = Library()
        self.choice = {'1': self.register_member, '2': self.add_books, '3': self.issue_book, '4': self.return_book, '7': self.remove_book, '8': self.print_transaction, '9': self.all_members, '10': self.all_books, '11': self.search_member, '0': self.exit}

    def display(self):
        print("""
                    LIBRARY MENU
                    ========================
                    1. Register member
                    2. Add books
                    3. Issue book
                    4. Return book
                    7. Remove book
                    8. Print transaction
                    9. All members
                    10. All books
                    11. Search member
                    """)

    def run(self):
        self.display()
        while True:
            choice = input('Enter choice:\n')
            if choice:
                action = self.choice.get(choice)
                if action:
                    action()



    def register_member(self):
        while True:
            name = input('Enter your name: ')
            address = input('Enter your address: ')
            id_no = input('Enter your id no: ')
            print(self.library.add_member(name, id_no, address))
            choice = input('Do you want to add another:(YES/NO) ')
            if choice.lower() == 'yes':
                continue
            else:
                break

    def add_books(self):
        while True:
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            id_no = input('Enter book id no : ')
            print(self.library.add_book(title, author, id_no))
            choice = input('Do you want to add more books:(YES/NO) ')
            if choice.lower() == 'yes':
                continue
            else:
                break
             
    def issue_book(self):
        id_no = input('Enter member id no: ')
        print(self.library.issue_book(id_no))


    def return_book(self):
        member = input('Enter member id')
        print(self.library.return_book(member))

    def remove_book(self):
        book_id = input('Enter book id')
        return self.library.remove_book(book_id)

    def print_transaction(self):
        id_no = input('Enter member id no: ')
        month = input('Enter month: ')
        date = input('Enter date of month: ')
        print(self.library.print_transactions(id_no, month, date))

    def all_members(self):
        print(self.library.get_members())

    def all_books(self):
        print(self.library.get_books())

    def search_member(self):
        id_no = input('Enter id no: ')
        print(self.library.search_member(id_no))

    def exit(self):
        print('Exiting............')
        sys.exit()


if __name__ == '__main__':
    ui = Interface()
    ui.run()
