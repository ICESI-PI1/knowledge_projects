from django.test import TestCase
from .models import User
from .models import Client
from .models import Employee




class UserTestCase(TestCase):
        # Tests creating a user with valid data. 
    def test_create_user_valid_data(self):
        user = User.objects.create(username="testuser", password="testpassword", email="test@test.com", is_client=True)
        assert user.username == "testuser"
        assert user.email == "test@test.com"
        assert user.is_client == True

    # Tests that a user can be saved with valid credentials. 
    def test_save_user_with_valid_credentials(self):
        user = User(username="testuser", password="testpassword")
        user.save()
        assert user.username == "testuser"
        assert user.check_password("testpassword")

        # Tests that the password is hashed when saved. 
    def test_password_hashing(self):
        user = User(username="testuser", password="testpassword")
        user.save()
        assert user.password != "testpassword"
        
        # Tests that is_client functionality works as expected. 
    def test_is_client_functionality(self):
        user = User(username="testuser", password="testpassword", is_client=True)
        user.save()
        assert user.is_client

        # Tests that is_employee functionality works as expected. 
    def test_is_employee_functionality(self):
        user = User(username="testuser", password="testpassword", is_employee=True)
        user.save()
        assert user.is_employee

    
        
class ClientTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Juan",
            password='juan123',
            is_client=True
        )

    def test_client_creation(self):
        client = Client.objects.create(
            user=self.user,
            name="Nombre del cliente",
            phone_number="1234567890",
            address="Dirección del cliente",
            representative_name="Nombre del representante",
            phone_number_representative="9876543210"
        )

        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(client.user, self.user)
        self.assertEqual(client.name, "Nombre del cliente")
        self.assertEqual(client.phone_number, "1234567890")
        self.assertEqual(client.address, "Dirección del cliente")
        self.assertEqual(client.representative_name, "Nombre del representante")
        self.assertEqual(client.phone_number_representative, "9876543210")

        # Tests the updating of a client's information. 
    def test_update_client_information(self):
        client = Client.objects.create(
            user=self.user,
            name="Nombre del cliente",
            phone_number="1234567890",
            address="Dirección del cliente",
            representative_name="Nombre del representante",
            phone_number_representative="9876543210"
        )

        client.name = "Nuevo nombre"
        client.save()

        updated_client = Client.objects.get(pk=client.pk)

        assert updated_client.name == "Nuevo nombre"


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Juan",
            password='juan123',
            is_employee=True
        )

    def test_employee_creation(self):
        employee = Employee.objects.create(
            user=self.user,
            first_name="Nombre del empleado",
            last_name="Apellido del empleado",
            picture="ruta/de/la/imagen.jpg",
            birth_date="1990-01-01"
        )

        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(employee.user, self.user)
        self.assertEqual(employee.first_name, "Nombre del empleado")
        self.assertEqual(employee.last_name, "Apellido del empleado")
        self.assertEqual(employee.picture, "ruta/de/la/imagen.jpg")
        self.assertEqual(str(employee.birth_date), "1990-01-01")
    
        # Tests the behavior when is_employee is set to False. 
    def test_is_employee_false(self):
        # General behavior test
        user = User.objects.create_user(
            username="Maria",
            password='maria123',
            is_employee=False
        )

        assert not user.is_employee