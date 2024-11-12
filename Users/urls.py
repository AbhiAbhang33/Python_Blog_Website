from django.urls import path,include
from Users import views as user_views

urlpatterns = [
    path('students/', user_views.students, name="students"),
]