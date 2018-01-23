from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import reverse
from django.forms import ModelForm
from app01 import models


class ClassModel(ModelForm):

    class Meta:
        model = models.Class_list
        fields = "__all__"

        error_messages = {
            'name': {'required': '班级不能为空'},
        }






def classList(request):

    class_obj = models.Class_list.objects.all()

    return render(request,"class_list.html",{"class_obj":class_obj})



def classAdd(request):
    if request.method == "GET":
        form = ClassModel()
        return render(request,"class_add.html",{"form":form})
    else:
        form = ClassModel(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/classlist/')

        return render(request, 'class_add.html', {"form":form})





def classEdit(request,nid):

    obj = models.Class_list.objects.filter(id=nid).first()

    if request.method == "GET":
        form = ClassModel(instance=obj)

        return render(request, 'class_edit.html',{"form":form})
    else:
        form = ClassModel(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/classlist/')

        return render(request, 'class_edit.html', {"form":form})



