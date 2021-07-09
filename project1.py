#Project 1: Basic school administration test

import csv

def write_info_csv(info_list):
    with open("student_info.csv",'a+',newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Conctact_info","Email_id"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1

    while (condition):
        student_info=input("Enter the student information for student #{} in the following format(Name Age Contact_number Email_id):".format(student_num))

        #splitting the information
        student_info_list=student_info.split(' ')

        print("\n The entered information is \nName:{} \nAge:{} \nContact_number:{} \nEmail_id:{}"
               .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("Is the entered information is correct?(yes/no):")
        if choice_check=="yes":
            write_info_csv(student_info_list)

            condition_check=input("Enter (yes/no) if you want to enter the student info or not:")

            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            else:
                condition=False
        elif choice_check=="no":
            print("\nPlease re-enter the information")
