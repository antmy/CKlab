from django.db import models


# 相册表
class Album(models.Model):
    picture = models.ImageField(upload_to='album')
    information = models.TextField(max_length=100)

    def __str__(self):
        return self.information


# 学生表
class Student(models.Model):
    picture = models.ImageField(upload_to='student')
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name


# 通知公告表
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content1 = models.TextField(max_length=2000, blank=True, null=True)
    content2 = models.TextField(max_length=2000, blank=True, null=True)
    content3 = models.TextField(max_length=2000, blank=True, null=True)
    file = models.FileField(upload_to='file', blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return self.title


# 讲座信息表
class Lecture(models.Model):
    title = models.CharField(max_length=200)
    people = models.CharField(max_length=100, blank=True, null=True)
    danwei = models.CharField(max_length=100, blank=True, null=True)
    lectureTime = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=2000)
    peopleIntroduce = models.TextField(max_length=2000, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return self.title


# 娱乐活动表
class Fun(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    time = models.DateField()

    def __str__(self):
        return self.title


# 历史竞赛表
class Competition(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    file = models.FileField(upload_to='file', blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return self.title


# 项目课题表
class Project(models.Model):
    title = models.CharField(max_length=100)
    content1 = models.TextField(max_length=2000, blank=True, null=True)
    content2 = models.TextField(max_length=2000, blank=True, null=True)
    content3 = models.TextField(max_length=2000, blank=True, null=True)
    file = models.FileField(upload_to='file', blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return self.title


# 学术成果表
class Essay(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    time = models.DateField()

    def __str__(self):
        return self.title


# 学术资料表
class Material(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    time = models.DateField()

    def __str__(self):
        return self.title