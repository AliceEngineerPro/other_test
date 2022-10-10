# coding: utf8
""" 
@File: main.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/10 10:04
"""

import os

import path


def write_file():

    if not os.path.exists(os.path.join(os.getcwd(), 'testing')):
        os.makedirs('testing')

    for count in range(100):
        file_name = f'testing/python_file_{count}.py'
        with open(file=file_name, mode='w+', encoding='utf-8') as file:
            for _ in range(1000000):
                if not os.path.getsize(filename=file_name) > 1024 * 3:
                    file.write('print("I Love Python")\n')
                else:
                    break
            file.close()


if __name__ == '__main__':
    write_file()
