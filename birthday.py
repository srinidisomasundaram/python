from datetime import *
from dateutil import relativedelta
import calendar


class Birthday:


    '''A function that counts the number of days
    and weeks'''
    
    def days_count(self,bday,date2):
        self.diff1 = abs( bday - date2)
        self.diff = self.diff1.days
     #   print("Days to birthday- {}\n".format(self.diff))
        self.weeks = abs(self.diff)//7
        return self.diff,self.weeks

    '''A function to notify upcoming
    birthdays within the range of 2 months'''

    def upcoming_birthday(self,days,weeks,dob,today): 
        if days==1:
            return "Tomorrow"
        elif days==2:
            return "Day after Tomorrow"
        elif days in range(3,7):         
            return "Coming {}".format(dob.strftime("%A"))
        elif days in range(7,14):         
            return "Next {}".format(dob.strftime("%A"))
        elif days==14:
            return "{} weeks from now".format(self.weeks)
        elif days in range(14,21):       
            return "{} days from now".format(days)
        elif days==21:
            return "{} weeks from now".format(self.weeks)
        elif days in range(21,28):    
            return "After {} weeks".format(self.weeks)
        elif days==28 or days==30 :
            return "{} days from now".format(days)
        elif ( days==29 or days==31 and abs(dob.month - today.month)==1 )or (days>31 and abs(dob.month-today.month)==1):
            return "Next month"
        elif abs(dob.month - today.month)>1 and days>31:
            return "{} months from now".format(abs(dob.month - today.month))

    '''A function to notify
    passed birthdays'''
    
    def passed_birthday(self,days,weeks,dob,today): 
        if days == 1:
            return "Yesterday"
        elif days == 2:
            return "Day before yesterday"
        elif days in range(3,7):
            return "{} days back".format(days)
        elif days == 7:
            return "Last {}".format(dob.strftime("%A"))
        elif days in range(8,14):
            return "in the last week"
        elif days in range(14,28):
            return "{} weeks ago".format(self.weeks)
        elif days >= 28 and days <= calendar.monthrange(today.year,today.month)[1]:
            return "Almost a month ago"
        elif today.day >= dob.day and abs(dob.month-today.month) == 1:
            return "Last Month"
        elif abs(dob.month - today.month)>1:
            return "{} months ago".format(abs(dob.month - today.month))


    '''A function to check if birthdays are coming up/passed and
    display reminders accordingly'''

    def birthday_check(self,dob, today):
        dob = dob.replace(year=today.year)
        month_count = abs(dob.month - today.month)
        result = 'none'
        
##    case-1: 
##    checks if system date falls below the
##    date of birth, within a range of 2 months. If yes,it
##    displays a reminder accordingly

        
        if (today < dob) and (month_count <= 2):
          
            days_to_birthday, weeks_to_birthday = self.days_count(dob, today )
            result= self.upcoming_birthday(days_to_birthday, weeks_to_birthday,dob, today )
            return result
       
            
##    case-2 :  checks if system date has
##    passed the birthdate this year.If yes, it further checks the difference
##    between the system date and the birthday that falls next year. Incase the
##    next birthdate falls within a span of 2 months,reminder is set for upcoming birthday.
##    Else, reminder is displayed for passed birthday
        elif today > dob and (today.month==dob.month):
            
            days_to_birthday, weeks_to_birthday = self.days_count(dob, today)
            result = self.passed_birthday(days_to_birthday, weeks_to_birthday , dob, today)
            return result

        elif today > dob :
            dob_2 = dob.replace(year=today.year + 1)
            m_diff = relativedelta.relativedelta(dob_2,today).months
            days_to_birthday, weeks_to_birthday = self.days_count(dob,today)
            dob = dob_2
    
     
            if m_diff > 2 :

                result= self.passed_birthday(days_to_birthday, weeks_to_birthday,dob,today)
                return result
                print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob.strftime("%B")))

            elif m_diff in (1,2):

                result= self.upcoming_birthday(days_to_birthday, weeks_to_birthday,dob,today )
                return result
                print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob_2.strftime("%B")))


##    case-3: system date matches
##    with the birthdate

        else:
            result = "Today"
            return result
            print("on {0},{1}th of {2}".format(dob.strftime("%A"),dob.strftime("%d"),dob.strftime("%B")))
   



if __name__=="__main__":
    a = Birthday()
    birth_year = input('Enter your date of birth in YYYY-MM-DD format')
    year, month, day = map(int, birth_year.split('-'))
    dob = date(year, month, day)
    today_date = datetime.today()
    y,m,d = datetime.today().year, datetime.today().month, datetime.today().day
    today = date(y, m, d)
    a.birthday_check(dob, today)
    


            
    
