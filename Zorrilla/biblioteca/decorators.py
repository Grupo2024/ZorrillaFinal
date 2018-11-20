from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import AnonymousUser, User, Group

def check_Director(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    return False

def check_Profesor(user):
    if Group.objects.get(name='Profesor') in user.groups.all():
        return True
    return False

def check_Secretaria(user):
    if Group.objects.get(name='Secretaria') in user.groups.all():
        return True
    return False

def check_Admin_s(user):
    if Group.objects.get(name='Admin_Secretaria') in user.groups.all():
        return True
    return False

def check_Director_or_Profesor(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    elif Group.objects.get(name='Profesor') in user.groups.all():
        return True
    return False

def check_Director_or_Secretaria(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    elif Group.objects.get(name='Secretaria') in user.groups.all():
        return True
    return False

def check_Profesor_or_Secretaria(user):
    if Group.objects.get(name='Secretaria') in user.groups.all():
        return True
    elif Group.objects.get(name='Profesor') in user.groups.all():
        return True
    return False
