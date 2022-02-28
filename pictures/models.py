from django.db import models

# Create your models here.
class Category(models.Model):
  cat_name = models.CharField(max_length=30)

  def __str__(self):
    return self.cat_name
  
  def save_category(self):
    self.save()

  def delete_category(self):
    self.delete()

class Location(models.Model):
  loc_name = models.CharField(max_length=30)

  def __str__(self):
    return self.loc_name

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete()

class Image(models.Model):
  image = models.ImageField(upload_to='images/',null=False)
  img_name = models.CharField(max_length=30)
  img_description = models.CharField(max_length=30)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.img_name

