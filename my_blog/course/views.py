from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from course.models import Course, Homework
from datetime import datetime


def create_course(request, name: str = "course", code: int = 0):

    template = loader.get_template("template_course.html")

    course = Course(name=name, code=code)
    course.save()  # save into the DB

    context_dict = {"course": course}
    render = template.render(context_dict)
    return HttpResponse(render)

def courses(request):
    courses = Course.objects.all()
    
    context_dict = {'courses': courses}
    
    return render(
        request = request,
        context = context_dict,
        template_name= 'course/courses_list.html'
    )
    
def create_homework(request, name: str, due_date: str):

    template = loader.get_template("template_homework.html")
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    homework = Homework(name=name, due_date=due_date, is_delivered=False)
    homework.save()  # save into the DB

    context_dict = {"homework": homework}
    render = template.render(context_dict)
    return HttpResponse(render)

def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {"homeworks": homeworks}

    return render(
        request=request,
        context=context_dict,
        template_name="course/homework_list.html",
    )