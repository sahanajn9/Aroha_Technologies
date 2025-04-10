from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.models import AllTasks
from todoapp.forms import TaskForm,EditForm
from django.core.paginator import Paginator


# Create your views here.
def AddTasks(request):
    if request.method == 'POST':
        fm=TaskForm(request.POST)
        if fm.is_valid():
            # print("fm:",fm)
            # nm=request.POST.get('Task_name')
            # tk=request.POST.get('about_task')
            # print('nm:',nm)
            # print('tk:',tk)
            fm.save()
            return HttpResponse('<h2 style="color:green"> Your response has been saved</h2>')
        
    fm=TaskForm()
    return render(request,'Addtask.html',{'form':fm})

# def paginatorPage(request):
#     details=AllTasks.objects.all()
#     paginator=Paginator(details,5)
#     print("paginator:",paginator)
#     page=request.GET.get('pg')
#     print("page",page)
#     details=paginator.get_page(page)
#     print("data basedata:",details)
#     return render(request,'Alltask.html',{'details':details})


def DisplayAllTask(request):
    tasks=AllTasks.objects.all()
    paginator=Paginator(tasks,5)
    page_number=request.GET.get('pg')
    tasks=paginator.get_page(page_number)
    return render(request,'Alltask.html',{'form':tasks})

def EditTask(request,id=0):
    # data=AllTasks.objects.get(id=pk)
    data=AllTasks.objects.get(id=id)
    # print("id:",data['id'])
    fm=EditForm(instance=data)
    if request.method == 'POST':
        edata=EditForm(request.POST,instance=data)
        if edata.is_valid():
            edata.save()
            return redirect('display')
    
    return render(request,'edittask.html',{'form':fm})
    
def DeleteTask(request,id=0):
     data=AllTasks.objects.get(id=id)
     data.delete()
     return redirect('display')
     
        