from django.shortcuts import render ,get_object_or_404 ,redirect
from .form import EmployeesForm
from .models import Employees


def emp_list(request):
    queryset = Employees.objects.all()
    return render(request ,"emplist.html" ,{"EmpList" : queryset})


def create_employees(request):
    form = EmployeesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employees_list")
    return render(request , "form.html" , {"empForm" : form})

def edit_employees(request , id):
    employees = get_object_or_404(Employees , id=id)
    form = EmployeesForm(request.POST or None , instance=employees)
    if form.is_valid():
        form.save()
        return redirect('employees_list')
    return render(request , "form.html" , {"empForm" : form})

def delete_employees(request , id):
    employees = get_object_or_404(Employees , id=id)
    employees.delete()
    return redirect('employees_list')






