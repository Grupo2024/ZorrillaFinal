from django.db import models
from .models import *
import random

def create_pass_user(self):
        name_f = ""
        cantidad = 0
        r = random.randint(1111,9999)
        for a in self.nombre_t:
            cantidad = cantidad + 1
            if cantidad == 1:
                name_f = a
                break
            else:
                pass
        password = name_f + str(r) + self.apellido_t
        return password

def create_username(self):
    name_f = ""
    cantidad = 0
    r = random.randint(1111,9999)
    for a in self.nombre_t:
        cantidad = cantidad + 1
        if cantidad == 1:
            name_f = a
            break
        else:
            pass
    username = name_f + self.apellido_t
    return username
