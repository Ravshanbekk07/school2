import json
from .models import Course,Group,Pupil
from django.forms.models import model_to_dict
from django.http import JsonResponse

def to_dict(instance:Group):
     return {
        "id":instance.id,
        "name":instance.name,
        "course":instance.course.name,
        "students":[model_to_dict(student) for student in instance.students.all()]
    }

def get_allcourse(request):
    if request.method=='GET':
        courses =Course.objects.all()
        
        course_json=[model_to_dict(course) for course in courses]
        return JsonResponse(course_json,safe=False)

def get_course(request,pk):
    if request.method=='GET':
        course=Course.objects.get(id=pk)
        return JsonResponse(model_to_dict(course))
def create_course(request):
    if request.method =='POST':
        data = json.loads(request.body.decode('utf-8'))
        course = Course.objects.create(
        name = data.get('name'))
        return JsonResponse(model_to_dict(course))
def update_course(request,pk):
    if request.method == 'PUT':
        courses = Course.objects.get(id=pk)
        data = json.loads(request.body.decode('utf-8'))
        courses.name = data.get('name',courses.name)
        courses.save()
        return JsonResponse(model_to_dict(courses))    
def deletecourse(request,pk):
    if request.method =='DELETE':
        courses = Course.objects.get(id=pk)
        courses.delete()
        return JsonResponse({'deleted':True},safe=False)
        
def get_group(request):
    if request.method=='GET':
        groups=Group.objects.all()
        group_json=[model_to_dict(group) for group in groups]
        return JsonResponse(group_json,safe=False)

def group_id(request,pk):
     if request.method  == 'GET':
        groups = Group.objects.get(id = pk)
        return JsonResponse(to_dict(groups))
     

def create_group(request):
        if request.method=='POST':
            data = json.loads(request.body.decode('utf-8'))
            groups = Group.objects.create(
            name=data.get('name'),
            course=Course.objects.get(id=data.get('course')))
            return JsonResponse(model_to_dict(groups))


def update_group(request,pk):
    group = Group.objects.get(id = pk)
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        group.name = data.get('name',group.name)
        group.course=Course.objects.get(id = data.get('course'))

        group.save()
        return JsonResponse (model_to_dict(group))
    
def delete_group(request,pk):
    group = Group.objects.get(id =pk)
    if request.method == 'DELETE':
        group.delete()
        return JsonResponse({'delete':True},safe=False)
    

    