from django.test import TestCase
from todo.models import Task, Tag

class TaskTagTestCase(TestCase):
    def setUp(self):
        tag = Tag.objects.create(name="Test Tag")
        task = Task.objects.create(content="Test Task")
        task.tags.add(tag)

    def test_task_has_tag(self):
        task = Task.objects.first()
        self.assertEqual(task.tags.first().name, "Test Tag")

