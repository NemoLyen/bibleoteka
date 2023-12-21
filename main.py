from models.books import books
from models.vault import vault
from models.keeping import keeping
from models.process import process
from models.faculties import faculties
faculties = faculties()
vault = vault()
books = books()
keeping = keeping()
process = process()


vault.add()
print(vault.get())

# print(books.getOneField('Publishers'))