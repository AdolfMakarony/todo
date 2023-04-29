from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import TodoTask, TodoStatus, TodoList


# Create your views here.
def todo_main(request: WSGIRequest):
    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_todo(request)

        if action_type == 'destroy':
            todo = TodoTask.objects.get(pk=request.POST.get('task_id')).delete()
    # all_tasks = TodoTask.objects.all()


    return render(request,   'todo_main.html', {
        'tasks_array' : TodoTask.objects.all().order_by('-id'),
        'tasks_counts' : TodoTask.objects.all().count(),
    })

def __create_todo(request):
    todo = TodoTask()
    todo.title = request.POST.get('title')
    todo.status = TodoStatus.objects.get(pk=TodoStatus.C_NOT_COMPLETED)
    todo.create_at = datetime.now()
    todo.text = ''
    todo.todo_list = TodoList.objects.get(pk=1)
    todo.save()


