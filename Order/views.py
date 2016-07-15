from django.shortcuts import render,redirect
from django.template import loader
from Order.models import Order
from Meniu.models import Menu
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import OrderForm
from django.contrib import messages

# Create your views here.
def get_order(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            messages.success(request, 'Element added.')
            # return redirect('view-menu')
        else:
            messages.error(request, 'Data is invalid.')
    # if a GET (or any other method) we'll create a blank form
    else:

        form = OrderForm()

    return render(request, 'Order/newOrder.html', {'form': form})

def updateStatus(request,pk):
    # import ipdb; ipdb.set_trace()
    selectedOrder = Order.objects.get(id=pk)
    selectedOrder.status = 1
    idMeniu = selectedOrder.id_menu.pk
    meniu = Menu.objects.get(pk=idMeniu)
    selectedOrder.save()
    orders = Order.objects.filter(id_menu__pk=idMeniu)
    return render(request, 'Meniu/ordersByMenu.html', {'n':meniu ,'orders': orders})
