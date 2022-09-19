
def categories(request):
    from ki.models import Category
    return {'categories': Category.objects.all()}

def carts(request):
    from ki.models import Product
    return {"carts": Product.objects.filter(status_two=3)}