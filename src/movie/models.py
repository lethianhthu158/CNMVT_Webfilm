from distutils.command.upload import upload
from email.mime import image
from pydoc import describe
from statistics import mode
from django.db import models
# from multiselectfield import Multiselectfield

# Create your models here.
CATEGORY_CHOICE = (
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE'),

)

LAGUAGE_CHOICES = (
    ('EN','ENGLISH'),
    ('VI','VIETNAM'),
)

STATUS_CHOICES = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

class Cast_and_Crew(models.Model):
    title_movie = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255)
    sub_character = models.CharField(max_length=255, blank=True) #not required
    image = models.ImageField(upload_to='cast')
    
    def __str__(self):
        return str(self.name) + ' - ' + self.character

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=1)
    language = models.CharField(choices=LAGUAGE_CHOICES,max_length=2)
    status = models.CharField(choices=STATUS_CHOICES,max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    director = models.CharField(max_length=100)
    writers = models.CharField(max_length=255)
    #stars
    episodes = models.PositiveIntegerField(default=1)

    cast_and_crew = models.ManyToManyField(Cast_and_Crew)

    def __str__(self):
        return str(self.title) 

class Episode(models.Model):
    title = models.ForeignKey(Movie,related_name="movie_episode", on_delete=models.CASCADE)
    # episodes = models.AutoField()
    number_episode = models.IntegerField(default=1)
    

