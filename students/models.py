from django.db import models
from django.contrib.auth.models import User


students = models.ManyToManyField(User, related_name='courses_joined', blank=True)
