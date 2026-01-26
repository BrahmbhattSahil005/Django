from django.shortcuts import render

# Create your views here.
def result_view(request):
    result=""
    percentage=""
    grade=""
    if request.method=="POST":
        s1=int(request.POST.get("s1",0))
        s2=int(request.POST.get("s2",0))
        s3=int(request.POST.get("s3",0))

        total=s1+s2+s3
        percentage = total/3

        if s1>=40 and s2>=40 and s3>=40:

            result="pass"
        else:
            result="fail"

        if percentage>=85:
            grade="A"
        elif percentage>=70:
            grade="B"
        elif percentage>=55:
            grade="C"
        elif percentage>=40:
            grade="D"
        
        else:
            grade="fail"
        
    return render(request,"result.html",{
        "result":result,
        "percentage":percentage,
        "grade":grade
        })

