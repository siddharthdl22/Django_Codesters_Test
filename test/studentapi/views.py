from studentapi.models import Teacher
from studentapi.serializers import TeacherSerializer
from rest_framework_mongoengine import generics


class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
