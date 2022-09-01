from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Ecosystem(models.Model):
    MY_CHOICES = (
        (1,'Are there enabling policies and practices?'),
        (2,'Existing infrastructure to support ecosystems?'),
        (3,'Leaders, Partnerships and Allies?'),
        (4,'Public and/or Political Will?'),
        (5,'Familiarity and Commitment to the Ecosystems Vision in the community?'),
        (6,'Strong Community Partnerships?'),
        (7,'Urgency to address the issues at hand in new and different ways?'),
        (8,'Youth led efforts and organizations?'),
        (9,'Learner Centered Sites and organizations?'),
        (10,'Coordinator Role of individual or organization?'),
    )

    ecosystem_name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    template_name = MultiSelectField(choices=MY_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return self.ecosystem_name

class Eco_List(models.Model):
    eco_name = models.CharField(max_length=500)
    template_conditions = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.eco_name


