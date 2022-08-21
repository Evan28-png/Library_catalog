import datetime


class Library:
    def __init__(self):
        self.members = Memberlist()
        self.books = Catalog()

    def add_member(self, name, id_no, address):
        member = Member(name, id_no, address)
        return self.members.insert_member(member)

    def get_members(self):
        pass

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



            
class Memberlist(list):
    def search(self, id_no):
        for member in self:
            if str(member.id_no) == str(id_no):
                return member
            else:
                return None

    def insert_member(self, member):
        self.append(member)
        return 'New member Added'


class Catalog(list):
    def search(self, id_no):
        for book in self:
            if str(book.id_no) == str(id_no):
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
        return book.issue(self)

    def get_booksissued(self):
        return self.books_issued

    def return_book(self, book):
        return book.return_book(self)



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
                    days = int(input('Enter no of days'))
                    if days > 14:
                        print('No of days should be 14 or less days')
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


