# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def biblioteca(request):
    return render(request, 'biblioteca.html')
# Create your views here.
