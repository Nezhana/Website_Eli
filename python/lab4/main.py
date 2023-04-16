import re

# decorator singleton
# def singleton(cls):
#     instances = {}
#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls()
#         return instances[cls]
#     return getinstance

# metaclass singleton
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=MetaSingleton):

    def some_special_function(self):
        print('This is singleton class')


class Person:

    # constructor
    def __init__(self, fname, lname, age, worker):
        self.firstname = fname #string
        self.lastname = lname #string
        self.age = age #int
        self.worker = worker #bool

    #-------------------------------

    #getters, setters:
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, fname):
        if not isinstance(fname, str):
            raise TypeError('Firstname must be string type!')
        try:
            fname = re.findall(r'[A-Z][A-Za-z]+', fname)[0]
        except IndexError:
            raise ValueError('Your firstname must begin from capital letter!')
        self.__firstname = fname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lname):
        if not isinstance(lname, str):
            raise TypeError('Lastname must be string type!')
        try:
            lname = re.findall(r'[A-Z][A-Za-z]+', lname)[0]
        except IndexError:
            raise ValueError('Your lastname must begin from capital letter!')
        self.__lastname = lname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be integer type!')
        if (1 < age < 99):
            self.__age = age
        else:
            raise ValueError('Age must be in range 1-99!')

    @property
    def worker(self):
        return self.__worker

    @worker.setter
    def worker(self, worker):
        if not isinstance(worker, bool):
            raise TypeError('Worker data must be bool type!')
        self.__worker = worker

    #-------------------------------

    #simple method, returns string
    def get_fullname(self):
        return f'{self.lastname} {self.firstname}' #string, conc

    #print instance
    def __str__(self):
        if(self.worker):
            res = f'{self.lastname} {self.firstname} ({self.age}), worker.'
        else:
            res = f'{self.lastname} {self.firstname} ({self.age}), not a worker.'
        return res

class Employee(Person):

    # constructor
    def __init__(self, fname, lname, age, worker=True, salary=0.0, position=None):
        super().__init__(fname, lname, age, worker)
        self.salary = salary #float
        self.position = position #string

    #getters, setters:
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, int|float):
            raise TypeError('Salary must be int/float type!')
        self.__salary = float(salary) #type conversion

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        if not isinstance(position, str):
            raise TypeError()
        elif not len(position):
            raise ValueError('Program must not be empty!')
        self.__position = position

    #-------------------------------

    #overwriting print instance
    def __str__(self):
        res = f'{self.lastname} {self.firstname} ({self.age}), position: {self.position}, salary: {self.salary}'
        return res


def make_hash_array(array):
    my_dict = {}
    for el in array:
        my_dict[str(el)] = el*el
    return my_dict

def main():

    #hash-array
    my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_dict = make_hash_array(my_array)
    print(my_dict, end='.\n\n')

    #objects:
    tom = Person('Tom', 'Smith', 18, False)
    lily = Employee('Lily', 'Smith', 40, True, 534.5, 'Team Lead')
    print(tom.get_fullname())
    print(tom)
    print(lily.get_fullname())
    print(lily, end='.\n\n')

    #explode (split in python) example:
    expl_explode_1 = "part1 part2 part3 part4 part5"
    expl_explode_2 = "user:password1234:id1023:dir/subdir"
    print(expl_explode_1.split())
    name, pas, ID, dir_path = expl_explode_2.split(':')
    print(f'name: {name}, password: {pas}, id: {ID}, path: {dir_path}', end='.\n\n')

    #implode (join in python) example:
    expl_implode_1 = ['Hello', 'World', 'It\'s', 'Snizhana']
    expl_implode_2 = ['data1', 'data2', 'data3', 'data4']
    print(' '.join(expl_implode_1))
    print('Data:')
    print(';\n'.join(expl_implode_2), end='.\n\n')

    #comparison
    print('Strings:')
    print('123' > '1234') #False
    print('' == '', end='\n\n') #True

    print('Values')
    print(0 == 0.0) #True
    print(0 == 0.00000000001, end='\n\n') #False

    print('Bools')
    print(True > False) #True
    print(True != False, end='\n\n') #True

    #singleton
    s_obj1 = MyClass()
    s_obj2 = MyClass()
    print(f'obj1={id(s_obj1)}, obj2={id(s_obj2)}, comparison={id(s_obj1) == id(s_obj2)}')


if __name__ == '__main__' :
    main()