from django.shortcuts import render


# 主页
def lab(request):
    return render(request, 'index.html')


# 内嵌的html页面
def content(request):
    return render(request, 'html/content.html')


# 创客实验室
def CKlab(request):
    return render(request, 'html/CKlab.html')


# 师资力量
def teacher(request):
    return render(request, 'html/teacher.html')


# 大数据
def BigData(request):
    return render(request, 'html/BigData.html')


# 人工智能
def AI(request):
    return render(request, 'html/AI.html')


# 关于
def about(request):
    return render(request, 'html/about.html')


# 联系我们
def contect(request):
    return render(request, 'html/contect.html')

# 下面都是数据库
from . import models


# 活动相册
def album(request):
    img = models.Album.objects.all()
    return render(request, 'html/album.html', {'img': img})


# 学生相册
def student(request):
    img = models.Student.objects.all()
    return render(request, 'html/student.html', {'img': img})


# 通知公告（标题列表）
def notice(request):
    articals = models.Notice.objects.all().order_by('-time')
    return render(request, 'html/notice.html', {'articals': articals})


# 通知公告内容（内容）
def noticeContent(request, id):
    articles = models.Notice.objects.get(pk=id)
    return render(request, 'html/noticeContent.html', {'articles': articles})


# 讲座信息（标题列表）
def lecture(request):
    articals = models.Lecture.objects.all().order_by('-time')
    return render(request, 'html/lecture.html', {'articals': articals})


# 讲座信息内容（内容）
def lectureContent(request, id):
    articles = models.Lecture.objects.get(pk=id)
    return render(request, 'html/lectureContent.html', {'articles': articles})


# 娱乐活动（标题列表）
def fun(request):
    articals = models.Fun.objects.all().order_by('-time')
    return render(request, 'html/fun.html', {'articals': articals})


# 娱乐活动内容（内容）
def funContent(request, id):
    articles = models.Fun.objects.get(pk=id)
    return render(request, 'html/funContent.html', {'articles': articles})


# 历史竞赛（标题列表）
def competition(request):
    articals = models.Competition.objects.all().order_by('-time')
    return render(request, 'html/competition.html', {'articals': articals})


# 历史竞赛内容（内容）
def competitionContent(request, id):
    articles = models.Competition.objects.get(pk=id)
    return render(request, 'html/competitionContent.html', {'articles': articles})


# 项目课题（标题列表）
def project(request):
    articals = models.Project.objects.all().order_by('-time')
    return render(request, 'html/project.html', {'articals': articals})


# 项目课题内容（内容）
def projectContent(request, id):
    articles = models.Project.objects.get(pk=id)
    return render(request, 'html/projectContent.html', {'articles': articles})


# 学术成果（标题列表）
def essay(request):
    articals = models.Essay.objects.all().order_by('-time')
    return render(request, 'html/essay.html', {'articals': articals})


# 学术成果（内容）
def essayContent(request, id):
    articles = models.Essay.objects.get(pk=id)
    return render(request, 'html/essayContent.html', {'articles': articles})


# 学术资料（标题列表）
def material(request):
    articals = models.Material.objects.all().order_by('-time')
    return render(request, 'html/material.html', {'articals': articals})


# 学术资料（内容）
def materialContent(request, id):
    articles = models.Material.objects.get(pk=id)
    return render(request, 'html/materialContent.html', {'articles': articles})