from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_list.forms import TaskForm, TagCreateForm
from to_do_list.models import Task, Tag


class HomePageView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "to_do_list/home_page.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:home-page")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:home-page")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")


def toggle_complete_undo_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = False if task.status else True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:home-page"))


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("todo_list:tags-list")


class TagListView(generic.ListView):
    model = Tag


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tags-list")
