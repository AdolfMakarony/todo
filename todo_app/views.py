from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


# Create your views here.
def todo_main(request: WSGIRequest):
    user = request.user
    __todo_list_exists(user)

    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_todo(request)

        if action_type == 'destroy':
            todo = TodoTask.objects.get(pk=request.POST.get('task_id')).delete()
    all_tasks = TodoTask.objects.filter(todo_list__user=user).order_by('-id')



    return render(request,   'todo_main.html', {
        'tasks_array' : all_tasks.order_by('-id'),
    })

def __create_todo(request):
    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = TodoList.objects.get(user=request.user)
    todo.save()

def __todo_list_exists(user):
    if TodoList.objects.filter(user=user).exists():
        return
    TodoList(user=user, date=datetime.now()).save()


