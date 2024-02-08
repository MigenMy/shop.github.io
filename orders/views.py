from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket

def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key

    data = request.POST
    product_id = data.get('product_id')
    nub = data.get('nub')
    product_name = data.get('product_name')
    is_delete = data.get("is_delete")
    print(is_delete)
    if is_delete == 'true':
        ProductInBasket.objects.filter(product_id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key = session_key,product_id = product_id, is_active = True, defaults={"nub":nub})
        if not created:
            new_product.nub+=int(nub)
            new_product.save(force_update=True)

     #common code for 2 cases
    products_total_nub = ProductInBasket.objects.filter(session_key=session_key, is_active = True).count()
    return_dict["products_total_nub"] = products_total_nub
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nub = products_in_basket.count()
    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nub
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)

