from Book import Book


class Catalog:
    
    def __init__(self):
        self.Book_count=0 #keeps the total book count in the catalog
        self.Books=[] # Stores all the book items in the catalog
    
    
    # Method to display all the books in the catalog with their details
    def displayBooks(self):
        print ("{:<30} {:<30} {:<30} {:<30} {:<30}".format('Name','Author', 
                'Pages','Published_date','Copies')) 
        for Book in self.Books:
            print ("{:<30} {:<30} {:<30} {:<30} {:<30}".format(Book.name, Book.author, 
                str(Book.pages),Book.published_date,str(len(Book.Book_items)))) 
        print('\n')


    # Method to add a book to the catalog
    def addBook(self,name,author,pages,Date):
        b=Book(name,author,pages,Date)
        self.Books.append(b)
        self.Book_count+=1
        print(f'{name} is added successfully to the catalog',end='\n\n')

    # Method to remove book from the catalog   
    def removeBook(self,name):
        flag=False
        for book in self.Books:
            if book.name.lower()==name.lower():
                self.Books.remove(book)
                flag=True
        if flag:
            print(f'{book.name} is removed Successfully',end='\n\n')
        else:
            print(f'{book.name} is not in the catalog',end='\n\n')
    
    # Method to add a book item to the catalog
    def addBookItem(self,name,isbn,Rack):
        book=self.searchBookByName(name)
        book.addBookItem(isbn,Rack)
        self.Book_count+=1
        print (f'{book.name} with isbn {isbn} added to the Rack {Rack}',end='\n\n')

    # Method to remove a book item from the catalog
    def removeBookItem(self,name,isbn):
        if name:
            book=self.searchBookByName(name)
            book_item=book.searchBookItem(isbn)
            book.removeBookItem(book_item)
            self.Book_count-=1
            print (f'{book.name} with isbn {isbn} was removed from the Rack {book_item.Rack}',end='\n\n')

    # Method to search a book by it's name
    def searchBookByName(self,name):
        if name:
            for book in self.Books:
                if book.name.lower()==name.lower():
                    return (book)

    # Method to search a book by it's author name
    def searchBookByAuthor(self,author):
        if author:
            for book in self.Books:
                if book.author.lower()==author.lower():
                    print (book)
        
    