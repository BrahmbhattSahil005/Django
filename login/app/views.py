# from django.shortcuts import render

# # Create your views here.
# student=[
#     {"id":1,"name":"mohit","password":"mohit@123"},
#     {"id":2,"name":"rohit","password":"rohit@123"},
#     {"id":3,"name":"sujal","password":"sujal@123"},
# ]

# def home(request):
#     return render(request,"home.html")

# def login(request):
#     return render(request,"login.html")

# def error(request):
#     return render(request,"error.html")
#     name=request.POST.get('name')
#     password=request.POST.get('password')
#     print(name)
#     print(password)


from django.shortcuts import render, redirect


students = [
    {"id": 1, "name": "mohit",   "password": "mohit@123"},
    {"id": 2, "name": "rohit",   "password": "rohit@123"},
    {"id": 3, "name": "sujal",   "password": "sujal@123"},
]

def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()

    
        print(f"Login attempt → name: '{name}' | password: '{password}'")


        for student in students:
            if student["name"] == name and student["password"] == password:
             
                return redirect('home')   

     
        return redirect('error')

def error(request):
    return render(request, "error.html")

