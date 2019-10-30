from django.shortcuts import render
from django.http import HttpResponse
from .models import Login,User
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def fn_reg(req):
    try:
        data = json.loads(req.body)
        user = data['username']
        check_user = Login.objects.filter(username = user).exists()
        if check_user == False:
            uname = data['name']
            uage = data['age']
            umob = data['mob']
            upsw = data['password']
            role = 'user'
            if 'role' in data:
                role = data['role']
            log_obj = Login(username = user,password = upsw,role = role) 
            log_obj.save()
            if log_obj.id > 0:
                user_save = User(name = uname,age = uage, mob = umob,fk_login = log_obj)
                user_save.save()
                if user_save.id > 0:
                    return JsonResponse({'status':True,'res':"registration success"})
        return JsonResponse({'status':False,'res':"user already exists"})       
    except Exception as i:
        print(i)
        return JsonResponse({'status':False,'res':"registration failed"})

@csrf_exempt        
def fn_login(req):
    try:
        data = json.loads(req.body)
        user = data['name']
        psw = data['upsw']
        authant = Login.objects.filter(username=user,password=psw).exists()
        if authant:
            user_obj = Login.objects.get(username=user,password=psw)
            return JsonResponse({'status':True, 'userId':user_obj.id, 'role':user_obj.role})
        return JsonResponse({'status':False})    
    except Exception as i:
        print(i);
        return JsonResponse({'res':'login faild'})

def fn_userdata(req):
    userobjects = [];
    data =  User.objects.all()
    if data:
        for i in data:
            userobjects.append({
                'name':i.name,
                'age':i.age,
                'mob':i.mob,
                'username':i.fk_login.username
            })
    print(userobjects) 
    return  JsonResponse({'status':True,'res':userobjects})            

