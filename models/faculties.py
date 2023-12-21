from models.model import Model

class faculties(Model):
    __nameTable = 'faculties'
    __Name_F = 'Name_F'
    __Dean = 'Dean'
    __Date_F = 'Date_F'

    def get(self):
        return super().get(self.__nameTable)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    # def add(self):
    #     name = input("Введите имя: ")
    #     start_time = input("Введите время старта в формате 1 окт. 2023 г., 12:24:18: ")
    #     finish_time = input("Введите время старта в формате 1 окт. 2023 г., 12:24:18: ")
    #     mountain_id = input ("Введите id горы: ")
    #     str = f"{self.__name}, {self.__start_time}, {self.__finish_time}, {self.__mountain_id}"
    #     super().add(self.__nameTable, str, name, start_time, finish_time, mountain_id)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)
