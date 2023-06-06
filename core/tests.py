from django.test import TestCase
from .models import State
from .models import Category
from .models import Project
from .models import Convocatory
from .models import Log
from .models import Binnacle
from .models import User
from .models import Donation
from .models import Suggestion
from .models import Comments
from .models import Client
from .models import Beneficiary
from django.core.exceptions import ValidationError


# Create your tests here.

class StateTestCase(TestCase):

    def test_valid_state_creation(self):
        # Caso de prueba para crear un objeto State válido
        state = State(state_name="Valid State", description="Valid description")
        self.assertEqual(state.state_name, "Valid State")
        self.assertEqual(state.description, "Valid description")

    def test_state_name_exceeding_limit(self):
        # Caso de prueba para crear un objeto State con state_name excediendo el límite de longitud
        long_state_name = 'A' * 31
        with self.assertRaises(ValidationError):
            State(state_name=long_state_name, description="Exceeded limit state name").full_clean()

    def test_empty_description(self):
        # Caso de prueba para crear un objeto State con description vacío
        state = State(state_name="State with empty description", description="")
        self.assertEqual(state.state_name, "State with empty description")
        self.assertEqual(state.description, "")

    def test_all_fields_empty(self):
        # Caso de prueba para crear un objeto State con todos los campos vacíos
        with self.assertRaises(ValidationError):
            State().full_clean()

    

class CategoryTestCase(TestCase):

    def setUp(self):
        Category.objects.create(category_name="Category 1", icon_src="icon1.png", description="Description 1")
        Category.objects.create(category_name="Category 2", icon_src="icon2.png", description="Description 2")

    def test_category_str(self):
        category = Category.objects.get(category_name="Category 1")
        self.assertEqual(str(category), "Category 1")

    def test_category_id(self):
        category = Category.objects.get(category_name="Category 2")
        self.assertEqual(category.category_id, 2)

    def test_create_category_valid_fields(self):
        # Attempt to create Category object with valid fields
        category = Category(category_name="New Category", icon_src="new_icon.png", description="New description")
        category.save()

        # Verify if the category was created successfully
        self.assertIsNotNone(category.category_id)
        self.assertEqual(category.category_name, "New Category")
        self.assertEqual(category.icon_src, "new_icon.png")
        self.assertEqual(category.description, "New description")

    def test_create_category_empty_fields(self):
        # Attempt to create Category object with empty fields
        category = Category(category_name="", icon_src="", description="")
        with self.assertRaises(ValidationError):
            category.full_clean()

    def test_update_category_fields(self):
        category = Category.objects.get(category_name="Category 1")
        category.icon_src = "new_icon.png"
        category.description = "Updated description"
        category.save()

        # Verify if the category fields were updated successfully
        updated_category = Category.objects.get(category_id=category.category_id)
        self.assertEqual(updated_category.icon_src, "new_icon.png")
        self.assertEqual(updated_category.description, "Updated description")

    def test_delete_category(self):
        category = Category.objects.get(category_name="Category 2")
        category.delete()

        # Verify if the category was deleted successfully
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(category_name="Category 2")

class ProjectTestCase(TestCase):

        # Tests the creation of a project with related objects (State, Category, Convocatory).
    def test_project_creation_related_objects(self):
        # Crear un objeto Project con objetos relacionados (State, Category, Convocatory)
        project = Project(
            project_name="New Project",
            project_description="New Description",
            result="New Result",
            scope="New Scope",
            work_plan="New Work Plan",
            budget=3000,
            goal="New Goal",
            state=State.objects.create(
                state_id="756864",
                state_name="Abierto",
                description="Proyecto abierto"
            ),
            convocatory=Convocatory.objects.create(
                
                convocatory_name="Convocatory 4",
                start_date="2023-01-01",
                closing_date="2023-01-31"
            ),
            category=Category.objects.create(
                category_id="12345",
                category_name="Category 3",
                icon_src="icon3.png",
                description="Description 3"
            )
        )
        project.save()

        # Verificar si el proyecto se creó correctamente
        self.assertIsNotNone(project.project_id)
        self.assertEqual(project.project_name, "New Project")
        self.assertEqual(project.project_description, "New Description")
        self.assertEqual(project.result, "New Result")
        self.assertEqual(project.scope, "New Scope")
        self.assertEqual(project.work_plan, "New Work Plan")
        self.assertEqual(project.budget, 3000)
        self.assertEqual(project.goal, "New Goal")
        self.assertEqual(project.state.state_name, "Abierto")
        self.assertEqual(project.convocatory.convocatory_name, "Convocatory 4")
        self.assertEqual(project.category.category_name, "Category 3")

    
        
class ConvocatoryTestCase(TestCase):
    def setUp(self):
        # Crear instancias de Convocatory para usar en las pruebas
        convocatory_1 = Convocatory.objects.create(
            convocatory_id="1",
            start_date="2023-01-01",
            closing_date="2023-01-31"
        )
        convocatory_2 = Convocatory.objects.create(
            convocatory_id="2",
            start_date="2023-02-01",
            closing_date="2023-02-28"
        )

    def test_create_convocatory_valid_fields(self):
        # Intentar crear un objeto Convocatory con campos válidos
        convocatory = Convocatory(
            convocatory_id="3",
            start_date="2023-03-01",
            closing_date="2023-03-31"
        )
        convocatory.save()

        # Verificar si la convocatoria se creó correctamente
        self.assertIsNotNone(convocatory.convocatory_id)
        self.assertEqual(convocatory.start_date, "2023-03-01")
        self.assertEqual(convocatory.closing_date, "2023-03-31")

    def test_create_convocatory_empty_fields(self):
        # Intentar crear un objeto Convocatory con campos vacíos
        convocatory = Convocatory(
            convocatory_id=None,
            start_date=None,
            closing_date=None
        )

        with self.assertRaises(ValidationError):
            convocatory.full_clean()

    
class BinnacleModelTestCase(TestCase):

    def setUp(self):
        project = Project.objects.create(
            project_id = "13456",
            project_name="Project 1",
            project_description="Description 1",
            result="Result 1",
            scope="Scope 1",
            work_plan="Work Plan 1",
            budget=1000,
            goal="Goal 1",
            state= State.objects.create(
                state_id="13543",
                state_name="Cerrado",
                description="Proyecto cerrado"
            ),
            convocatory = Convocatory.objects.create(
                convocatory_id="1",
                start_date="2023-01-01",
                closing_date="2023-01-31"
            ),
            category = Category.objects.create(category_name="Category 1", icon_src="icon1.png", description="Description 1")
        )
        Binnacle.objects.create(binnacle_id="11", project_id=project)
        Binnacle.objects.create(binnacle_id="22", project_id=project)

    def test_binnacle_id(self):
        binnacle = Binnacle.objects.get(binnacle_id="11")
        self.assertEqual(binnacle.binnacle_id, "11")

    def test_binnacle_project(self):
        binnacle = Binnacle.objects.get(binnacle_id="22")
        self.assertEqual(binnacle.project_id.project_name, "Project 1")

    def test_create_binnacle_valid_fields(self):
        project =  project = Project.objects.create(
            project_id = "23456",
            project_name="Project 2",
            project_description="Description 2",
            result="Result 2",
            scope="Scope 2",
            work_plan="Work Plan 2",
            budget=100,
            goal="Goal 2",
            state= State.objects.create(
                state_id="23543",
                state_name="Cerrado",
                description="Proyecto cerrado"
            ),
            convocatory = Convocatory.objects.create(
                convocatory_id="2",
                start_date="2023-01-01",
                closing_date="2023-01-31"
            ),
            category = Category.objects.create(category_name="Category 1", icon_src="icon1.png", description="Description 1")
        )
        binnacle = Binnacle(binnacle_id="33", project_id=project)
        binnacle.save()

        # Verificar si el binnacle se creó correctamente
        self.assertIsNotNone(binnacle.id)
        self.assertEqual(binnacle.binnacle_id, "33")
        self.assertEqual(binnacle.project_id, project)

    def test_create_binnacle_invalid_id(self):
        project = Project.objects.create(
            project_id = "33456",
            project_name="Project 3",
            project_description="Description 3",
            result="Result 3",
            scope="Scope 3",
            work_plan="Work Plan 3",
            budget=100,
            goal="Goal 3",
            state= State.objects.create(
                state_id="33543",
                state_name="Cerrado",
                description="Proyecto cerrado"
            ),
            convocatory = Convocatory.objects.create(
                convocatory_id="3",
                start_date="2023-01-01",
                closing_date="2023-01-31"
            ),
            category = Category.objects.create(category_name="Category 1", icon_src="icon1.png", description="Description 1")
        )
        binnacle = Binnacle(binnacle_id="", project_id=project)

        with self.assertRaises(ValidationError) as context:
            binnacle.full_clean()

        # Verificar los mensajes de error esperados
        expected_errors = {
            'binnacle_id': ['This field cannot be blank.']
        }
        self.assertDictEqual(context.exception.message_dict, expected_errors)
          
class DonationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword", email="test@test.com", is_client=True)

        state = State.objects.create(state_id="1000", state_name="California", description="Test state")
        category = Category.objects.create(category_name="Test category", icon_src="test.png", description="Test category")
        self.project = Project.objects.create(project_id=1123, project_name="Test project", project_description="Test description",
                                    result="Test result", scope="Test scope", work_plan="Test work plan",
                                    budget=10000, goal="Test goal", state=state, category=category)
        self.donation = Donation.objects.create(
            payment_method='Credit Card',
            amount=10000,
            user=self.user,
            project=self.project
        )

class SuggestionTestCase(TestCase):
        # Tests that a suggestion can be created with all required fields filled in correctly.
    def test_create_suggestion_happy_path(self):
        suggestion = Suggestion.objects.create(suggestion_name="Test Suggestion", suggestion_description="This is a test suggestion", suggestion_work_plan="This is the work plan for the test suggestion", suggestion_budget=1000)
        self.assertIsNotNone(suggestion.suggestion_id)

        # Tests that a suggestion can be updated with valid changes.
    def test_update_suggestion_happy_path(self):
        suggestion = Suggestion.objects.create(suggestion_name="Test Suggestion", suggestion_description="This is a test suggestion", suggestion_work_plan="This is the work plan for the test suggestion", suggestion_budget=1000)
        suggestion.suggestion_name = "Updated Test Suggestion"
        suggestion.save()
        updated_suggestion = Suggestion.objects.get(suggestion_id=suggestion.suggestion_id)
        self.assertEqual(updated_suggestion.suggestion_name, "Updated Test Suggestion")

        # Tests that a suggestion can be created with the maximum length for suggestion_name and suggestion_description.
    def test_create_suggestion_max_length(self):
        suggestion = Suggestion.objects.create(suggestion_name="A"*50, suggestion_description="B"*500, suggestion_work_plan="C"*1000, suggestion_budget=1000)
        self.assertIsNotNone(suggestion.suggestion_id)

        # Tests that a suggestion can be created with the minimum and maximum budget values.
    def test_create_suggestion_min_max_budget(self):
        suggestion = Suggestion.objects.create(suggestion_name="Test Suggestion", suggestion_description="This is a test suggestion", suggestion_work_plan="This is the work plan for the test suggestion", suggestion_budget=0)
        self.assertIsNotNone(suggestion.suggestion_id)
        suggestion = Suggestion.objects.create(suggestion_name="Test Suggestion", suggestion_description="This is a test suggestion", suggestion_work_plan="This is the work plan for the test suggestion", suggestion_budget=9999999999)
        self.assertIsNotNone(suggestion.suggestion_id)

        # Tests that a suggestion can be created with an empty suggestion_work_plan.
    def test_create_suggestion_empty_work_plan(self):
        suggestion = Suggestion.objects.create(suggestion_name="Test Suggestion", suggestion_description="This is a test suggestion", suggestion_work_plan="", suggestion_budget=1000)
        self.assertIsNotNone(suggestion.suggestion_id)



    
