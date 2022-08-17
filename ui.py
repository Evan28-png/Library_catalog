class Interface:
    def display(self):
        while True:
            print("""
                    LIBRARY MENU
                    ========================
                    1. Register member
                    2. Add books
                    3. Issue book
                    4. Return book
                    7. Remove book
                    8. Print transaction
                    9. Place hold
                    10.Remove hold
                    11.Renew book
                    12.Notify availability
                    """)

    def register_member(self):
        pass
    def add_books(self):
        pass
    def issue_book(self):
        pass
    def return_book(self):
        pass
    def remove_book(self):
        pass
    def print_transaction(self):
        pass
    def place_hold(self):
        pass
    def remove_hold(self):
        pass
    def renew_book(self):
        pass
    def notify_availability(self):
        pass


i = Interface()
i.display()
