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

  @classmethod
  def display_locations(cls):
    locs = cls.objects.all()
    return locs

class Image(models.Model):
  image = models.ImageField(upload_to='images/',null=False)
  img_name = models.CharField(max_length=30)
  img_description = models.CharField(max_length=30)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.img_name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def display_images(cls):
    img = cls.objects.all()
    return img
    
  @classmethod
  def search_by_category(cls,search_term):
    categ = cls.objects.filter(category__cat_name__icontains=search_term)
    return categ

  @classmethod
  def filter_by_location(cls,loc):
    location_filter = Location.objects.filter(id=loc).first()
    images_by_location = cls.objects.filter(location=location_filter).all()
    return images_by_location

