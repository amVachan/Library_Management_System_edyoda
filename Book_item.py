# Book item basically is a copy of a particular book
class Bookitem:

    def __init__(self,Book,isbn,Rack):
        self.Book=Book
        self.isbn=isbn
        self.Rack=Rack
        
    def __repr__(self):
        return self.Book.name+' with isbn '+self.isbn