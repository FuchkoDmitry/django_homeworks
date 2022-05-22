import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django_testing import settings
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def max_students_settings():
    default_value = settings.MAX_STUDENTS_PER_COURSE
    settings.MAX_STUDENTS_PER_COURSE = 1
    yield
    settings.MAX_STUDENTS_PER_COURSE = default_value


# эти варианты также не срабатывают
# @pytest.fixture(scope='session')
# def students_settings():
#     from django.conf import settings
#     settings.MAX_STUDENTS_PER_COURSE = 1


# @pytest.fixture
# def max_students_settings(settings):
#     settings.MAX_STUDENTS_PER_COURSE = 1
