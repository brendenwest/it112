import unittest
from django.test import TestCase
from students.models import Student, graduating_eta


class TestStudents(TestCase):
    def setUp(self):
        # Do some initialization work
        self.id = 2

    def test_graduating_now(self):
        assert graduating_eta(2023) == 0

    def test_graduated(self):
        assert graduating_eta(2022) < 0

    def test_graduating_later(self):
        assert graduating_eta(2024) > 0


    def test_create_student(self):
      student = Student(lastname="Smith", firstname="Jonesy", year="SO")
      self.assertIsInstance(student, Student)
      self.assertEquals(student.display_name, "Smith, SO")