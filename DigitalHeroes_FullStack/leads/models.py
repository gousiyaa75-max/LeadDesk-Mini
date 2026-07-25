from django.db import models

class Lead(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Closed', 'Closed'),
    ]

    BUDGET_CHOICES = [
        ('<1000', 'Under $1000'),
        ('1000-5000', '$1000 - $5000'),
        ('5000+', '$5000+'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
