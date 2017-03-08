from rest_framework_mongoengine.serializers import DocumentSerializer
from studentapi.models import Teacher


class TeacherSerializer(DocumentSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
