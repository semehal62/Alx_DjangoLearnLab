from django.db import models

# Create your models here.
# practice_relationships/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    # ForeignKey: A Department belongs to one Company
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    # on_delete=models.CASCADE means if a Company is deleted, all its Departments are also deleted.

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # ForeignKey: An Employee belongs to one Department
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    # on_delete=models.SET_NULL means if a Department is deleted, employees in that department will have their department field set to NULL.
    # null=True, blank=True are required for SET_NULL to work.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# practice_relationships/models.py (continued)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    # OneToOneField: Links a ProductDetail to exactly one Product
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='details')
    # primary_key=True is often used with OneToOneField if the primary key of ProductDetail is also the FK to Product.
    # on_delete=models.CASCADE means if the Product is deleted, its ProductDetail is also deleted.
    description = models.TextField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    manufacturing_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Details for {self.product.name}"
# practice_relationships/models.py (continued)

class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=10, unique=True)
    # ManyToManyField: Defines the many-to-many relationship
    students = models.ManyToManyField(Student, related_name='courses_enrolled')
    # related_name='courses_enrolled' allows you to access courses from a student instance: student.courses_enrolled.all()

    def __str__(self):
        return self.title
