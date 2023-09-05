from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test Recipe object
        Recipe.objects.create(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredient 1, Test Ingredient 2',
            cooking_time=30,
            rating='yum'
        )

    def test_title_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_ingredients(self):
        recipe = Recipe.objects.get(id=1)
        ingredients = recipe.ingredients
        self.assertEqual(ingredients, 'Test Ingredient 1, Test Ingredient 2')

    def test_cooking_time_positive(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertTrue(cooking_time >= 0)

    
