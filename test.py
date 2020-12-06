from Book import Book
from Catalog import Catalog
from User import Librarian,Member
catalog=Catalog()

catalog.addBook('Shoe Dog','Phil Knight',312, '2015')
catalog.addBook('Moonwalking with Einstien','J Foer',318, '2017')
catalog.displayBooks()

librarian=Librarian('Kushal','banglr',23,1234567,123)

librarian.addBook('chariats of god','Von Deniken',500,'2000',catalog)



librarian.addBookItem('Shoe Dog','123hg','H1B2',catalog)
librarian.addBookItem('Shoe Dog','123hg','H1B3',catalog)

librarian.addBookItem('chariats of god','154ab','H1A1',catalog)
librarian.addBookItem('chariats of god','154ab','H1A2',catalog)
catalog.displayBooks()

b=librarian.searchBookByName('chariats of god',catalog)
print(b)

librarian.searchBookByAuthor('Von Deniken',catalog)

member1=Member("Vish","Bangalore",23,'asljlkj22','std1233')

member1.DisplayIssuedBooks()

member1.displayBooksIncatalog(catalog)

member1.issueBook('chariats of god',catalog)

member1.DisplayIssuedBooks()

member1.returnBook('chariats of god',catalog)

member1.DisplayIssuedBooks()