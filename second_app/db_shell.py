from os import name
from second_app.models import *
from django.contrib.auth.models import User

e = Employee(emp_id="RC0001",salary=68000)
e.save()
s_name =Student.objects.all().order_by("name")
# print(s_name)
s_name_reverse = Student.objects.all().order_by("-name")
# print(s_name_reverse.query)


try:
    c1 = College.objects.get(name="D Y Patil")
    # print(c1)
except College.DoesNotExist:
    print("College Doesnot exist")
else:
    print(c1)    
# Principal
# print(c1.principal)      # one to one relationship------single object
# print(dir(c1))

# print(c1.department_set.all())  # one to many relationship     group object    

# d1 = Department.objects.get(name="Machnical")
# print(d1.student_set.all())

# s1 = Student.objects.get(name="aaa")      #many to many relationship 
# print(s1)
# print(dir(s1))
# print(s1.subject_set.all())   

dept = c1.department_set.all().filter(name="Machnical")[0]
studs = dept.student_set.all()
print(studs)
# dept = c1.department_set.all()[1]
# print(dept)

def stud_from_depart():
    student_list = []
    depts = c1.department_set.all()
    for dept in depts:
        studs = dept.student_set.all()
        student_list.extend(studs) 
    print(student_list)    

# stud_from_depart()

all_data = Student.objects.all().values("id")
# print(all_data)


# for stud in all_data:
    # print(stud,type(stud))

def sub_from_dept():
    student_list = []
    depts = c1.department_set.all()
    for dept in depts:
        studs = dept.student_set.all()
        student_list.extend(studs)

    subject_list = set()    
    for stud in student_list:
        sub =stud.subject_set.all()
        subject_list.update(sub)
    print(subject_list)


# sub_from_dept()

all_user = User.objects.all()
# print(all_user)

# s1 = Subject.objects.filter(student__department__name="CSE")
# print(s1)


# c1 = College.objects.create(name="Sinhgad clg",address="Lonavala")
# print(c1.id)
# p1 = Principal.objects.create(name="virus",college_id=7)
# print(p1)

# c1 = College.objects.get(name="Sinhgad clg")
# print(c1)

# d1 = Department.objects.create(name="IT",intake=100,college=c1)
# print(d1.__dict__)

# Subject.objects.create(name="Python",is_practical=True,total_marks=120)

s = Student.objects.get(name="aaa")
sub1 = Subject.objects.get(name="Python")
print(sub1)
sub1.student.add(s)




# exec(open(r'G:\class\a\Django_demo\first_project\second_app\db_shell.py').read())