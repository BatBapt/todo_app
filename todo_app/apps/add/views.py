from django.shortcuts import render

from .forms import AddTaskForm


def add(request):
    if request.method == "POST":
        print("here")
    else:
        add_form = AddTaskForm()
        context = {
            'add_form': add_form
        }
        return render(request, 'add.html', context)
