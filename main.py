import datetime


class Library:
    def __init__(self):
        self.members = Memberlist()
        self.books = Catalog()

    def add_member(self, name, id_no, address):
        member = Member(name, id_no, address)
        return self.members.insert_member(member)

    def get_members(self):
        return self.members

    def get_books(self):
        return self.books

    def add_book(self, title, author, id_no):
        book = Book(title, author, id_no)
        return self.books.insert_book(book)

    def all_books(self):
        return self.books.get_books()

    def issue_book(self, id_no):
        search_member = self.members.search(id_no)
        if search_member is None:
            return 'User not found'
        else:
            print('==================================')
            print(f'User found -------------> {search_member.name.upper()}')
            print('==================================')
            book_id = input('Enter book id: ')
            search_book = self.books.search(book_id)
            if search_book is None:
                return 'Book not found'
            else:
                return search_member.issue_book(search_book)

    def return_book(self, id_no):
        search_member = self.members.search(id_no)
        if search_member is None:
            return 'User not found'
        else:
            search_memberbooks = search_member.get_booksissued()
            books = list(map((lambda obj: (obj.title, obj.id_no)), search_memberbooks))
            print(books)
            book_id = input('Enter Book id: ')
            result = [obj for obj in search_member.get_booksissued() if obj.id_no == book_id]
            if result:
                return search_member.return_book(result[0])
            else:
                return 'Error Book not found'

    def remove_book(self, book_id):
        search_book = self.books.search(book_id)
        if search_book:
            index = self.books.index(search_book)
            self.books.pop(index)
            return f'{search_book.title} REMOVED'
        else:
            return 'Book doesnt exist'
    
    def print_transactions(self, id_no, month, date):
        search_member = self.members.search(id_no)
        if search_member:
            return search_member.get_transactions(month, date)
        else:
            return 'member not found'

    def search_member(self, id_no):
        return self.members.search(id_no)

            

class Memberlist(list):
    def search(self, id_no):
        result = [obj for obj in self if str(obj.id_no) == str(id_no)]
        member = result[0]
        if member:
            return member
        else:
            return None


    def insert_member(self, member):
        self.append(member)
        return 'New member Added'


class Catalog(list):
    def search(self, id_no):
        result = [obj for obj in self if str(obj.id_no) == str(id_no)]
        book = result[0]
        if book:
            return book
        else:
            return None

    def get_books(self):
        return self

    def insert_book(self, book):
        self.append(book)
        return 'Book added'


class Member:
    def __init__(self, name=None, id_no=None, address=None):
        self.name = name
        self.id_no = id_no
        self.address = address
        self.book_onhold = []
        self.transactions = []
        self.books_issued = []

    def issue_book(self, book):
        date = datetime.date.today()
        content = f'Issued with book {book.title.upper()}'
        trans = Transaction(date, content)
        self.transactions.append(trans)
        return book.issue(self)

    def get_booksissued(self):
        return self.books_issued

    def return_book(self, book):
        date = datetime.date.today()
        content = f'Retured book {book.title.upper()}'
        trans = Transaction(date, content)
        self.transactions.append(trans)
        return book.return_book(self)

    def get_transactions(self, month, date):
        result = [obj for obj in self.transactions if str(obj.date.month) == str(month) and str(obj.date.day) == str(date)]
        if not result:
            print('No transactions on that date')
        else:
            count = 1
            for a in result:
                print(f'{count}. {a.transactions}')
                count = count + 1 


class Book:
    def __init__(self, title, author, id_no):
        self.title = title
        self.author = author
        self.id_no = id_no
        self.borrower = None
        self.holds = None
        self.duedate = None

    def issue(self, member):
        today = datetime.date.today()
        if self.borrower is None:
            self.borrower = member
            while True:
                try:
                    days = int(input('Enter no of days: '))
                    if days > 14:
                        print('No of days should be 14 or less')
                        continue
                except ValueError:
                    continue
                break
            self.duedate = today + datetime.timedelta(days=days)
            member.books_issued.append(self)
            return f'{self.title.upper()} issued =======> {member.name}\n\nDue date =====> {self.duedate}'
        else:
            return 'Book already has a borrower'

    def return_book(self, member):
        self.borrower = None
        member.books_issued.clear()
        return 'Book has been returned'

class Transaction:
    def __init__(self, date=None, transactions=None):
        self.date = date
        self.transactions = transactions

