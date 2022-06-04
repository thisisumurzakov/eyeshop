from django.db import models

class Category(models.Model):
    GENDER = (
        ("M", "Man"),
        ("W", "Woman")
    )
    icon = models.ImageField(upload_to='category/', null=True, blank=True)
    title = models.CharField(max_length=250)
    gender = models.CharField(max_length=1,
                              choices=GENDER)

    def __str__(self):
        return self.title

class Product(models.Model):
    SHADE = (
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Autumn", "Autumn"),
        ("Winter", "Winter")
    )
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    shade = models.CharField(max_length=6, choices=SHADE)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title
