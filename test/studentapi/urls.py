from django.conf.urls import url
from studentapi import views

app_name = 'studentapi'
urlpatterns = [
    url(r'^$', views.TeacherView.as_view()),
]
