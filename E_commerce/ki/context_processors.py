
def categories(request):
    from ki.models import Category
    return {'categories': Category.objects.all()}

