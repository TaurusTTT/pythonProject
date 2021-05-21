from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.
from .models import stuInfo


def toSubmit_view(request):
	return render(request,'submit.html')

def submit_view(request):
	id = request.POST.get('stuID','')
	name = request.POST.get('name','')
	v = request.POST.get('vaccinateornot','')
	stu = stuInfo(stu_id = id,stu_name = name,stu_vacci = v)
	stu.save()

	if id and name and v:
		c = stuInfo.objects.filter(stu_id = id).count
		if c == 0:
			stu = stuInfo(stu_id=id, stu_name=name, stu_vacci=v)
			stu.save()
			return HttpResponse("提交成功！")
		else:
			return HttpResponse("你已提交过该问卷！")
	else:
		return HttpResponse("请完整填写问卷！")