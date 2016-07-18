from django.shortcuts import render,redirect
from django.template import loader
from Meniu.models import Menu
from Order.models import Order
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import MenuForm
from django.contrib import messages
import datetime 



# method used to add a menu
def get_name(request):  
    if request.method == 'POST':
        # create a Menu form instance and populate it with data from the request:
        form = MenuForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            #saving the created object 
            form.save()
            #saves a message
            messages.success(request, 'Element added.')
            # redirect to a new URL:
            return redirect('meniu:view-menu')  
        else:
            messages.error(request, 'Data is invalid.')
    # if a GET (or any other method) we'll create a blank form
    else:

        form = MenuForm()
    #
    return render(request, 'Meniu/newMenu.html', {'form': form})

# method used to return all the avaible menus
def view_menu(request):
    menus = Menu.objects.all().order_by('datta')
    return render(request, 'Meniu/availableMenus.html', {'menu': menus})

# method used to return the avaible menus for today 
def view_daily_menus(request):
    today = datetime.date.today()
    menus = Menu.objects.all().filter(datta = today) 
    return render(request, 'Meniu/dailyMenus.html', {'menu': menus})

# method used to return the menu and the average raiting, orders for it.
def getOrders(request,pk):
    orders = Order.objects.filter(id_menu__pk=pk)
    meniu = Menu.objects.get(pk=pk)
    nrOrders = len(orders)
    if nrOrders>0:
        sumRating=0
        for i in  orders:
            sumRating += i.rating
        averageRating = sumRating/nrOrders
    else:
        averageRating=0
    return render(request, 'Meniu/ordersByMenu.html', {'n':meniu ,'o':averageRating, 'orders': orders})










