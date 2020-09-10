# Author: Sergio Ulloa siu5033@psu.edu
# Collaborator: Arabella Harrison axh5810@psu.edu
# Collaborator: Vishal Vardhan vvm5237@psu.edu
# Collaborator: Tigran Saakyan tms6749@psu.edu
# Section: 12
# Breakout: 10

def getLetterGrade(grade):
  if(grade >= 93.0):
    return "A"
  elif (grade >= 90.0):
    return "A-"
  elif (grade >= 87.0):
    return "B+"
  elif (grade	>=83.0):
    return "B"
  elif (grade >= 80.0):
    return "B-"
  elif (grade >= 77.0):
    return "C+"
  elif (grade >= 70.0):
   return "C"
  elif (grade >= 60.0):
    return "D"
  else:
    return "F"
 

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  print (f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__ == "__main__":
  run() 