from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    salary = models.FloatField()
    company = models.ForeignKey(Company, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def ord(self):
        class Meta:
            ordering = ('-salary',)

    def __str__(self):
        return (self.name + f" ({self.company.name}) | {self.salary}")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': {
                'id': self.company.id,
                'name': self.company.name,
                'description': self.company.description,
                'city': self.company.city,
                'address': self.company.address
            }
        }
