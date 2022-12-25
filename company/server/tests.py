from django import test as django_test
from django.urls import reverse

from company.server.models import Employee, Company



class TestHomePageView(django_test.TestCase):

    def test_project_home_page(self):
        client = django_test.Client()

        response = client.get(reverse('all companies'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_project_home_page_with_company(self):
        client = django_test.Client()
        company = Company.objects.create(
            name='Tesla',
            logo='https://scontent.fskg3-1.fna.fbcdn.net/v/t1.18169-9/1496620_631467996919883_902845890_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xQj2Xnrt_g8AX-bVKr8&_nc_ht=scontent.fskg3-1.fna&oh=00_AfDHSBvmHD1oO7Zj-gANMZEKoFwtbelw1dzQrQmvuSMQ5g&oe=63D00A19',
            description='Going Electric is the best option for the environment,also we accept Bitcoin and Dogecoin'
        )
        response = client.get(reverse('all companies'))

        self.assertTemplateUsed(response,'home.html')
        self.assertIsNotNone(company)

class TestCreateCompanyView(django_test.TestCase):

    def test_create_company(self):
        client = django_test.Client()
        company = Company.objects.create(
            name='Tesla',
            logo='https://scontent.fskg3-1.fna.fbcdn.net/v/t1.18169-9/1496620_631467996919883_902845890_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xQj2Xnrt_g8AX-bVKr8&_nc_ht=scontent.fskg3-1.fna&oh=00_AfDHSBvmHD1oO7Zj-gANMZEKoFwtbelw1dzQrQmvuSMQ5g&oe=63D00A19',
            description='Going Electric is the best option for the environment,also we accept Bitcoin and Dogecoin'
        )
        response = client.get(reverse('create company'))
        self.assertTemplateUsed(response,'create-company.html')


class TestHireEmployeeToCompany(django_test.TestCase):

    def test_hire_employee_to_company(self):
        client = django_test.Client()
        company = Company.objects.create(
            name='Tesla',
            logo='https://scontent.fskg3-1.fna.fbcdn.net/v/t1.18169-9/1496620_631467996919883_902845890_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xQj2Xnrt_g8AX-bVKr8&_nc_ht=scontent.fskg3-1.fna&oh=00_AfDHSBvmHD1oO7Zj-gANMZEKoFwtbelw1dzQrQmvuSMQ5g&oe=63D00A19',
            description='Going Electric is the best option for the environment,also we accept Bitcoin and Dogecoin'
        )
        employee = Employee.objects.create(
            first_name='Andrew',
            last_name= 'Tate',
            date_of_birth= '2003-2-2',
            photo='https://scontent.fskg3-1.fna.fbcdn.net/v/t1.18169-9/1496620_631467996919883_902845890_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xQj2Xnrt_g8AX-bVKr8&_nc_ht=scontent.fskg3-1.fna&oh=00_AfDHSBvmHD1oO7Zj-gANMZEKoFwtbelw1dzQrQmvuSMQ5g&oe=63D00A19',
            position='CEO',
            salary=2000,
            company=company
        )
        response = client.get(reverse('hire employee'))
        self.assertTemplateUsed('hire_employee.html')
        self.assertIsNotNone(company)
        self.assertIsNotNone(employee)
