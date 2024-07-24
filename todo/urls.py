from django.urls import path

from todo.views import (
    HomePageView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

path("", HomePageView.as_view(), name="index")
path("create/", TaskCreateView.as_view(), name="task-create")
path("<int:pk>/update/", TaskUpdateView .as_view(), name="task-update")
path("<int:pk>/delete/", TaskDeleteView .as_view(), name="task-delete")
path("tags/", TagsListView.as_view(), name="tag-list")
path("tags/create/", TagsCreateView.as_view(), name="tag-create")
path("tags/<int:pk>/update/", TagsUpdateView .as_view(), name="tag-update")
path("tags/<int:pk>/update/", TagsDeleteView .as_view(), name="tag-update")

app_name = "todo"
