from django.urls import path

from company.server.views import CompanyView,CreateCompany,ViewCompany,HireEmployee,FireEmployee,EditEmployee,DeleteCompany

urlpatterns = [
 path('',CompanyView.as_view(),name='all companies'),
 path('add-company/',CreateCompany.as_view(),name='create company'),
 path('view-company/<int:pk>',ViewCompany.as_view(),name = 'view company'),
 path('hire-employee/',HireEmployee.as_view(),name = 'hire employee'),
 path('fire-employee/<int:pk>',FireEmployee.as_view(),name='fire employee'),
 path('edit-employee/<int:pk>',EditEmployee.as_view(),name='edit employee'),
 path('delete-company/<int:pk>',DeleteCompany.as_view(),name='delete company')
]