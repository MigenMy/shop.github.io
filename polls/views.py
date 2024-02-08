from django.shortcuts import render
from .forms import SubscribersForm
from products.models import ProductImage


def index(request):
    name = 'Андрей'
    form = SubscribersForm(request.POST or None)   #добавляем форму

    if request.method == "POST" and form.is_valid():   #принимаем форму

        pDict = request.POST.copy()
        form = SubscribersForm(pDict)  # if not valid shows error with previous post values in corresponding field
        form.save() #сохраняем
        form = SubscribersForm()  # show empty form no need to give HttpResponseRedirect()

    return render(request, 'landing/landing.html', locals())

def home(request):

    products_images_phones = ProductImage.objects.filter(is_active = True, is_main = True, product__category__id = 3)
    products_images_laptops = ProductImage.objects.filter(is_active=True, is_main=True, product__category__id=4)
    return render(request, 'home/home.html', locals())
