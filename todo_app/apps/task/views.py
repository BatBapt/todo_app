from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone

from .forms import AddTaskForm, AddCategoryForm

from .models import Task, Category


def add_task(request):
    if request.method == "POST":
        add_form = AddTaskForm(request.POST)

        if add_form.is_valid():
            title = add_form.cleaned_data['title']
            content = add_form.cleaned_data['content']
            due_date = add_form.cleaned_data['due_date']
            category = Category.objects.get(name=request.POST['category'])
            new_task = Task(title=title, content=content, due_date=due_date, category=category, done=False)
            new_task.save()
            return redirect(reverse('accueil'))
    else:
        categories = Category.objects.all()
        add_form = AddTaskForm()
        context = {
            'add_form': add_form,
            'categories': categories
        }
        return render(request, 'add.html', context)


def done_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.date_done = timezone.now()
    task.save()
    return redirect(reverse('accueil'))


def done(request):
    tasks = Task.objects.all().filter(done=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'done.html', context)


def add_category(request):
    if request.method == "POST":
        add_form = AddCategoryForm(request.POST)

        if add_form.is_valid():
            name = add_form.cleaned_data['name']
            color = add_form.cleaned_data['color']
            category = Category(name=name, color=color)
            category.save()
            return redirect(reverse('category'))

    else:
        categories = Category.objects.all()
        add_form = AddCategoryForm()
        context = {
            "add_form": add_form,
            'categories': categories
        }
        return render(request, 'category.html', context)