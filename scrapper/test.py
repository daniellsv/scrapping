from django.contrib.auth.models import User
from django.test import TestCase
from .models import diario_as



class AuthTestCase(TestCase):

    def setUp(self):
        user, created = User.objects.update_or_create(username='daniel', email='dflorez@ñlsv-tech.com', is_superuser=True)
        user.set_password('123456')
        user.is_staff = True
        user.is_active = True
        user.save()

    def test_access_admin(self):
        response = self.client.get('/admin/auth/user/')
        self.assertRedirects(response, '/admin/login/?next=/admin/auth/user/')
        self.client.login(**{'username': 'daniel', 'password': '123456'})
        response = self.client.get('/admin/auth/user/')
        self.assertEqual(200, response.status_code)


class ModelProductTestCase(TestCase):

    def setUp(self):
        name_equipo = diario_as.objects.create(name='junior')

    def test_number_of_product(self):
        count = diario_as.objects.count()
        self.assertEqual(1, count)

    def test_str(self):
        name_equipo = diario_as.objects.last()
        self.assertEqual('junior', str(name_equipo))
