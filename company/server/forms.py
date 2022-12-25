from django.forms import ModelForm

from company.server.models import Company, Employee


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'logo', 'description')


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'date_of_birth', 'photo', 'position','salary',
                  'company')
