import os
import re
import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator # can be changed to import * to import all validators if needed
from django.contrib.auth.models import User

# Function to return a default user
def get_default_user():
    return User.objects.first()  # Replace with logic to get a default user

# Create your models here.
class BookEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)
    isbn_13 = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(13), MaxLengthValidator(13)]
    )
    isbn_10 = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)]
    )
    published_date = models.DateField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=99999, decimal_places=2)
    rating_star = models.DecimalField(max_digits=2, 
                                      decimal_places=1,
                                      validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
                                      default=0.0
    )
    rating_count = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    author = models.CharField(max_length=50)
    time_added = models.DateTimeField(auto_now_add=True)
    review_list = models.JSONField(default=dict)
    publisher = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    @property
    def average_rating(self):
        if not self.review_list:
            return 0.0
        return sum(self.review_list.values()) / len(self.review_list)
    
    # When deployed, app should not display the initial images because the images are gitignored
    def image_url(self):
        # Replace spaces with underscores and add the file extension
        image_name = re.sub(r'\W+', '_', self.name).lower()
        extentions = ['jpg', 'jpeg', 'png']
        media_dir = os.path.join(settings.MEDIA_ROOT, 'image/books')

        # Check if the image exists with any of the extensions (jpg, jpeg, png)
        for ext in extentions:
            if os.path.exists(os.path.join(media_dir, image_name + '.' + ext)):
                return f'image/books/{image_name}.{ext}'
            
        return 'image/books/default.jpg'
    
    def is_in_stock(self):
        return self.quantity > 0
    
    def add_review(self, reviewer, rating):
        self.review_list[reviewer] = rating
        self.rating_star = len(self.review_list.values()) / len(self.review_list)
        self.save()

    def add_discount(self, discount_percentage=0):
        self.price = self.price - (self.price * discount_percentage / 100)
        self.save()

    def add_stock(self, quantity):
        self.quantity += quantity
        self.save()