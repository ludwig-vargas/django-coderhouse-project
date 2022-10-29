from django import forms
from course.models import Course

class CourseForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del curso",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "Nombre de curso",
                "required": "True",
            }
        ),
    )
    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-code",
                "placeholder": "Código del curso",
                "required": "True",
            }
        ),
    )
    
    class Meta:
        model = Course
        fields = ["name", "code"]