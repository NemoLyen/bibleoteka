from models.model import Model
class vault(Model):
    __nameTable = 'vault'
    __FIO_Leader = 'FIO_Leader'
    __Address = 'Address'
    __Phone = 'Phone'
    __Capacity = 'Capacity'

    def get(self):
        return super().get(self.__nameTable)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def add(self):
        FIO_Leader = input("Введите имя лидера: ")
        Address = input("Введите адрес: ")
        Phone = input("Введите телефон: ")
        Capacity = input ("Введите вместимость: ")
        str = f"{self.__FIO_Leader}, {self.__Address}, {self.__Phone}, {self.__Capacity}"
        super().add(self.__nameTable, str, FIO_Leader, Address, Phone, Capacity)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)