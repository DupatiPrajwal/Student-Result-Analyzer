run = 1
while run == 1 :
    Stu_name = input("enter name of the student :")
    Stu_roll = int(input("enter roll number of the student :"))
#------------------------------------------------------------------------#
    Sub_1 = int(input("enter marks of English/100 :"))
    Sub_2 = int(input("enter marks of Maths/100 :"))
    Sub_3 = int(input("enter marks of Physics/100 :"))
    Sub_4 = int(input("enter marks of Chemistry/100 :"))
    Sub_5 = int(input("enter marks of Computer Science/100 :"))
#------------------------------------------------------------------------#
    if Sub_1 < 35 or Sub_2 < 35 or Sub_3 <35 or Sub_4 < 35 or Sub_5 < 35 :
        Sub_result = "Fail"
    else :
        Sub_result = "Pass"   
#------------------------------------------------------------------------#
    Stu_total = Sub_1+ Sub_2 + Sub_3 + Sub_4 + Sub_5
    Stu_percentage = (Stu_total)/500*100
    print("Stu_total :",Stu_total)
    print("Stu_percentage :",Stu_percentage)
#------------------------------------------------------------------------#
    if Sub_result == "Fail" :
        print("Result = Fail")
        print("Grade = F")
    else :
        if Stu_percentage >= 75 :
            print("Distinction")
        elif Stu_percentage >= 60 :
            print("First Class")
        elif Stu_percentage >= 40 :
            print("pass")
        else :
            print("Fail")
#------------------------------------------------------------------------#
        if Stu_percentage >= 90 :
            print("Grade : +A")
        elif Stu_percentage >= 75 :
            print("Grade : A")
        elif Stu_percentage >= 60 :
            print("Grade : B")
        elif Stu_percentage >= 40 :
            print("Grade : C")
        else :
             print("Grade : F")
#------------------------------------------------------------------------#
    run = int(input("enter 1 to add another student, 0 to exit :"))



