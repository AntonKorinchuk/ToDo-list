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
    toggle_complate_task
)

urlpatterns = [
    path(
        "",
        HomePageView.as_view(),
        name="index"
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/complate/",
        toggle_complate_task,
        name="task-complete"
    ),
    path(
        "tags/",
        TagsListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagsCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagsUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagsDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "todo"
