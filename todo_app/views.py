from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo_app.models import TodoTask, TodoStatus, TodoList


# Create your views here.
def todo_main(request: WSGIRequest):
    user = request.user
    __todo_list_exists(user)
    all_tasks = TodoTask.objects.filter(todo_list__user=user).order_by('-id')

    if request.method == 'POST':
        action_type = request.POST.get('type')
        if action_type == 'create':
            __create_todo(request)

        if action_type == 'destroy':
            todo = TodoTask.objects.get(pk=request.POST.get('task_id')).delete()

    if request.method == 'GET':
        if request.GET.get('type') == 'change':
            my_task = TodoTask.objects.get(id=request.GET.get('task_id'))
            if my_task.status_id != 1:
                my_task.status_id = 1
            else:
                my_task.status_id = 2
            my_task.save(update_fields=['status_id'])

        if request.GET.get('status') == 'no':
            all_tasks = all_tasks.filter(status_id=1)

        if request.GET.get('status') == 'yes':
            all_tasks = all_tasks.filter(status_id=2)

        if request.GET.get('action') == 'clear-completed':
            print('OR')





    return render(request,   'todo_main.html', {
        'tasks_array' : all_tasks
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

def __clear_completed(request: WSGIRequest):
    user = request.user
    task_to_del = TodoTask.objects.filter(todo_list__user=user)
    task_to_del.filter(status_id=1).delete()
    return redirect('todo_main')
