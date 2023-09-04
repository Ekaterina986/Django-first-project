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


# cd ~/python_большой_курс/Django/dj-homeworks/3.4-django-testing/django_testing
# pytest -s
@pytest.mark.django_db
def test_retrieve(client, course_factory):
    course = course_factory()
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    response_courses = response.json()
    assert len(response_courses) == 1
    assert response_courses[0]['id'] == course.id
    assert response_courses[0]['name'] == course.name


@pytest.mark.django_db
def test_list(client, course_factory):
    courses = course_factory(_quantity=100)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    response_courses = response.json()
    assert len(response_courses) == len(courses)
    for key, response_course in enumerate(response_courses):
        # Порядок элементов может не совпадать
        # assert c['name'] == courses[key].name
        find_course = [course_item for course_item in courses if course_item.id == response_course['id']]
        assert len(find_course) == 1
        assert find_course[0].name == response_course['name']


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=100)
    for key, course in enumerate(courses):
        response = client.get('/api/v1/courses/', {"id": course.id})
        assert response.status_code == 200
        response_courses = response.json()
        assert len(response_courses) == 1
        assert response_courses[0]['id'] == course.id
        assert response_courses[0]['name'] == course.name


@pytest.mark.django_db
def test_filter_name(client, course_factory):
     courses = course_factory(_quantity=100)
     for key, course in enumerate(courses):
         response = client.get('/api/v1/courses/', {"name": course.name})
         assert response.status_code == 200
         response_courses = response.json()
         # Может быть несколько записей с одинаковым названием
         assert len(response_courses) >= 1
         for key, response_course in enumerate(response_courses):
            assert response_course['name'] == course.name


@pytest.mark.django_db
def test_create(client):
    name = "test_course"
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', {'name':name},'json')
    assert response.status_code == 201
    response_courses = response.json()
    assert Course.objects.count() == count + 1
    course_db = Course.objects.get(id = response_courses['id'])
    assert course_db.id == response_courses['id']
    assert course_db.name == name


@pytest.mark.django_db
def test_update(client, course_factory):
    name = "test_course_update"
    courses = course_factory(_quantity=100)
    id = courses[0].id
    response = client.patch('/api/v1/courses/', {'name':name, 'id':id},'json')
    assert response.status_code == 204
    course_db = Course.objects.get(id = id)
    assert course_db.name == name


@pytest.mark.django_db
def test_delete(client, course_factory):
    courses = course_factory(_quantity=100)
    count = Course.objects.count()
    id = courses[0].id
    response = client.delete('/api/v1/courses/', {'id': id}, 'json')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    course_db = Course.objects.filter(id=id).first()
    assert course_db is None

