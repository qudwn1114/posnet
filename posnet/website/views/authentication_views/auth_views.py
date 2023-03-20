from django.shortcuts import render, redirect, resolve_url
from django.views.generic import View, TemplateView
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings


class HomeView(View):
    '''
        메인 화면
        김병주/2023.03.20
    '''
    def get(self, request: HttpRequest, *args, **kwargs):
        context = {}

        return render(request, 'authentication/website_main.html', context)