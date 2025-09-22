from django.db import models
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError


# Create your models here.

class Category(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    NAME_CHOICES = {
        'income': ['salary', 'freelance', 'investments', 'gifts', 'other'],
        'expense': ['groceries', 'rent', 'utilities', 'entertainment', 'transportation', 'health', 'other']
    }

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'type'], name='unique_name_type')
        ]
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    
    def clean(self):
        allowed_names = self.NAME_CHOICES.get(self.type, [])
        if self.name not in allowed_names:
            raise ValidationError(f"Invalid category name '{self.name}' for type '{self.type}'. Allowed names are: {allowed_names}")
        
    
    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


