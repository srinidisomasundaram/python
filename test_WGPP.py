from WGPP import Birthday, WGPP
from datetime import *
import pytest

def test_01():
        with open("C:\\Users\\Srinidi.S.S\\Desktop\\python_tasks_2\\finalapplication\\wgpp_testcase2.txt",mode='r') as a_file:
                b = WGPP()
                first_line = (a_file.readline()).strip()
                dates = first_line.split(',')
                renewal_date = date(int(dates[0]),int(dates[1]),int(dates[2]))
                
                for line in a_file:
                        data = line.split(" ",1)
                        now = data[0].split(',')
                        today = date(int(now[0]),int(now[1]),int(now[2]))
                        expected = b.validity_check(renewal_date,today)
                        print("DOB : {}\nSystem Date:{}\nExpected Output: {}\nActual Output: {}\n".format(renewal_date,today,expected,data[1].strip()))
                        assert expected == data[1].strip()
                    

