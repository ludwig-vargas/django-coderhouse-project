from datetime import datetime
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello !!, this is my first view in Django!!!")

def title(request):
    return HttpResponse("<h1>This is a Title in H1</h1>")

def my_name_is(request, name, age):
    documentText = f"Mi nombre es: <br><br> {name} <br><br> Mi edad multiplicada por 2: {age*2}"
    return HttpResponse(documentText)

def calculate_age(request, birth_day):
    birth_day = datetime.strptime(birth_day, '%Y-%m-%d')
    print(type(birth_day))
    delta_time = datetime.now() - birth_day
    days_by_year = 365.25
    
    http_response = '''
    <br><br>
    I´m {years} years, {months} months, {days} days old.
    '''.format(
        years=int(delta_time.days // days_by_year),
        months=int((delta_time.days % days_by_year) // 30),
        days=int((delta_time.days % days_by_year) % 30)
    )
    return HttpResponse(http_response)