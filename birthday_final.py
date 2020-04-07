from datetime import *
from dateutil import relativedelta
import calendar


class Birthday:

    '''A function to get
    Date of Birth from user'''

    def get_birthdate(self):
        birth_year = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, birth_year.split('-'))
        self.dob = date(year, month, day)
        today_date = datetime.today()
        y,m,d = datetime.today().year, datetime.today().month, datetime.today().day
        self.today = date(y, m, d)
        return self.dob,self.today

    '''A function that counts the number of days
    and weeks'''
    
    def days_count(self,bday,date2):
        self.diff1 = abs( bday - date2)
        self.diff = self.diff1.days
        print("Day Count- ",self.diff)
        self.weeks = abs(self.diff)//7
        return self.diff,self.weeks

    '''A function to notify upcoming
    birthdays within the range of 2 months'''

    def upcoming_birthday(self,d,w,dob_2): 
        if d==1:
            print("Tomorrow")
        elif d==2:
            print("Day after Tomorrow")
        elif d in range(3,7):         
            print("Coming",dob_2.strftime("%A"))
        elif d in range(7,14):         
            print("Next",dob_2.strftime("%A"))
        elif d==14:
            print(self.weeks,"weeks from now")
        elif d in range(14,21):       
            print(d,"days from now")
        elif d==21:
            print(self.weeks,"weeks from now")
        elif d in range(21,29) and calendar.monthrange(today.year,today.month)[1]-1 != d:      
            print("After",self.weeks,"weeks")
        elif (abs(dob.month-today.month)==1 and calendar.monthrange(today.year,today.month)[1]-1== d)or d==30:
            print(d, "days from now")
        elif abs(dob.month-today.month)==1 and d >= calendar.monthrange(today.year,today.month)[1]:
            print("Next month")
        elif abs(dob.month - today.month)>1:
            print( abs(dob.month - today.month),"months from now")

    '''A function to notify
    passed birthdays'''
    
    def passed_birthday(self,d,w): 
        if d == 1:
            print("Yesterday")
        elif d == 2:
            print("Day before yesterday")
        elif d in range(3,7):
            print( d, "days back")
        elif d == 7:
            print("Last",dob.strftime("%A"))
        elif d in range(8,14):
            print("in the last week")
        elif d in range(14,28):
            print(self.weeks,"weeks ago")
        elif d >= 28 and d <= calendar.monthrange(today.year,today.month)[1]:
            print("Almost a month ago")
        elif today.day >= dob.day and abs(dob.month-today.month) == 1:
            print("Last Month")
        elif abs(dob.month - today.month)>1:
            print( abs(dob.month - today.month),"months ago")


    '''A function to check if birthdays are coming up/passed and
    display reminders accordingly'''

    def birthday_check(self,dob, today):
        dob = dob.replace(year=today.year)
        month_count = abs(dob.month - today.month)  
        
##    case-1: 
##    checks if system date falls below the
##    date of birth, within a range of 2 months. If yes,it
##    displays a reminder accordingly

        
        if (today < dob) and (month_count <= 2):
            days_to_birthday, weeks_to_birthday = self.days_count(dob, today )
            self.upcoming_birthday(days_to_birthday, weeks_to_birthday,dob )
       
            
##    case-2 :  checks if system date has
##    passed the birthdate this year.If yes, it further checks the difference
##    between the system date and the birthday that falls next year. Incase the
##    next birthdate falls within a span of 2 months,reminder is set for upcoming birthday.
##    Else, reminder is displayed for passed birthday


        elif today > dob :
            dob_2 = dob.replace(year=today.year + 1)
            m_diff = relativedelta.relativedelta(dob_2,today).months
            days_to_birthday, weeks_to_birthday = self.days_count(dob,today)
     
            if m_diff > 2 :

                self.passed_birthday(days_to_birthday, weeks_to_birthday)
                print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob.strftime("%B")))

            elif m_diff <=2 :

                self.upcoming_birthday(days_to_birthday, weeks_to_birthday, dob_2 )
                print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob_2.strftime("%B")))


##    case-3: system date matches
##    with the birthdate

        else:
            print("Today")
            print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob.strftime("%B")))
   



if __name__=="__main__":
    a = Birthday()
    dob, today = a.get_birthdate()
    a.birthday_check(dob, today)
    


            
    
