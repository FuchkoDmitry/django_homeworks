from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from students.models import Course, Student
from django_testing import settings


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'name', 'birth_date')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        if self.context['request'].method in ("POST", "PATCH"):
            if len(data.get('students', [])) > settings.MAX_STUDENTS_PER_COURSE:
                raise ValidationError(
                    f'на курсе не может быть '
                    f'больше {settings.MAX_STUDENTS_PER_COURSE} студентов'
                )
        return data

    def create(self, validated_data):
        students = validated_data.pop('students', None)
        course = super().create(validated_data)
        if students:
            course.students.set(students)

        return course

    def update(self, instance, validated_data):
        students = validated_data.pop('students', [])
        instance = super().update(instance, validated_data)
        instance.students.set(students)
        return instance
