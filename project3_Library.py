class Member:
    def __init__(self, bookList):
        self.book=bookList

    def borrowBook(self):
        self.bookName=input("Enter name of Book that you want to borrow: ")
        
    def returnBook(self):
        self.bookName=input("Enter name of book you want to return/donate: ")

class Library(Member):
    def displayBook(self):
        print("Books available in library: ")
        for book in self.book:
            print("•"+book)

    def borrow(self, bookName):
        self.bookName=bookName
        if self.bookName in self.book:
            print("Thanks for using Coders Library.")
            self.book.remove(self.bookName)
        else:
            print("The book is currently not available. Please try again later or borrow any other book.")

    def retur(self, bookName):
        self.bookName=bookName
        self.book.append(self.bookName)
        print("Thanks for Returning/Donating the book.")

if __name__=="__main__":
    book=Library(["Python","C","Java","C++","C#"])
    while(True):
        welcome='''************ Welcome to Coders Library! ************
            Feel free to borrow any books.
                1. List of available Books
                2. Borrow a book
                3. Return/Donate book
                4. Exit Library'''
        print(welcome)
        choice=int(input("Enter your choice: "))
        if choice==1:
            book.displayBook()
        elif choice==2:
            book.borrowBook()
            book.borrow(book.bookName)
        elif choice==3:
            book.returnBook()
            book.retur(book.bookName)
        elif choice==4:
            exit()
        else:
            print("Please enter valid choice.")
