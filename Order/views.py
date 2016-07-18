from django.shortcuts import render,redirect
from django.template import loader
from Order.models import Order
from Meniu.models import Menu
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from restaurant.utils import *

#views for order
#method used to get an order
def get_order(request, pk):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = newOrderForm(request.POST, id_menu=pk)
        if form.is_valid():
            form.save()
            #create the details of email
            subject = "Order confirmation Restaurant Archers"
            mail = form.data["email"]
            menu_code = str(form.data["id_menu"]) + "-"
            orderr = Order.objects.last()
            menu_code += str(orderr.pk)
            send_mail(subject, menu_code, "restaurantarchers@gmail.com", [mail])
            messages.success(request, 'Element added.')
            #redirect to the list of menus
            return redirect('meniu:view-daily')
        else:
            messages.error(request, 'Data is invalid.')
    # create a form
    else:
        form = newOrderForm(id_menu=pk)

    return render(request, 'Order/newOrder.html', {'form': form})

#method used to get an order
def updateStatus(request,pk):
    selectedOrder = Order.objects.get(id=pk)
    selectedOrder.status = 1
    idMeniu = selectedOrder.id_menu.pk
    meniu = Menu.objects.get(pk=idMeniu)
    selectedOrder.save()
    orders = Order.objects.filter(id_menu__pk=idMeniu)
    return render(request, 'Meniu/ordersByMenu.html', {'n':meniu ,'orders': orders})

#method used to get a code and if it is valid, it returns the details of the order
def get_code(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = codeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            code = form.data['code']
            tup = validateCode(code)
            meniu = Menu.objects.get(pk=tup[0])
            comanda = Order.objects.get(pk=tup[1])
            return render(request, 'Order/orderStatus.html', {'m':meniu ,'c': comanda})

    else:
        form = codeForm()
    return render(request, 'Order/verifyCode.html', {'form': form})
    
#returns tje details of the order
def checkCode(request):
    import ipdb; ipdb.set_trace()
    data = request.POST
    try:
        receivedData = data["code"]
    except:
        pass
    tup = validateCode(receivedData)
    meniu = Menu.objects.get(pk=tup[0])
    comanda = Order.objects.get(pk=tup[1])
    return render(request, 'Order/orderStatus.html', {'m':meniu ,'c': comanda})