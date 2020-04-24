from WGPP import Birthday
from datetime import *
import pytest
def test_01():
        with open("C:\\Users\\Srinidi.S.S\\Desktop\\python_tasks_2\\finalapplication\\birthday.txt",mode='r') as a_file:
                x = Birthday()
                dob = date(2020,3,15)
                for line in a_file:
                        data = line.split(" ",1)
                        now = data[0].split(',')
                        today = date(int(now[0]),int(now[1]),int(now[2]))
                        expected = x.birthday_check(dob,today)
                        print("DOB : {}\nSystem Date:{}\nExpected Output: {}\nActual Output: {}\n".format(dob,today,expected,data[1].strip()))
                        assert expected == data[1].strip()
                        


