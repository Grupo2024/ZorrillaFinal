from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import AnonymousUser, User, Group

def check_Director(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    return False

def check_Director_or_Profesor(user):
    if Group.objects.get(name='Director') in user.groups.all():
        return True
    elif Group.objects.get(name='Profesor') in user.groups.all():
        return True
    return False