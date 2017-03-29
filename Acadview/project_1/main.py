print " welcome to my project 1"
print " CONTENTS"
print " 1:- BATTLESHIP"
print " 2:- EXAM STATISTICS"
print " 3:- STUDENT BECOME TEACHER"
print " 4:- ENTER YOUR CHOICE (1/2/3)"
# to get the input from user
choice = raw_input()
 # code which will execute the files acording to the user's choice
 if choice==1:
     import battleship.py
 elif choice==2:
     import examstatistics.py
 elif choice==3:
     import student_to_teacher.py
 else:
     print "Oops..! you entered wrong choice"