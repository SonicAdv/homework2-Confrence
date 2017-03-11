#!/usr/bin/env python3

class Employee(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.salary_table = {
            'manager': 50000,
            'director': 20000,
            'staff': 10000
        }

    def salary(self):
        return self.salary_table[self.title]

    def introduce(self):
        print('Hi,all. My name is {}'.format(self.name))
        print('My title is {}, and my salary is a secret...'.format(self.title))
        print('OK, salary is {}'.format(self.salary()))


staffInfo = {
    'sonic': 'manager',
    'tom': 'director',
    'jerry': 'director',
    'amanda': 'staff',
    'Bella': 'staff',
    'Carry': 'staff',
    'Dolce': 'staff',
    'Emma': 'staff'
}


def conference_a():
    for name in staffInfo:
        employee = Employee(name, staffInfo[name])
        employee.introduce()


def what_will_happen():
    return 'sonic', 'male', 34


def main():
    print('This is Sonics homework2.')
    conference_a()
    name, gend, age = what_will_happen()
    print('name={}, gender={}, age={}'.format(name, gend, age))
    #name2, gend2, age2, title2 = what_will_happen()
    #print('name2={}, gender2={}, title2={}'.format(name2, gend2, title2))  



if __name__ == '__main__':
    main()
