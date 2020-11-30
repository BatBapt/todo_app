from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import AddTaskForm

from .models import Task, Category


def add_task(request):
    if request.method == "POST":
        add_form = AddTaskForm(request.POST)

        if add_form.is_valid():
            title = add_form.cleaned_data['title']
            content = add_form.cleaned_data['content']
            due_date = add_form.cleaned_data['due_date']
            category = add_form.cleaned_data['category_choice']
            category = Category.objects.get(name=category)
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
    task.save()
    return redirect(reverse('accueil'))


