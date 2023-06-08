from django.shortcuts import render,redirect,get_object_or_404
from.models import Task

def Add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        item_name=request.POST.get('item_name','')
        desc=request.POST.get('desc','')
        task=Task(slno=slno,item_name=item_name,desc=desc)
        task.save()
        # task=task.objects.all()
    return render(request,'index.html',{'task1':task1})

# Create your views here.
# def Crud(request):
#     return render(request,'index.html')
def Delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def Update(request,task_id1):
    task=get_object_or_404(Task,id=task_id1)
    if request.method=='POST':
        task.slno=request.POST.get('slno')
        task.item_name=request.POST.get('item_name')
        task.desc=request.POST.get('desc')
        
        task.save()
        return redirect('/')
        # task=task.objects.all()
    return render(request,'update.html',{'task':task})


    # f=TodoForm(request.POST OR None,instance=task)
    # if f.is_valid():
    #     f.save()
    #     return redirect('/')
    # return render(request,'update.html',{'f':f,})
