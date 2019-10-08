from django.urls import path
from download import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('caseManner/', views.caseManner, name='caseManner'),
    path('check/', views.check, name='check'),
    path('startTestCase/', views.startTestCase, name='startTestCase'),
    path('deleteCase/', views.deleteCase, name='deleteCase'),
    path('initDate/', views.initDate, name='initDate'),
    path('tools/', views.tools, name='tools'),
    path('luckydraw/', views.luckydraw, name='luckydraw'),
    path('stepTestCase/', views.stepTestCase, name='stepTestCase'),
    path('projectName/', views.projectName, name='projectName'),
    path('case/<str:project>', views.case, name='case'),
    path('details/<str:project>', views.details, name='details'),
    path('report/<str:project>', views.report, name='report'),
    path('threadtest/', views.threadtest, name='threadtest'),
    path('threadGetResult/', views.threadGetResult, name='threadGetResult'),
]
