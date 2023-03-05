import easygui
import math

nameOfSchool = easygui.enterbox("Enter the name of your school", "School Name")
maxClassSize = easygui.integerbox("What is the maximum number of students you want in each class, Must be a Number "
                                  "between 10 and 30")

totalNumChildren = easygui.integerbox(f"What is the total number of children currently at {nameOfSchool}"
                                      f", this must be between 10 and 1400", upperbound=1400, lowerbound=10)


numClasses = math.ceil(totalNumChildren / maxClassSize)
print(numClasses)
