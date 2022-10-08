from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField(null = True)
    age = models.IntegerField(null = True)
    upload_image = models.ImageField(upload_to = "image/", null = True)
    
    def __str__(self):
        return  "{}".format(self.lastname)

class mark(models.Model):
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE, null = True)
    subject = models.CharField(max_length=100, null = True)
    mark = models.IntegerField()
    updated_on = models.DateTimeField (null = True, auto_now = True)
    created_on = models.DateTimeField (null = True, auto_now_add = True)
    modified_by = models.CharField(max_length=100, null = True)
    created_by = models.CharField(max_length=100, null = True)
    
    



