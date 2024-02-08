from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()    #поле базы с типом данных почты
    name = models.CharField(max_length = 128)  #буквенный тип поля
    coment = models.CharField(max_length = 128)  #буквенный тип поля



    #def __str__(self):
     #   return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Mysubscriber'
        verbose_name_plural = 'Subscribers'
