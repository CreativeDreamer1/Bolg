from django.db import models

# A Model that stores all the information in database

class Product(models.Model):
    title = models.CharField(max_length=200, label="Title")
    description = models.TextField()
    image = models.ImageField(upload_to="products")
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()
    
    def shortDescription(self):
        words = self.description.split()
        if len(words) > 50:
            return " ".join(words[:30]) + "..."
        else:
            return self.description