import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_course(client, course_factory):

    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.pk})

    response = client.get(url)
    response_json = response.json()

    assert response.status_code == HTTP_200_OK

    assert response_json['id'] == course.pk
    assert response_json['name'] == course.name


@pytest.mark.django_db
def test_get_courses(client, course_factory):

    courses = course_factory(_quantity=10)
    url = reverse('courses-list')

    response = client.get(url)

    assert response.status_code == HTTP_200_OK

    courses_list = response.json()
    assert len(courses_list) == 10
    for index, course in enumerate(courses_list):
        assert course['name'] == courses[index].name


@pytest.mark.django_db
def test_id_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    id_to_check = courses[4].id
    url = reverse('courses-list')

    response = client.get(url, data={'id': id_to_check})

    assert response.status_code == HTTP_200_OK

    result = response.json()
    assert len(result) == 1
    assert result[0]['id'] == id_to_check


@pytest.mark.django_db
def test_name_filter(client, course_factory):
    courses = course_factory(_quantity=10)
    name_to_check = courses[6].name

    url = reverse('courses-list')

    response = client.get(url, data={'name': name_to_check})

    assert response.status_code == HTTP_200_OK

    result = response.json()
    assert len(result) == 1
    assert result[0]['name'] == name_to_check


@pytest.mark.django_db
def test_create_course(client):
    course_to_create = {'name': 'course_name'}
    url = reverse('courses-list')

    response = client.post(url, data=course_to_create)

    assert response.status_code == HTTP_201_CREATED

    assert response.json()['name'] == course_to_create['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course_to_update = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course_to_update.id})
    data_to_update = {'name': 'new_course_name'}

    response = client.patch(url, data=data_to_update)
    response_json = response.json()

    assert response.status_code == HTTP_200_OK

    assert response_json['name'] == data_to_update['name']
    assert response_json['id'] == course_to_update.id


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_to_delete = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course_to_delete.pk})

    response = client.delete(url)

    assert response.status_code == HTTP_204_NO_CONTENT


@pytest.mark.parametrize(
    'students_count,expected_status',
    [(2, HTTP_201_CREATED),
     (3, HTTP_400_BAD_REQUEST)
     ]
)
@pytest.mark.django_db
def test_course_students(
        client, course_factory, student_factory, settings, students_count, expected_status):
    settings.MAX_STUDENTS_PER_COURSE = 1

    students = student_factory(_quantity=students_count)

    course = course_factory(students=students)

    data = {"name": course.name, "students": [s.id for s in students]}

    url = reverse('courses-list')

    response = client.post(url, data=data)

    print(response)
    print(response.json())
    print(response.data)

    assert response.status_code == expected_status



