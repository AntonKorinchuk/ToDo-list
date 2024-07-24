from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/index.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo/tags-list.html"
    context_object_name = "tags"
    paginate_by = 5


class TagsCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")

class TagsUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


