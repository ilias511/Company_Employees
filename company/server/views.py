from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as view

from company.server.forms import CompanyForm, EmployeeForm
from company.server.models import Company, Employee


# Create your views here.
class CompanyView(view.ListView):
    template_name = 'home.html'
    model = Company

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['companies'] = Company.objects.all()
        return data


class CreateCompany(view.CreateView):
    template_name = 'create-company.html'
    form_class = CompanyForm
    success_url = reverse_lazy('all companies')


class ViewCompany(view.DetailView):
    template_name = 'company_details.html'
    model = Company


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['company'] = Company.objects.get(id=)
        data['people'] = Employee.objects.filter(company_id=self.object.id)
        return data


class HireEmployee(view.CreateView):
    template_name = 'hire_employee.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('all companies')

class FireEmployee(view.DeleteView):
    model = Employee
    success_url = ('/')
    template_name = 'fire_employee.html'

class EditEmployee(view.UpdateView):
    model = Employee
    fields =('first_name', 'last_name', 'date_of_birth', 'photo', 'position','salary',
                  'company')
    template_name = 'edit_employee.html'

    def get_success_url(self):
        return reverse_lazy('all companies')

class DeleteCompany(view.DeleteView):
    model = Company
    success_url = ('/')
    template_name = 'delete_company.html'