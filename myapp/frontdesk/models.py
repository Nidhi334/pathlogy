from django.db import models
# from .models import CustomUser

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')

        ],
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    ipList = models.TextField(blank=True, null=True)  # Assuming this is a list of IPs as text
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bdo = models.CharField(max_length=255, blank=True, null=True)
    altPhone = models.CharField(max_length=15)
    email = models.EmailField()
    workArea = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255)
    regNumber = models.CharField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "Unnamed"


class TestGroup(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    # created_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE , editable=False)
    status = models.BooleanField(choices=((True, 'Active'), (False, 'Inactive')), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Test(models.Model):
    sample_type = models.CharField(
        max_length=50,
        choices=[
        ('blood', 'Blood'),
        ('body_fluids', 'Body Fluids'),
        ('surgical_drain_fluids', 'Surgical Drain Fluids'),
        ('synovial_fluid', 'Synovial Fluid'),
        ('peritoneal_fluid', 'Peritoneal Fluid'),
    ], blank=True, null=True)

    group = models.ForeignKey(TestGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    timeframe = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.BooleanField(choices=((True, 'Active'), (False, 'Inactive')), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Package(models.Model):
    name = models.CharField(max_length=100)
    group =models.ForeignKey(TestGroup, on_delete=models.CASCADE)
    tests = models.ManyToManyField(Test)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    isactive = models.BooleanField(choices=((True, 'Active'), (False, 'Inactive')), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    



