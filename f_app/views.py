from django.shortcuts import render
from f_app.models import  questions

# Create your views here.
def index(request):
    question=questions()
    return render(request,'index.html')

def about(request):
    return render(request,'about.html',{'Name':'RAGT'})

def exam(request):
    message=""
    if request.method=="post":
        if request.POST['question']!="" & request.POST['answer']!="":
            question = questions(question=request.POST['question'],answer=request.POST['answer'])
            question.save()
            message="Add succesfully"

    return render(request,'exam.html',{'message':message})