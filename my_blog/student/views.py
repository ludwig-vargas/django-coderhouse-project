from re import template
from django.http import HttpResponse
from django.template import loader

from student.models import Studen

def create_student(request, name: str = 'name', last_name: str = 'last_name', email: str = 'email'):
    
    template = loader.get_template('template_studen.html')
    
    student = Studen(name = name, last_name = last_name, email = email)
    student.save()
    
    context_dict = {'student': student}
    render = template.render(context_dict)
    return HttpResponse(render)