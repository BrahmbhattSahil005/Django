from django.shortcuts import render

# Create your views here.
student=[
    {"id":1,"name":"mohit","course":"MCA"},
    {"id":2,"name":"rohit","course":"mscIT"},
]

def home(request):
    return render(request,"home.html",{"student":student})

def addnew(request):
    return render(request,"addnew.html")

def save(request):
    name=request.POST.get('name')
    course=request.POST.get('course')
    print(name)
    print(course)
    d={"id":3,'name':name,'course':course}
    student.append(d)
    return render(request,"home.html",{"student":student})