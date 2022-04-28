
class Human:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hi, my name is %s." %self.name)
    def __iter__(self, items):
        self.items = items
    def __getitem__(self, index):
            return self.items[index]
iterable_2 = Human(["James", "Peter", "Kyle", "Lewis", "Kevin"])
human_j = Human("John")
human_j.sayHi()

class Adult(Human, worker1):
    worker1 = "Peter"
    increase_amount = 1.04
    number_of_adults = 0
def __init__(self, first, pay):
    self.first = first
    self.pay = pay
    self.email = f'{first}@company.ua'
    Adult.number_of_adults += 1
def __iter__(self, items):
    self.items = items
def __getitem__(self, index):
    return self.items[index]
iterable_3 = Human(["James", "Peter", "Kyle", "Lewis", "Kevin"])
human_j = Human("John")
human_j.sayHi()
def fullname(self):
    return f'{self.first}'

def pay_increase(self):
    self.pay *= self.increase_amount

def __repr__(self):
    return f"Adult({self.first}, {self.pay})"

def worker(self, name1):
    self.name1 = name1
def abc(self):
    print("Hi, my name is %s. I earn %salary" % self.name % salary)
salary = 20000
emp_1 = Adult('Peter')
print(emp_1)


class Student(Adult):
    def __getitem__(self, index):
        return self.items[index]
iterable_4 = Student(["James", "Peter", "Kyle", "Lewis", "Kevin"])
human_j = Student("John")
human_j.sayHi()
student = "James"
number_of_students = 0
def __iter__(self, items):
    self.items = items


def func(self, first):
    self.first = first
    self.email = f'{first}@school.ua'
    Adult.number_of_adults += 1

def represent(self):
    return f"Student({self.first}, {self.pay})"


def student(self, name1):
    self.name1 = name1


def abcd(self):
    print("Hi, my name is %s. I study" % self.name)

stud_1 = Student('James')
print(stud_1)
class Child:
    def __getitem__(self, index):
        return self.items[index]
    iterable_7 = (["James", "Peter", "Kyle", "Lewis", "Kevin"])
human_j = Child("John")
human_j.sayHi()
def __iter__(self, items):
    self.items = items
child = "Jordan"
number_of_students = 0
def func1(self, first):
    self.first = first
    self.email = f'{first}'
    Adult.number_of_adults += 1
def represent1(self):
    return f"Student({self.first}, {self.pay})"
def child(self, name1):
    self.name1 = name1
def abcd1(self):
    print("Hi, my name is %s." % self.name)
child_1 = Child('James')
print(child_1)
class Worker(Human):
    def __getitem__(self, index):
        return self.items[index]
    iterable_8 = (["James", "Peter", "Kyle", "Lewis", "Kevin"])
human_j = Worker("John")
human_j.sayHi()
def __iter__(self, items):
    self.items = items
worker = "Joe"
increase_amount = 1.04
number_of_adults = 0
def __init__1(self, first, pay):
    self.first = first
    self.pay = pay
    self.email = f'{first}@company.ua'
    Adult.number_of_adults += 1


def fullname2(self):
    return f'{self.first}'


def pay_increase2(self):
    self.pay *= self.increase_amount


def __repr__1(self):
    return f"Adult({self.first}, {self.pay})"


def worker2(self, name1):
    self.name1 = name1


def abc2(self):
    print("Hi, my name is %s. I earn %salary1" % self.name % salary1)


salary1 = 20000
emp_1 = Adult('Peter')
print(emp_1)

class Teacher(Worker):
    def __getitem__(self, index):
        return self.items[index]
    iterable_7 = (["James", "Peter", "Kyle", "Lewis", "Kevin"])
    human_j = Student("John")
    human_j.sayHi()
    def __iter__(self, items):
        self.items = items
    teacher = "Erica"
    increase_amount = 1.04
    number_of_students = 0
    if human_j not in ["James", "Peter", "Kyle", "Lewis", "Kevin"]:
        raise ValueError(f'{human_j} has to be a student!')
def __init__2(self, first, pay):
    self.first = first
    self.pay = pay
    self.email = f'{first}@company.ua'
    Teacher.number_of_adults += 1
def __init__3(self, first, last):
    self.first = first
    self.last = last
    print('RealPerson.__init__() ->')
    super().__init__(first, last)
    print('RealPerson.__init__() <-')

def fullname3(self):
    return f'{self.first}'


def pay_increase3(self):
    self.pay *= self.increase_amount


def __repr__2(self):
    return f"Teacher({self.first}, {self.pay})"


def worker3(self, name1):
    self.name1 = name1


def abc3(self):
    print("Hi, my name is %s. I earn %salary2. I teach James" % self.name % salary2)


salary2 = 25000
teacher_1 = Teacher('Erica')
print(teacher_1)
