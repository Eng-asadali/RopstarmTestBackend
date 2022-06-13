from django.db import models

# Create your models here.

class vehicleCategory(models.Model):
    A = 'Active'
    I = 'Inactive'
    status_choices = [
        (A, 'Active'),
        (I, 'Inactive')
    ]
    name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, default=I, null=True, blank=True)

    def __str__(self):
        return self.name

class vehicle(models.Model):
    A = 'Active'
    I = 'Inactive'
    status_choices = [
        (A, 'Active'),
        (I, 'Inactive')
    ]
    name = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    modal = models.CharField(max_length=255, null=True, blank=True)
    makes = models.CharField(max_length=255, null=True, blank=True)
    registration = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, choices=status_choices, default=I, null=True, blank=True)
    parent_category = models.ForeignKey(vehicleCategory, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name