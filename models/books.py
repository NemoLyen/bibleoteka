from models.model import Model

class books(Model):
    __nameTable = 'books'
    __Name = 'Name'
    __Author = 'Author'
    __Publishers = 'Publishers'
    __Year_P = 'Year_P'
    __Cost = 'Cost'
    __Scientific = 'Scientific'

    def get(self):
        return super().get(self.__nameTable)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def add(self):
        Name = input("Введите имя: ")
        Author = input("Введите имя автора книги: ")
        Publisher = input("Введите издательство книги: ")
        Year_P = input ("Введите год написания книги: ")
        Cost = input("Введите стоимость одного экземпляра: ")
        Scientific = input("Введите Scientific: ")
        str = f"{self.__Name}, {self.__Author}, {self.__Publishers}, {self.__Year_P}, {self.__Cost}, {self.__Scientific}"
        super().add(self.__nameTable, str, Name, Author, Publisher, Year_P, Cost, Scientific)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)