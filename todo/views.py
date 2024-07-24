from django.shortcuts import render
from django.views import generic

from todo.models import Task


class HomePageView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/index.html"
    paginate_by = 5


