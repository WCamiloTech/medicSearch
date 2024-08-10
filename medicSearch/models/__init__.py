from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente')
)

from .Address import Address
from .City import City
from .DayWeek import DayWeek
from .Neighborhood import Neighborhood
from .Profile import Profile
from .Rating import Rating
from .Speciality import Speciality
from .State import State
