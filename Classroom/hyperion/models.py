from django.db import models
from datetime import date,datetime

from django.urls import reverse


class user(models.Model):
    ID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    DoB = models.DateField()
    Email = models.EmailField()
    Registration_Date = models.DateField(default=date.today)

    #def __str__(self):
       # return self.ID

class classroom(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=128)
    Description = models.TextField()
    Creator_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Creation_Date = models.DateField(default= date.today)
    ClassCode = models.CharField(max_length=128)

    #def __str__(self):
        #return self.ID

class teacher(models.Model):
    ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Class_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)

class student(models.Model):
    ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Class_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)

class user_login(models.Model):

    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Password = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('login', args=[str(self.User_ID)])

class content(models.Model):
    ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Classroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)
    Attachment = models.FileField(upload_to='files/', null=True)
    TimeStamp = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.ID + ": " + str(self.Attachment)




class submission(models.Model):
    ID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Time_stamp = models.DateTimeField(default=datetime.today)
    Last_modified = models.DateTimeField(default=datetime.today)
    Content_ID = models.ForeignKey(content, on_delete=models.CASCADE)
    CLassroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)

class analytic(models.Model):
    ID = models.AutoField(primary_key=True)
    CLassroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)
    Teacher_ID = models.ForeignKey(teacher, on_delete=models.CASCADE)
    Generation_Time = models.DateTimeField(default=datetime.today)
    Report = models.FileField()

class Post(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.TextField()
    Classroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField(default=datetime.today)
    Description = models.TextField()
    Content_ID = models.ForeignKey(content, on_delete=models.CASCADE)
    LastModified = models.DateTimeField()

class Task(models.Model):
    TaskID = models.AutoField(primary_key=True)
    Title = models.TextField()
    Description = models.TextField()
    Teacher_ID = models.ForeignKey(teacher, on_delete=models.CASCADE)
    Classroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)
    Content_ID = models.ForeignKey(content, on_delete=models.CASCADE)
    Creation_Date = models.DateTimeField()
    LastModified = models.DateTimeField()

class comment(models.Model):
    ID = models.AutoField(primary_key=True)
    Classroom_ID = models.ForeignKey(classroom, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
    TimeStamp = models.DateTimeField()
    LastModified = models.DateTimeField()
    Content = models.TextField()