from datetime import datetime  #this module is used to handle date time expressions
from playsound import playsound  #this module is used to play sound files 
import re  #this module provides a way to deal with regular expressions
import time #this module provides a way to work with time related functions

def validate_time(input_time):
    pattern = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
    return pattern.match(input_time)

def set_alarm():
    while True:
        alarm_time = input("enter the time in hours minutes and time format(HH:MM:SS) separated by the colons: ")
        if validate_time(alarm_time):
            return alarm_time
        else:
            print("Enter the time again as the last input wa invlaid time.")
            
            
def main():
    alarm_time = set_alarm()
    print(f"The alarm time is set for : {alarm_time}")
    
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now==alarm_time:
            playsound("alarm.mp3")
            print("Wake up")
            break
        time.sleep(1)
        
        
if __name__=="__main__":
    main()