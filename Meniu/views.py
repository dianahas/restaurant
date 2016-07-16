from django.shortcuts import render,redirect
from django.template import loader
from Meniu.models import Menu
from Order.models import Order
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import MenuForm
from django.contrib import messages
import datetime 



# Create your views here.

def get_name(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MenuForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            messages.success(request, 'Element added.')
            return redirect('view-menu')
        else:
            messages.error(request, 'Data is invalid.')
    # if a GET (or any other method) we'll create a blank form
    else:

        form = MenuForm()

    return render(request, 'Meniu/newMenu.html', {'form': form})

def view_menu(request):
    menus = Menu.objects.all().order_by('datta')
    return render(request, 'Meniu/availableMenus.html', {'menu': menus})

def view_daily_menus(request):
    today = datetime.date.today()
    menus = Menu.objects.all().filter(datta = today) 
    return render(request, 'Meniu/dailyMenus.html', {'menu': menus})

def getOrders(request,pk):
    #import ipdb; ipdb.set_trace()
    orders = Order.objects.filter(id_menu__pk=pk)
    sumRating=0
    for i in  orders:
        sumRating += i.rating
    nrOrders = len(orders)
    averageRating = sumRating/nrOrders
    meniu = Menu.objects.get(pk=pk)
    return render(request, 'Meniu/ordersByMenu.html', {'n':meniu ,'o':averageRating, 'orders': orders})










