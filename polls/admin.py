from django.contrib import admin
from .models import *




class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]        #какие колонки выводить в админке
    fields = ["email", "name"]     #какие поля выводить на редактирование
    #exclude = []            #какие поля убрать из редактирования
    list_filter = ["name"]      #будет показываться одинакеовые запипси
    search_fields = ["id", "name", "email"]         #появляется окно поиска по тем колонкам который я указал



    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)      #регистрируем модель

