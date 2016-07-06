from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import ToDo
from .forms import ToDoForm
#import pdb; pdb.set_trace()


def todo_list(request):
    context = {'items': ToDo.objects.all()}
    return render(request, 'seeds/list.html', context)

def todo_create(request):
    context = {'form': ToDoForm(request.POST or None)}
    if request.POST:
        form = context['form']
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    return render(request, 'seeds/create.html', context)

def todo_detail(request, slug):
    context = {'item': get_object_or_404(ToDo, slug=slug),
               'users_list': User.objects.all().exclude(is_staff=True, is_superuser=True)}
    return render(request, 'seeds/detail.html', context)


def todo_delete(request, slug):
    item = get_object_or_404(ToDo, slug=slug)
    item.delete()
    return redirect('todo_list')


def todo_assign(request, todo_id):
    item = get_object_or_404(ToDo, id=todo_id)
    if request.POST:
        postdata = request.POST.copy()
        if 'assign_to' in postdata:
            user = User.objects.filter(id=postdata.get('assign_to')).first()
            if user is not None:
                item.assigned = user
                item.save()
    return redirect('todo_detail', slug=item.slug)


def todo_completed(request):
    if request.is_ajax() and request.POST:
        try:
            item = ToDo.objects.get(id=request.POST.get('todo_id'))
            item.status = 'Done'
            item.save()
            response = {'success': 'Success Done'}
        except Exception as e:
            response = {'error': e}
    else:
        response = {'error': 'Request Can\'t be process'}
    return JsonResponse(response)
