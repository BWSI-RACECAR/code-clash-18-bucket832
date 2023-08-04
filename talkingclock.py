"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""




    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            hour = {
                 '0':"twelve",
                 '1':"one",
                 '2':"two",
                 '3':"three",
                 '4':"four",
                 '5':"five",
                 '6':"six",
                 '7':"seven",
                 '8':"eight",
                 '9':"nine",
                 '10':"ten",
                 '11':"eleven",
                 '12':"twelve",
                 '13':"one",
                 '14':"two",
                 '15':"three",
                 '16':"four",
                 '17':"five",
                 '18':"six",
                 '19':"seven",
                 '20':"eight",
                 '21':"nine",
                 '22':"ten",
                 '23':"eleven",
            }
            tens = {
                '2': "twenty",
                '3': "thirty",
                '4': "thirty",
                '5': "thirty",
            }  
            teens = {
                '10': "ten",
                '11': "eleven",
                '12': "twelve",
                '13': "thirteen",
                '14': "fourteen",
                '15': "fifteen",
                '16': "sixteen",
                '17': "seventeen",
                '18': "eighteen",
                '19': "nineteen",
            }
            ones = {
                '1': "one",
                '2': "one",
                '3': "one",
                '4': "one",
                '5': "one",
                '6': "one",
                '7': "one",
                '8': "one",
                '9': "one",
            }
            #TODO: Write code below to return a string with the solution to the prompt.
            hours, minutes = input_time.split(':')
            ind = 'pm' if hour >= 12 else 'am'
            str_hour = hour[hours] + ' '
            ten, one = minutes[0], minutes[1]
            if ten == '1':
                 return f"It's {str_hour}{teens[minutes]} {ind}"     
            str_ten = tens[ten]  + ' '  
            str_one = ones[one] + ' '
            return f"It's {str_hour}{str_ten}{str_one}{ind}"

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        