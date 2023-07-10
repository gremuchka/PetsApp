from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # модель юзера


class Pet(models.Model):
    objects = ''
    vin = models.CharField(verbose_name="Vin", db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name="Color", max_length=64)
    name = models.CharField(verbose_name="Name", max_length=64)
    age = models.IntegerField(verbose_name="Age")
    PET_BREED = (
        (1, 'Акита ину'),
        (2, 'Аляскинский маламут'),
        (3, 'Аргентинский дог'),
        (4, 'Доберман'),
        (5, 'Вельш корги пемброк'),
        (6, 'Такса'),
    )
    breed = models.IntegerField(verbose_name="Breed", choices=PET_BREED)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
