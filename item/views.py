from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item, Category
from .forms import AddItemForm, EditItemForm
from conversation.forms import MessageForm
from conversation.models import Conversation


# Create your views here.


def details(request, id):
    product = get_object_or_404(Item, pk=id)
    conversation = Conversation.objects.filter(item=product).first()
    related_items = Item.objects.filter(category=product.category, is_sold=False).exclude(pk=id)[:3]
    message_form = MessageForm()
    return render(request, 'core/details.html',
                  {'product': product, 'related_items': related_items, 'message_form': message_form, 'conversation': conversation})


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            form.save()
            messages.success(request, 'Item was successfully created')
            return redirect('item:details', item.id)
    else:
        form = AddItemForm()
    return render(request, 'item/create.html', {'form': form})


@login_required(login_url='login')
def delete(request):
    if request.method == 'POST':
        product = get_object_or_404(Item, pk=request.POST['id'])
        if product.created_by.id == request.user.id:
            product.delete()
            messages.success(request, 'Item was successfully deleted')
            return redirect('dashboard:index')
        else:
            return render(request, 'errors/../templates/403.html')
    else:
        return redirect('dashboard:index')


@login_required(login_url='login')
def edit(request, id):
    product = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item was successfully edited')
            return redirect('dashboard:index')
    else:
        form = EditItemForm(instance=product)

    return render(request, 'item/update.html', {'form': form, 'product': product})
