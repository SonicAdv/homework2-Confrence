#!/usr/bin/env python3


def main():
    print('This is Sonics homework2.')


class Employee(object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.salary_table = {
            'Manager': 50000,
            'Director': 20000,
            'Staff': 10000
        }

    def introduce(self):
        print('Hi,all. My name is {}'.format(self.name))
        print('My title is {}, and my salary is a secret...'.format(self.title))
        print('OK, salary is {}'.format(self.salary_table[self.title]))

staffInfo = {
    'sonic': 'Manager',
    'tom': 'Director',
    'jerry': 'Director',
    'amanda': 'Staff',
    'Bella': 'Staff',
    'Carry': 'Staff',
    'Dolce': 'Staff',
    'Emma': 'Staff'
}


def confrence_a():
    for name in staffInfo:
        employee = Employee(name, staffInfo[name])
        employee.introduce()

if __name__ == '__main__':
    main()
    confrence_a()
