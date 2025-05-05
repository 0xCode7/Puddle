from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from item.models import Item


# Create your views here.


@login_required(login_url='/login')
def index(request):
    products = Item.objects.filter(created_by=request.user).order_by('-is_sold', 'category')
    if request.method == "POST":
        search_query = request.POST.get('search_query')
        if search_query:
            products = (Item.objects.filter(created_by=request.user).filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                (Q(is_sold=1) if search_query.lower() == 'sold' else Q())
            ).order_by('-is_sold', 'category'))
            return render(request, 'dashboard/dashboard.html', {'products': products})

    return render(request, 'dashboard/dashboard.html', {'products': products})
