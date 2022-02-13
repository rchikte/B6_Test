from django.db import models
from django.forms import ValidationError

# Create your models here.



class table1(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "table1"


class Student(models.Model):
    name = models.CharField(max_length = 100)
    marks = models.FloatField()
    subject_nm = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100,null=True)
    age = models.IntegerField()
    is_active =models.BooleanField(default=True)
    department = models.ForeignKey("Department",on_delete=models.SET_NULL,null=True)
    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.name}"


class Common_field(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class College(Common_field):
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = "College"


class Principal(Common_field):
    college = models.OneToOneField(College,on_delete=models.CASCADE,null=True)


    class Meta: 
        db_table = "Principle"

class Department(Common_field):
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    intake = models.IntegerField()

    class Meta:
        db_table = "Department"

class Subject(Common_field):
    is_practical = models.BooleanField(default=False)
    total_marks = models.IntegerField()
    student = models.ManyToManyField(Student)

    class Meta:
        db_table = "Subject"


class Employee(Common_field):
    emp_id = models.CharField(primary_key=True,max_length=6)
    salary = models.IntegerField()

    class Meta:
        db_table = "Employee"


    def save(self,*args,**kwargs):
        if not self.emp_id:
            raise ValidationError("Emp id should be pass at time of object creation")
        super(Employee,self).save(*args,**kwargs)
