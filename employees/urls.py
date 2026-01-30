
from django.urls import path 

from . import views
urlpatterns = [
    path("" , views.emp_list , name="employees_list"),
    path("add/" , views.create_employees , name="create_employees"),
    path("edit/<int:id>" , views.edit_employees , name="edit_employees"),
    path("delete/<int:id>" , views.delete_employees , name="delete_employees"),
]