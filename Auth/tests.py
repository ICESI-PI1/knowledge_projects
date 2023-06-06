from django.test import TestCase
from .models import User
from .models import Client
from django.test import TestCase
from .models import Client, User
from .models import Employee
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Client, User




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

   
    def test_access_client_fields(self):
        user = User.objects.create(username='testuser', password='testpassword', is_client=True)
        client = Client.objects.create(user=user, name='Test Client', phone_number='1234567890', address='Test Address', representative_name='Test Rep', phone_number_representative='0987654321')
        assert client.name == 'Test Client'
        assert client.phone_number == '1234567890'
        assert client.address == 'Test Address'
        assert client.representative_name == 'Test Rep'
        assert client.phone_number_representative == '0987654321'

  
    def test_create_client_invalid_fields(self):
        user = User.objects.create(username='testuser', password='testpassword', is_client=True)

        invalid_phone_number = '123'  # Teléfono inválido, no cumple con la longitud mínima requerida
        invalid_address = ''  # Dirección vacía, no se permite un valor vacío
        invalid_representative_name = 'Test Rep'  # Nombre de representante inválido, no cumple con la longitud mínima requerida

        # Attempt to create Client object with invalid fields
        client = Client(
            user=user,
            name='Test Client',
            phone_number=invalid_phone_number,
            address=invalid_address,
            representative_name=invalid_representative_name,
            phone_number_representative=''
        )

        with self.assertRaises(ValidationError) as context:
            client.full_clean()

                
    def test_create_client_exceeding_length_fields(self):
        user = User.objects.create(username='testuser', password='testpassword', is_client=True)

        long_name = 'A' * 31  # Excede el límite de 30 caracteres
        long_phone_number = '1' * 21  # Excede el límite de 20 caracteres
        long_address = 'A' * 21  # Excede el límite de 20 caracteres
        long_representative_name = 'B' * 31  # Excede el límite de 30 caracteres
        long_phone_number_representative = '2' * 21  # Excede el límite de 20 caracteres

        # Attempt to create Client object with exceeding length fields
        client = Client(
            user=user,
            name=long_name,
            phone_number=long_phone_number,
            address=long_address,
            representative_name=long_representative_name,
            phone_number_representative=long_phone_number_representative
        )
        
        with self.assertRaises(ValidationError):
            client.full_clean()


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
            birth_date="1990-01-01"
        )

        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(employee.user, self.user)
        self.assertEqual(employee.first_name, "Nombre del empleado")
        self.assertEqual(employee.last_name, "Apellido del empleado")
        self.assertEqual(str(employee.birth_date), "1990-01-01")

    def test_is_employee_false(self):
        user = User.objects.create_user(
            username="Maria",
            password='maria123',
            is_employee=False
        )

        self.assertFalse(user.is_employee)

    def test_first_name_max_length(self):
        max_length = Employee._meta.get_field('first_name').max_length
        employee = Employee.objects.create(
            user=self.user,
            first_name="X" * max_length,
            last_name="Apellido del empleado",
            birth_date="1990-01-01"
        )
        self.assertEqual(employee.first_name, "X" * max_length)

    def test_last_name_max_length(self):
        max_length = Employee._meta.get_field('last_name').max_length
        employee = Employee.objects.create(
            user=self.user,
            first_name="Nombre del empleado",
            last_name="X" * max_length,
            birth_date="1990-01-01"
        )
        self.assertEqual(employee.last_name, "X" * max_length)

    def test_first_name_max_length_exceeds(self):
        max_length = Employee._meta.get_field('first_name').max_length
        with self.assertRaises(Exception):
            employee = Employee.objects.create(
                user=self.user,
                first_name="X" * (max_length + 1),
                last_name="Apellido del empleado",
                birth_date="1990-01-01"
            )
            employee.full_clean()

    def test_last_name_max_length_exceeds(self):
        max_length = Employee._meta.get_field('last_name').max_length
        with self.assertRaises(Exception):
            employee = Employee.objects.create(
                user=self.user,
                first_name="Nombre del empleado",
                last_name="X" * (max_length + 1),
                birth_date="1990-01-01"
            )
            employee.full_clean()

    def test_first_name_required(self):
        with self.assertRaises(Exception):
            employee = Employee.objects.create(
                user=self.user,
                last_name="Apellido del empleado",
                birth_date="1990-01-01"
            )
            employee.full_clean()

    def test_last_name_required(self):
        with self.assertRaises(Exception):
            employee = Employee.objects.create(
                user=self.user,
                first_name="Nombre del empleado",
                birth_date="1990-01-01"
            )
            employee.full_clean()

    def test_picture_required(self):
        with self.assertRaises(Exception):
            employee = Employee.objects.create(
                user=self.user,
                first_name="Nombre del empleado",
                last_name="Apellido del empleado",
                birth_date="1990-01-01"
            )
            employee.full_clean()

    