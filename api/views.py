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
def get_id(request,pk):
    if request.method=='GET':
        pupil=Pupil.objects.get(id=pk)
        return JsonResponse(model_to_dict(pupil))
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


def update(request,pk):
    pupil=Pupil.objects.get(id=pk)
    if request.method=='PUT':
        data=json.loads(request.body.decode('utf-8'))
        pupil.first_name=data.get('firstname',pupil.first_name)
        pupil.last_name=data.get('lastname',pupil.last_name)
        pupil.age=data.get('age',pupil.age)
        pupil.username=data.get('username',pupil.username)
            
        pupil.password=data.get('password',pupil.password)
        pupil.save()    
        return JsonResponse(model_to_dict(pupil))
def delete(request,pk):
    pupil=Pupil.objects.get(id=pk)
    if request.method=='DELETE':
        pupil.delete()
        return JsonResponse({'status':True},safe=False)

def get_contact(request):
    if request.method=='GET':
        contacts=Contact.objects.all()
        contact_json=[model_to_dict(contact) for contact in contacts]
        return JsonResponse(contact_json,safe=False)
    
def contact_id(request,pk):
    if request.method=='GET':
        contact=Contact.objects.get(pupil=pk)
        return JsonResponse(model_to_dict(contact))
    
def create_contact(request):
    pupils = Pupil.objects.last()
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        contact=Contact.objects.create(
            pupil=pupils,
            phone=data.get('phone'),
            email=data.get('email'),
            address=data.get('address')
        )
        return JsonResponse(model_to_dict(contact))
    
def update_contact(request,pk):
    contact=Contact.objects.get(pupil=pk)
    if request.method=='PUT':
        data = json.loads(request.body.decode('utf-8'))
       
        contact.phone = data.get('phone', contact.phone)
        contact.email = data.get('email', contact.email)
        contact.address = data.get('address', contact.address)
        contact.save()
        return JsonResponse(model_to_dict(contact))
    
def delete_contact(request,pk):
    contact=Contact.objects.get(id=pk)
    if request.method=='DELETE':
        contact.delete()
        return JsonResponse({'status':True},safe=False)