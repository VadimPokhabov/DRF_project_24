from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """
    Тестирование создания, изменения и получения урока
    """

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(course_name="test1", description="test1", owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name="test2", description="test2_2", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            "lesson_name": "Java",
            "description": "good lesson",
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "lesson_name": "Java + ",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name', ), "Java + ", )

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name', 'description'), "test2", "test2_2")

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {'id': self.lesson.id,
                       'lesson_name': self.lesson.lesson_name,
                       'description': self.lesson.description,
                       'image': None,
                       'url': self.lesson.url,
                       'course': self.lesson.course,
                       'owner': self.lesson.owner.id}
                  ]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

