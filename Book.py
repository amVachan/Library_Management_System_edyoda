from Book_item import  Bookitem


class Book:
   
    def __init__(self,name,author,pages,published_date):
        self.name=name
        self.author=author
        self.pages=pages
        self.published_date=published_date
        self.Book_items=[] # stores the copies of the book as book items
        self.Book_count=0  # Keeps count of copies of the book
    
    def __repr__(self):
        return self.name+' by '+self.author
    
    #Method to add a book item
    def addBookItem(self,isbn,Rack):
        b=Bookitem(self,isbn,Rack)
        self.Book_items.append(b)
        self.Book_count+=1
        return b
    
    #Method to remove a book item
    def removeBookItem(self,Book_item):
        if Book_item in self.Book_items:
            self.Book_items.remove(Book_item)
            self.Book_count-=1

    # Method to Search a book item
    def searchBookItem(self,isbn):
        for book_item in self.Book_items:
            if isbn.strip() == book_item.isbn:
                return (book_item)

    # Method to print the book items of the book
    def printBook(self):
        for Book in self.Book_items:
            print(Book,end='\n\n')
            
    
            
   
            