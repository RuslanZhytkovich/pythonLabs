# Вариант 3
import datetime

class Person():


    def __init__(self, name='Руслан', surname='Житкович', birth_year = 2003):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year



    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_birth_year(self):
        return self.birth_year

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def get_age(self):
        return datetime.datetime.today().year - self.birth_year



    def enter_data(self):
        self.name = input('Введите имя')
        self.surname = input('Введите фамилию')
        self.birth_year = int(input('Введите год рождения'))

    def print_info(self):
        return self.name,self.surname,self.birth_year





class Enrolle(Person):
    def __init__(self, name='Петя', surname='Булатов', birth_year = 2005, faculty = 'FCP'):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.faculty = faculty





class Student(Enrolle):

    def __init__(self, name='Петя', surname='Булатов', birth_year = 2005, faculty = 'FCP', course = 2):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.faculty = faculty
        self.course = course








if __name__ == '__main__':
    lst = []

    petya = Enrolle()
    misha = Enrolle('Миша','Угрумов', 2004, 'FKSIS')
    katya = Enrolle('Катя','Задорнова',2004,'FKSIS')

    vasya = Student()
    zhenya = Student('Евгений','Мальцев', 2000, 'FCP', 4)
    pasha = Student('Павел', 'Кириянов', 2001, 'FCSIS', 3)

    lst.append(petya)
    lst.append(vasya)
    lst.append(misha)
    lst.append(katya)
    lst.append(pasha)



    board1 = int(input('Введите левую границу возраста: '))
    board2 = int(input('Введите правую границу возраста: '))

    for i in range(len(lst)):
        if (lst[i].get_age() >= board1 and lst[i].get_age() <= board2):
            print(lst[i].print_info())








