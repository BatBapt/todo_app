from django.shortcuts import render

from apps.task.models import Task


def frontpage(request):
    tasks = Task.objects.all().order_by('due_date')
    context = {
        "tasks": tasks
    }
    print(context)
    return render(request, 'frontpage.html', context)
