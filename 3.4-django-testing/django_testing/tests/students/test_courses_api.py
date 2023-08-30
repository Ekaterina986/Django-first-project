import pytest
from rest_framework.test import APIClient
from students.models import Course, Student
from model_bakery import baker


# def test_example():
    # assert False, "Just test example"

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return student

@pytest.fixture
def course_factory():
    def course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return course



@pytest.mark.django_db
def test_retrieve(client, course_factory):
    course = course_factory()
    response = client.get(f'api/v1/courses/{course.id}')
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == courses[0].name

def test_list(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.get('api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.object.filter(id = courses.id)
    data = response.json()

    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id

def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.object.filter(name = courses.name)
    data = response.json()

    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


def test_create(client, course_factory):
    courses = course_factory()
    count = Course.objects.count()
    response = client.post('api/v1/courses/', data={'name'="test_course", 'student' = student.id}, format = 'json')
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


def test_update(client, course_factory):
    courses = course_factory()
    response = client.patch(f'api/v1/courses/{course.id}', data={'name' = "test_course1", }, format = 'json')
    assert response.status_code == 200
    assert data[0].['name'] == 'test_course1'


def delete(client, course_factory):
    courses = course_factory()
    count = Course.objects.count()
    response = client.delete(f'api/v1/courses/{course.id}', data={'id' = course.id, }, format = 'json')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1

