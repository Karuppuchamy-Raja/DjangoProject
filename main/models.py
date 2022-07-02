from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=10000, null=True, blank=True)
    price=models.FloatField()
    img=models.ImageField(null=True, blank=True)
    
    def safeurl(self):
        try:
            return self.img.url
        except:
            return 'https://images.unsplash.com/photo-1588087699156-a91fb26b1b1a?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=360&ixid=MnwxfDB8MXxyYW5kb218MHx8d2FybmluZ3x8fHx8fDE2NTY3MDA3NzE&ixlib=rb-1.2.1&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=640'
    
    def __str__(self):
        return self.name