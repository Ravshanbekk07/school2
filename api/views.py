from django.shortcuts import render
from .models import Pupil,Contact
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

def get_students(request):
    if request.method=='GET':
        pupils=Pupil.objects.all()
        pupil_json=[model_to_dict(pupil) for pupil in pupils]
        return JsonResponse(pupil_json,safe=False)

def create(request):
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        pupil=Pupil.objects.create(
            first_name=data.get('firstname'),
            last_name=data.get('lastname'),
            age=data.get('age'),
            username=data.get('username'),
            
            password=data.get('password')
            )
    return JsonResponse(model_to_dict(pupil))


