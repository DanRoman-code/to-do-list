from django import forms
import datetime

from to_do_list.models import Task, Tag


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={'rows': 5, 'cols': 55}),
            'deadline': DateTimeInput(),
        }


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
