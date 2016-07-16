from django.shortcuts import render,redirect
from django.template import loader
from Order.models import Order
from Meniu.models import Menu
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib import messages
from restaurant.utils import *

# Create your views here.
def get_order(request, pk):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = newOrderForm(request.POST, id_menu=pk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Element added.')
            return redirect('view-daily')
        else:
            messages.error(request, 'Data is invalid.')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = newOrderForm(id_menu=pk)

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

def get_code(request):
    # if this is a POST request we need to process the form data
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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = codeForm()
    return render(request, 'Order/verifyCode.html', {'form': form})

def checkCode(request):
    import ipdb; ipdb.set_trace()
    data = request.POST
    try:
        receivedData = data["code"]
    except:
        pass
    # if validateCode(receivedData) == False:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    tup = validateCode(receivedData)
    meniu = Menu.objects.get(pk=tup[0])
    comanda = Order.objects.get(pk=tup[1])
    return render(request, 'Order/orderStatus.html', {'m':meniu ,'c': comanda})