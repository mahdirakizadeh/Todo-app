from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForms


def Home(request):
    # return HttpResponse("jon mani django")
    all = Todo.objects.all()
    return render(request, 'index.html', {'todos': all})


def Detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todoo': todo})


def Delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Delete was successfully", "success")
    return redirect('home')


def Create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(tittle=cd['tittle'], body=cd['body'], created=cd['created'])
            messages.success(request, "Todo created successfully", "success")
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def Update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully", "success")
            return redirect('details', todo_id)
    else:
        form = TodoUpdateForms(instance=todo)
    return render(request, 'update.html', {'form': form})
