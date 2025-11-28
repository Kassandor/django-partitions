from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    pk = models.CompositePrimaryKey('id', 'created_at')
    id = models.IntegerField()
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    created_at = models.DateField()
    status = models.CharField(verbose_name='Статус', max_length=20)

    class Meta:
        db_table = 'django_orders'
