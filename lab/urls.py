from django.urls import path
import lab.views as lv
app_name = 'lab'
urlpatterns = [
    # 首页
    path('', lv.lab, name='shuaxin'),
    # 内容页面
    path('content/', lv.content, name='content'),
    # 创客实验室
    path('CKlab/', lv.CKlab, name='CKlab'),
    # 师资力量
    path('teacher/', lv.teacher, name='teacher'),
    # 大数据
    path('BigData/', lv.BigData, name='BigData'),
    # 人工智能
    path('AI/', lv.AI, name='AI'),
    # 关于
    path('about/', lv.about, name='about'),
    # 联系我们
    path('contect/', lv.contect, name='contect'),


    # 活动相册
    path('album/', lv.album, name='album'),
    # 学生相册
    path('student/', lv.student, name='student'),

    # 通知公告
    path('notice/', lv.notice, name='notice'),
    path('noticeContent/<int:id>', lv.noticeContent, name='noticeContent'),
    # 讲座信息
    path('lecture/', lv.lecture, name='lecture'),
    path('lectureContent/<int:id>', lv.lectureContent, name='lectureContent'),
    # 娱乐活动
    path('fun/', lv.fun, name='fun'),
    path('funContent/<int:id>', lv.funContent, name='funContent'),
    # 历史竞赛
    path('competition/', lv.competition, name='competition'),
    path('competitionContent/<int:id>', lv.competitionContent, name='competitionContent'),
    # 项目课题
    path('project/', lv.project, name='project'),
    path('projectContent/<int:id>', lv.projectContent, name='projectContent'),
    # 学术成果
    path('essay/', lv.essay, name='essay'),
    path('essayContent/<int:id>', lv.essayContent, name='essayContent'),
    # 学术资料
    path('material/', lv.material, name='material'),
    path('materialContent/<int:id>', lv.materialContent, name='materialContent'),
]
