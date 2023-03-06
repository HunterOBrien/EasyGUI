import easygui
import math

nameOfSchool = easygui.enterbox("Enter the name of your school", "School Name")
teacherNum = easygui.integerbox("How many teachers are currently at your school?", "Teachers At School")
maxClassSize = easygui.integerbox("What is the maximum number of students you want in each class, Must be a Number "
                                  "between 10 and 30")

totalNumChildren = easygui.integerbox(f"What is the total number of children currently at {nameOfSchool}"
                                      f", this must be between 10 and 1400", upperbound=1400, lowerbound=10)


numClasses = math.ceil(totalNumChildren / maxClassSize)

if teacherNum >= numClasses:
    easygui.msgbox(f"At {nameOfSchool}You have enough teachers at your school, you only need {numClasses}")

else:
    easygui.msgbox(f"At {nameOfSchool} You do no have enough teachers at your school, you need {numClasses}")

