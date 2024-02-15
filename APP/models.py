from django.db import models

# Create your models here.
class Details(models.Model):
      movie_name=models.CharField(max_length=200)
      language=models.CharField(max_length=100)
      genre=models.CharField(max_length=100)
      duration=models.CharField(max_length=10)
      img=models.ImageField(upload_to='movies')
      def __str__(self):
        return self.movie_name
      
#class Favourites(models.Model):
      #movie_name=models.CharField(max_length=200)
      #language=models.CharField(max_length=100)
      #genre=models.CharField(max_length=100)
      #duration=models.CharField(max_length=10)
      #def __str__(self):
        return self.movie_name
      
class Favourite(models.Model):
    movie_name=models.ForeignKey(Details, on_delete=models.CASCADE)
    def __str__(self):
        return self.movie_name
      