from django.urls import path

from to_do_list.views import (
    HomePageView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
    toggle_complete_undo_task
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", toggle_complete_undo_task, name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),

]

app_name = "todo_list"
