from django.conf.urls import url
from studentwebsite import views
from studentwebsite import templates
from django.conf import settings
from django.conf.urls.static import static

app_name = 'studentwebsite'
urlpatterns = [
    url(r'^getteacherview/$', views.get_teacher_view, name = "get_teacher_view"),
    url(r'^$', views.show_teacher_page, name = "show_teacher_page"),
]
