from django.db import models


def graduating_eta(year):
    return year - 2023


class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    graduation = models.IntegerField(blank=True)
    year = models.CharField(
        max_length=25,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )

    @property
    def display_name(self):
        return f"{self.lastname}, {self.year}"
