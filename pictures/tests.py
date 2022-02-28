from django.test import TestCase

# Create your tests here.
from .models import Category,Image,Location

class CategoryTest(TestCase):
  # setup method
  def setUp(self):
    self.travel = Category(cat_name='Travel')
  
  #Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.travel,Category))

  #Test Save method
  def test_save_category(self):
    self.travel.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories) > 0)
  
  #Test delete method
  def test_delete_category(self):
    self.travel.save_category()
    categories = Category.objects.all()
    self.travel.delete_category()
    self.assertTrue(len(categories) == 0)

class LocationTest(TestCase):
  # setup method
  def setUp(self):
    self.Nairobi = Location(loc_name='Nairobi')
  
  #Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.Nairobi,Location))

  #Test Save method
  def test_save_location(self):
    self.Nairobi.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations) > 0)
  
  #Test delete method
  def test_delete_location(self):
    self.Nairobi.save_location()
    locations = Location.objects.all()
    self.Nairobi.delete_location()
    self.assertTrue(len(locations) == 0)