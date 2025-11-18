from django.shortcuts import render
from .forms import UserForm, PROFS
from django.http import HttpResponse

users = [
    {'name': 'Golovnya',
     'phone': '8(983)324-33-33',
     'num': '1',
     'email': 'marina@mail.ru', 'prof': 'Менеджер'
     },
    {'name': 'Skripicyna',
     'phone': '8(983)324-03-33',
     'num': '2',
     'email': 'alena@mail.ru', 'prof': 'Программист'
     },
    {'name': 'Klyap',
     'phone': '8(983)324-33-73',
     'num': '3',
     'email': 'vladik@mail.ru', 'prof': 'Бухгалтер'
     }
]

def index(request):
    return render(request, "index.html", context={'users': users})

def routine(request):
    return render(request, "routine.html")

def addEmployee(request):
    if request.method=="POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            phone = userform.cleaned_data['phone']
            num = userform.cleaned_data['num']
            email = userform.cleaned_data['email']
            prof = int(userform.cleaned_data['prof'])
            prof = list(filter(lambda elem: elem[0] == prof, PROFS))[0][1]
            users.append({'name':name,
                          'phone':phone,
                          'num':num,
                          'email':email,
                          'prof':prof
                          })
        else:
            return HttpResponse('Invalid data')

    userform = UserForm()
    return render(request, 'addEmployee.html', {'form':userform})
