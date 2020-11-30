from django.shortcuts import render

from apps.task.models import Task, Category


def frontpage(request):
    tasks = Task.objects.all().order_by('due_date').filter(done=False)
    print(tasks)
    context = {
        "tasks": tasks
    }
    return render(request, 'frontpage.html', context)
