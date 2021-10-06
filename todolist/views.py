from django.shortcuts import redirect, render 
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):

    if request.method == 'POST':
        
        taskform = ListForm(request.POST or None)

        if taskform.is_valid:
            taskform.save()
            messages.success(request,'New task has been added!')
            all_item = List.objects.all
            return render(request, 'home.html', { 'all_item': all_item})
            
    else:
        all_item = List.objects.all
        return render(request, 'home.html', { 'all_item': all_item})
        

def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,'Task id ' + (list_id) + ' has been deleted')
    return redirect('home')


def crossoff(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        item = ListForm(request.POST or None, instance=item)

        if item.is_valid:
            item.save()
            messages.success(request,'Item has been edited successfully!')
            return redirect('home')
    else:
        item = List.objects.get(pk= list_id)
        return render(request, 'edit.html', { 'item': item})