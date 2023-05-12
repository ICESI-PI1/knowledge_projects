from django.test import TestCase
from .models import State
from .models import Category
from .models import Project
from .models import Convocatory
from .models import Log


# Create your tests here.

class StateTestCase(TestCase):

    def test_state_creation(self):
        state = State.objects.create(
            state_id="ST001",
            state_name="Nombre del estado",
            description="Descripción del estado"
        )

        self.assertEqual(State.objects.count(), 1)
        self.assertEqual(state.state_id, "ST001")
        self.assertEqual(state.state_name, "Nombre del estado")
        self.assertEqual(state.description, "Descripción del estado")

    

class CategoryTestCase(TestCase):

    def test_create_category(self):
         # Crear una instancia de Category
         category = Category.objects.create(category_name="Test Category", icon_src="test_icon.png", description="Test description")

         # Verificar que la categoría se haya creado correctamente
         self.assertEqual(Category.objects.count(), 1)
         self.assertEqual(category.category_name, "Test Category")
         self.assertEqual(category.icon_src, "test_icon.png")
         self.assertEqual(category.description, "Test description")
    
    # Tests creating a Category object with valid inputs. 
    def test_create_category_valid_inputs(self):
        category = Category.objects.create(category_name="Test Category", icon_src="test.png", description="This is a test category")
        assert category.category_name == "Test Category"
        assert category.icon_src == "test.png"
        assert category.description == "This is a test category"

class ProjectTestCase(TestCase):

        # Tests creating a project with all required fields filled in. 
    def test_create_project_all_fields(self):
        state = State.objects.create(state_id="CA", state_name="California", description="Test state")
        category = Category.objects.create(category_name="Test category", icon_src="test.png", description="Test category")
        project = Project.objects.create(project_id="TEST1", project_name="Test project", project_description="Test description",
                                         result="Test result", scope="Test scope", work_plan="Test work plan",
                                         budget=10000, goal="Test goal", state=state, category=category)
        assert project.project_id == "TEST1"
        assert project.project_name == "Test project"
        assert project.project_description == "Test description"
        assert project.result == "Test result"
        assert project.scope == "Test scope"
        assert project.work_plan == "Test work plan"
        assert project.budget == 10000
        assert project.goal == "Test goal"
        assert project.state == state
        assert project.category == category

        
class ConvocatoryTestCase(TestCase):
        # Tests creating a Convocatory with valid data and linking it to a Project. 
    def test_create_convocatory_valid_data(self):
        state = State.objects.create(state_id="CA", state_name="California", description="Test state")
        category = Category.objects.create(category_name="Test category", icon_src="test.png", description="Test category")
        project = Project.objects.create(project_id="P001", project_name="Test Project", project_description="Test Description", result="Test Result", scope="Test Scope", work_plan="Test Work Plan", budget=1000, goal="Test Goal", state=state, category=category)
        convocatory = Convocatory.objects.create(convocatoryId="C001", start_date="2022-01-01", closing_date="2022-01-31", project=project)
        assert convocatory.convocatoryId == "C001"
        assert convocatory.start_date == "2022-01-01"
        assert convocatory.closing_date == "2022-01-31"
        assert convocatory.project == project
        
