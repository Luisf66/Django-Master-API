from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('Portugal', 'Portugal'),
    ('Germany', 'Alemanha'),
    ('France', 'França'),
    ('Italy', 'Italia'),
    ('Spain', 'Espanha'),
    ('England', 'Inglaterra'),
    ('Mexico', 'Mexico'),
    ('Chile', 'Chile'),
    ('Colombia', 'Colombia'),
    ('Argentina', 'Argentina'),
    ('Peru', 'Peru'),
    ('Bolivia', 'Bolivia'),
)

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name