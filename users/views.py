from django.shortcuts import render
from django.views.generic import CreateView
from users.models import UserProfile


class PostProfileView(CreateView):
    models = UserProfile
    template_name = 'profile/profile.html'
    context_object_name = 'profiles'

    