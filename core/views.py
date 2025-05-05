from django.shortcuts import render
from item.models import Item, Category


# Create your views here.
def index(request):
    products = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')
