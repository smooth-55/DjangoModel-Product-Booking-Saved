from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Package(models.Model):
    image = models.ImageField(upload_to='dynamic_images')
    name = models.CharField(max_length=20) 
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    short_discription = models.TextField() 
    discription = models.TextField() 
    info_about_days = models.TextField() 
    created_on = models.DateTimeField(auto_now=True) 
    seats = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Package"
        db_table = "package_info"
        ordering = ['id']

    def __str__(self):
        return self.name

class Bookings(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField(default=1)
    booked_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "bookings"
        db_table = "bookings"
        ordering = ['-booked_on']

    def __str__(self):
        return self.package.name 

class Saved(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "saved"
        db_table = "saved"
        ordering = ['-saved_on']

    def __str__(self):
        return self.package.name





