from django.contrib import messages

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from course.forms import CourseForm
from course.models import Course, Homework

# Guara el modelo y definimos cuantas queremos visualizar en la pagina principal
class CourseListView(ListView):
    model = Course
    paginate_by = 3
  
#  Muestra los detalles del modelo para la vista
class CourseDetailView(DetailView):
    model = Course
    fields = ["name", "code"]

# Crea un nuevo elemento
class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy("course:course-list")

    form_class = CourseForm
    
    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        actual_objects = Course.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El curso {data['name']} - {data['code']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Curso {data['name']} - {data['code']} creado exitosamente!",
            )
            return super().form_valid(form)

# Actualiza
class CourseUpdateView(UpdateView):
    model = Course
    fields = ["name", "code"]

    def get_success_url(self):
        course_id = self.kwargs["pk"]
        return reverse_lazy("course:course-detail", kwargs={"pk": course_id})

# Elimina
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course:course-list")