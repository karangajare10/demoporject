from django.http import HttpResponse
from django.shortcuts import redirect, render
from website import models  

# Create your views here.
def home(req):
    return render(req,"home.html")

def save_student(req):
    student = models.Student(
        student_date = req.POST['date'],
        student_time = req.POST['time'],
        student_duration = req.POST['duration'],
        student_course = req.POST['course'],
        student_image = req.FILES['image']
    
    )
    student.save()
    
    return redirect("/")
    # return HttpResponse("Data is received and saved successfully!")  

def show_list(req):
    student = models.Student.objects.all()
    obj = {"student":student}
    return render(req,"show_list.html",obj)

def delete_student(req):
    old_student = models.Student.objects.get(id = req.GET['id']).delete()
    # return HttpResponse("Your data delete")
    return redirect("/show_list")
    


def edit_account(req):
    old_account = models.Student.objects.get(id = req.GET['id'])
    obj = {"old_account":old_account}
    return render(req,"edit_account.html",obj)

def update_account(req):
    old_account =models.Student.objects.get(id = req.POST['id'])
    old_account.student_date= req.POST['student_date']
    old_account.student_time = req.POST['student_time']
    old_account.student_duration = req.POST['student_duration']
    old_account.student_course = req.POST['student_course']
    old_account.student_image = req.FILES['student_image']  
    old_account.save()
    return redirect("/")

def sidebar(req):
    return render(req,"sidebar.html")

    




   