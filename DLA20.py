#DLA-20 Calculator
#Because Avatar is a piece of shit

from math import *
from time import sleep

print """
   __   _   __       __  __ 
  /  )//  /  )        )/  )
 /  / /   /--/ --- .--'/  / 
/__/_/___/  (_    (__ (__/  
                            
Daily Living Activities - 20
Level of Care Measurement Tool
v.2
by Jordan Howard                          

Press any key to continue...
"""

sleep(1)
print """Instructions: 
For each domain, input 1 through 7 according to the DLA-20 guide. If not enough information is available, please input 'none'. For help
on individual sections, press 'H' """

VALID_VALUES = [1, 2, 3, 4, 5, 6, 7, "none"] 

domains = ['1 Health Practices', '2. Housing Stability, Maintenance', '3. Communication', 'Safety', 
'4. Managing Time', '5. Managing Money', '6. Nutrition', '7. Problem Solving', '8. Family Relationship',
'10. Alcohol, Drug Use', '11. Leisure', '12. Community Resources', '13. Social Network', '14. Sexuality', 
'15. Productivity', '16. Coping Skills', '17. Behavioral Norms', '18. Personal Hygiene', '19. Grooming', '20. Dress']


def get_input(N):
  userInputValid = False
  while userInputValid == False:
    print domains[N]
    #score=sum([1.0*int(raw_input('Please input score for domain %s: ' % d)) for d in domains]) / len(domains)
    score=raw_input('Please input score: ')
    try:
      if score in VALID_VALUES or int(score) in VALID_VALUES:
        userInputValid = True 
        return score
      else:
        userInputValid = False
        print("Invalid Input!")
    except TypeError: 
      userInputValid = False
      print ("Invalid Input!")
    except ValueError:
      userInputValid = False
      print("Invalid Input")
      
def LoC_converter(score):
    if score >= 6.1:
        return "Level of Care #1"
    elif (score >= 5.1) and (score <= 6):
        return "Level of Care #2"
    elif (score >= 4.1) and (score <= 5):
        return "Level of Care #3"
    elif (score >= 3.1) and (score <= 4):
        return "Level of Care #4"
    else: 
        return "Level of Care #5"
      

doms =[get_input(N) for N in range(0, 20)]

ValidDoms = []

for i in doms:
  if i != "none":
    ValidDoms.append(int(i))
    
if len(ValidDoms) < 15:
  print "Not Enough Inputs. Please re-evaluate. DLA-20 requires **AT A MINIMUM** 15 domains"
  exit

DLAsum = 0
average = 0  
  
for i in ValidDoms:
  DLAsum = DLAsum + i
  
average = float(DLAsum) / len(ValidDoms)

print "Sum:"
print DLAsum

print "DLA Average"
print average

print LoC_converter(average)


"""
# This should print an "A"      
print grade_converter(92)

# This should print a "B"
print grade_converter(83)

# This should print an "F"
print grade_converter(61)
"""
