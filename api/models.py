from django.db import models

# Create your models here.


class Pupil(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    age=models.IntegerField()
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.first_name+" "+ self.last_name
    
class Contact(models.Model):
    pupil=models.OneToOneField(Pupil,on_delete=models.CASCADE)
    phone=models.CharField(max_length=64)
    email=models.CharField(max_length=30,unique=True)
    address=models.CharField(max_length=30,default="")


    def __str__(self) -> str:
        return self.email
    
class Course(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Group(models.Model):
    name=models.CharField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    students=models.ManyToManyField(to=Pupil)

    def __str__(self) -> str:
        return self.name