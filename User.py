
class User:

    def __init__(self, name, location, age, aadhar_id):
        self.name=name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        
# Librarian Class Inherits User class
class Librarian(User):
    
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
    
    # Librarian can add books to the catalog
    def addBook(self,name,Author,pages,Date,Catalog):
        Catalog.addBook(name,Author,pages,Date)
        
    # Librarian can remove books from the catalog
    def removeBook(self,name,Catalog):
        if name:
            Catalog.Remove_Book(name)
    
    # Librarian can add book items to the catalog
    def addBookItem(self,name,isbn,Rack,Catalog):
        Catalog.addBookItem(name,isbn,Rack)
                
    # Librarian can remove  book items from  the catalog
    def removeBookItem(self,Catalog,name,isbn):
        Catalog.removeBookItem(name,isbn)
    
    # Method to display all the books in the catalog
    def displayBooksInLibrary(self,Catalog):
        return Catalog.Display_Books()

    # Method to search a book by name in the catalog
    def searchBookByName(self,name,catalog):
        return catalog.searchBookByName(name)
                
    # Method to search a book by author name in the catalog
    def searchBookByAuthor(self,author,catalog):
        return catalog.searchBookByAuthor(author)
        
        
    
        
    
        
class Member(User):
    
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.Member_books=[] # Stores the Book items issued to the member 
    
    # Issue Book method is for lending a book item to the member from the catalog
    def issueBook(self,name,Catalog):
        if name:
            book=Catalog.searchBookByName(name)
            if book:
                if book.name.lower() not in [x.Book.name.lower() for x in self.Member_books]:
                    if len(book.Book_items)>0:
                        book_item=book.Book_items[0]
                        self.Member_books.append(book_item)
                        Catalog.removeBookItem(name,book_item.isbn)
                        print(f'book {name} has been issued to {self.name}',end='\n\n')
                    else:
                        print(f'catalog doesnt have any copies left of the book {name}',end='\n\n')
                else:
                    print(f'book {name} has been already issued to {self.name}',end='\n\n')
            else:
                print('catalog does not have the book you requested for,sorry.',end='\n\n')
        else:
            print('provide a proper book name',end='\n\n')
    


    # Return book method is for returning a book item from the member back to the catalog
    def returnBook(self,name,Catalog):
        if name:
            for book_item in self.Member_books:
                if book_item.Book.name.lower()==name.lower():
                    Catalog.addBookItem(name,book_item.isbn,book_item.Rack)
                    self.Member_books.remove(book_item)
                    print(f'book {name} with isbn {book_item.isbn} has been returned to the catalog',end='\n\n')
        else:
            print('please give a correct book name.',end='\n\n')



    # Method to display books issued to the member     
    def DisplayIssuedBooks(self):
        if self.Member_books:
            print ("{:<30} {:<30} {:<30} {:<30} {:<30}".format('Name','Author', 
                    'Pages','Published_date','Copies')) 
            for Book_item in self.Member_books:
                Book=Book_item.Book
                print ("{:<30} {:<30} {:<30} {:<30} {:<30}".format(Book.name, Book.author, 
                    str(Book.pages),Book.published_date,str(len(Book.Book_items)))) 
            print('\n')
        else:
            print('You have no books issued',end='\n\n')

    def displayBooksIncatalog(self,Catalog):
        return Catalog.displayBooks() 
        
    
    # Method to search a book by name in the catalog
    def searchBookByName(self,name,catalog):
        return catalog.searchBookByName(name)
                
    # Method to search a book by author name in the catalog
    def searchBookByAuthor(self,author,catalog):
        return catalog.searchBookByAuthor(author)