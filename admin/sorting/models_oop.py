from dataclasses import dataclass

@dataclass
class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1  # self = this(java)
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remain(self):
        return self.num1 % self.num2

@dataclass
class Contacts(object):

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_String(self):
        print(f'[Contacts] \nName: {self.name} \nPhone: {self.phone} \nEmail: {self.email} \nAddress: {self.address}')


def set_contact() -> object:
    return Contacts(input('name'), input('phone'), input('email'), input('address'))


def get_contacts(ls):
    for i in ls:
        i.to_String()


def del_contact(ls, name):
    for i, j in enumerate(ls):
        if name == j.name:
            del ls[i]


def print_menu(ls) -> int:
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

@dataclass
class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3


@dataclass
class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)


@dataclass
class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_String(self):
        print(f'[Person Info] \nname: {self.name} \nAge: {self.age} \nAddress: {self.address}\n')