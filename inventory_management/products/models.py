from django.db import models


class Product(models.Model):

    """ Product Model Definition """

    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to="gallery/")
    content = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()
    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, null=True)
