#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_msagala.py
Author: Michael Sagala
The python code in this file (a1_msagala.py) is original work written by
Michael Sagala. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import sys

def leap_year(obj):
    '''
    Check if a given year is a leap year or not
    '''
    status = True
    num = int(obj)
    if (num % 4) == 0:
        if (num % 100) == 0:
            if (num % 400) == 0: #Checks if a given year is a leap year
                status = True
            else:
                status = False
        else:
            status = True
    else:
        status = False        
    return status

def sanitize(obj1,obj2):
    '''
    removes any characters in obj1 that is not stated in obj2
    '''
    list1 = list(obj1)
    list2 = list(obj2)
    list3=[] #new list that will contain sanitized list
    for x in list1:
        if x in list2:
            list3.append(x) #if a character in list1 matches a character in list2, append it to new list3
        
    results = ''.join(list3)#convert list to string
    return results #return string that contains sanitized list

def size_check(obj, intobj):
    '''
    check if given string matches the size stated by intobj..
    '''
    l1 = len(obj)#length of obj string
    if (l1 == intobj):
        status = True #returns True if length of string is equal to stated number
    else:
        status = False

    return status


def range_check(obj1, obj2):
    '''
    checks if number specified in obj1 is between numbers in obj2
    '''
    num = int(obj1)#number to be checked
    low = obj2[0]#minimum threshold for range
    high = obj2[1]#maximum threshold for range
    
    if (num >= low) and (num <= high):
        status = True
    else:
        status = False
    
    return status
    
def usage():    
    '''
    Contains a usage message for too many or too few arguments ...
    '''
    string = ("Usage: a1_msagala.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD")
    return string

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage()) #print usage message if there are not 2 arguments 
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars) #remove non-numerical characters
   # setp 4
   result = size_check(dob,8)#check if string length is 8 characters
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))#Check if year is within range
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))#Check if month number is within 12
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)#check if year is a leap year
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)#Convert numerical date to string with name of month
   # step 8
   print(new_dob)  