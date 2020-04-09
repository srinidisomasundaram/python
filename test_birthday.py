from birthday import Birthday
from datetime import *
import pytest
test_inputs = dict( [( (2020,1,1), '2 months from now' ), ( (2020,1,31), '2 months from now' ), ( (2020,2,1), 'Next month' ),
              ( (2020,2,13), 'Next month' ), ( (2020,2,14), '30 days from now' ), ((2020,2,15), 'Next month' ),
              ((2020,2,16),'28 days from now'),((2020,2,17),'After 3 weeks'), ((2020,2,22), 'After 3 weeks'),
              ((2020,2,23),'3 weeks from now'), ((2020,2,24), '20 days from now'), ((2020,2,29), '15 days from now'),
              ( (2020,3,1), '2 weeks from now'), ((2020,3,2), 'Next Sunday'), ((2020,3,8),'Next Sunday'),
              ((2020,3,9),'Coming Sunday'), ((2020,3,10), 'Coming Sunday'), ((2020,3,11), 'Coming Sunday'),
              ((2020,3,12), 'Coming Sunday'), ((2020,3,13), 'Day after Tomorrow'), ((2020,3,14), 'Tomorrow'),
              ((2020,3,15), 'Today'), ((2020,3,16),'Yesterday'), ((2020,3,17), 'Day before yesterday'),
              ((2020,3,18), '3 days back'), ((2020,3,19), '4 days back'), ((2020,3,20), '5 days back'),
              ((2020,3,21),'6 days back'), ((2020,3,22), 'Last Sunday'), ((2020,3,23), 'in the last week'),
              ((2020,3,28), 'in the last week'),( (2020,3,29), '2 weeks ago'), ((2020,4,4), '2 weeks ago'),
              ((2020,4,5),'3 weeks ago'),((2020,4,6), '3 weeks ago'), ((2020,4,11), '3 weeks ago'),
              ((2020,4,12), 'Almost a month ago'), ((2020,4,13), 'Almost a month ago'), ((2020,4,14), 'Almost a month ago'),
              ((2020,4,15), 'Last Month'), ((2020,4,16),'Last Month'),((2020,4,30),'Last Month'),((2020,5,1),'2 months ago'),
              ((2020,5,31),'2 months ago'),((2020,6,1),'3 months ago'), ((2020,7,1),'4 months ago'), ((2020,8,1),'5 months ago'),
              ((2020,9,1),'6 months ago'), ((2020,10,1),'7 months ago'), ((2020,11,1),'8 months ago'), ((2020,12,1),'9 months ago')] )

@pytest.mark.parametrize('k',test_inputs)
def test_case_01(k):
        x = Birthday()
        dob = date(2020,3,15)
        today = date(k[0],k[1],k[2])
        expected = x.birthday_check(dob,today)
        print("DOB : {}\nSystem Date:{}\nOutput: {}\n".format(dob,today,expected))
        assert expected == test_inputs[k]
