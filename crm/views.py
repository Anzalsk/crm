from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.db.models import Sum
from .filters import SaleFilter


@login_required
def home(request):
    if request.user.is_superuser:
        target = Profile.objects.aggregate(Sum('target'))
        target = target['target__sum']
    else: 
        profile = get_object_or_404(Profile, user=request.user)
        target = profile.target

    today = datetime.date.today()
    if request.user.is_superuser:
        month_target_completed = Sale.objects.filter(date_created__year=today.year, date_created__month=today.month).aggregate(Sum('total_amount'))
    else:
        month_target_completed = Sale.objects.filter(owner=request.user, date_created__year=today.year, date_created__month=today.month).aggregate(Sum('total_amount'))
    
    if request.user.is_superuser:
        sale = Sale.objects.all()[0:5]
    else:
        sale = Sale.objects.filter(owner=request.user)[0:5]   # fetching recents 5 sales.
    
    if request.user.is_superuser:
        customer = Customer.objects.all()
    else:
        customer = Customer.objects.filter(owner=request.user)
    total_customers = customer.count() 
  
    context = {
        "sale":sale,
        "customer":customer,
        "total_customers":total_customers,
        "month_target_completed":month_target_completed,
        "target":target,
    }
    print(target)
    return render(request, "crm/home.html", context)




def customer(request):
    if request.user.is_superuser:
        customers = Customer.objects.all()
    else:
        customers = Customer.objects.filter(owner=request.user) # Only fetch those customers whose owner is current user.
    context = {
        "customers":customers,
    }
    return render(request, "crm/customer.html", context)

def all_sales(request):  
    if request.user.is_superuser:
        all_sale = Sale.objects.all()
        myfilter = SaleFilter(request.GET, queryset=all_sale)
        all_sale = myfilter.qs
    else:
        all_sale = Sale.objects.filter(owner=request.user)
        myfilter = SaleFilter(request.GET, queryset=all_sale)
        all_sale = myfilter.qs

    context = {
        "all_sale":all_sale,
        "myfilter":myfilter
    }
    return render(request, "crm/all_sales.html", context)

def sales(request, pk):
    user_id = Customer.objects.get(id=pk)
    form = SaleCreateForm()
    if request.method == 'POST':
        form = SaleCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = user_id
            instance.owner = request.user  #Assigning Owner to the customer
            instance.save()
            return redirect(reverse("crm-detail", kwargs={"pk":user_id.id}))

    context = {
       "form":form,
    }
    return render(request, "crm/sales.html", context)




def update_sales(request, pk):
    purchase = Sale.objects.get(id=pk) # Getting sale id
    form = SaleUpdateForm(instance=purchase)
    customer = purchase.customer # Getting the customer of this sale
    if request.method == 'POST':
        form = SaleUpdateForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect(reverse("crm-detail", kwargs={"pk":customer.id}))
    context = {

        "form":form
    }
    return render(request, "crm/update.html", context)




def delete_sale(request, pk):
    purchase = Sale.objects.get(id=pk)
    if request.method == 'POST':
        customer = purchase.customer
        purchase.delete()
        return redirect(reverse("crm-detail", kwargs={"pk":customer.id}))
    context = {
        "item":purchase
    }
    return render(request, "crm/delete_sale.html", context)




def detail(request, pk):
    customer = Customer.objects.get(id=pk) # Getting customer id
    customer_sale = customer.sale_set.all() # Getting all sales of that customer
    context = {
        "customer":customer, #tets
        "customer_sale":customer_sale
    }
    return render(request, "crm/detail.html", context)




def products(request):
    context = {
        "products":products
    }
    return render(request, "crm/products.html", context)




def create_customer(request):
    form = CustomerCraeteForm()
    if request.method == 'POST':
        form = CustomerCraeteForm(request.POST)
        if form.is_valid():
            instane = form.save(commit=False)
            instane.owner = request.user #Assigning owner to the new customer
            instane.save()
            return redirect('crm-customer')
    context = {
        "form":form
    }
    return render(request, "crm/sales.html", context)




def update_customer(request, pk):
    customer_id = Customer.objects.get(id=pk)
    form = UpdateCustomerForm(instance=customer_id)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer_id)
        if form.is_valid():
            form.save()
            return redirect(reverse("crm-detail", kwargs={"pk":customer_id.id}))
    context = {

        "form":form
    }
    return render(request, "crm/update.html", context)




def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('crm-customer')
    context = {
        "item":customer
    }
    return render(request, "crm/delete_customer.html", context)




def admin(request):
    if request.user.is_superuser:

        users = User.objects.filter(is_superuser=False).order_by("-id")
        context = {
            "users":users
        }
        return render(request, "crm/admin.html", context)
    else:
        return redirect("/")




def user_register(request):
    form = CraeteUserForm()
    if request.method == 'POST':
        form = CraeteUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.is_staff=True
            instance.save() 
            return redirect('crm-myadmin')    
    context = {
        "form": form
        }
    return render(request, "crm/user_register.html", context)




def update_user(request, pk):
    user_id = User.objects.get(id=pk)
    form = UserUpdateForm(instance=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user_id)
        if form.is_valid():
            form.save()
            return redirect(reverse("crm-profile", kwargs={"pk":user_id.id}))
    context = {
        "form":form
    }
    return render(request,"crm/update.html", context)




def delete_user(request, pk):
    user_id = User.objects.get(id=pk)
    if request.method == 'POST':
        user_id.delete()
        return redirect("crm-myadmin")
    context = {
        "item":user_id
    }
    return render(request, "crm/delete_user.html", context)




def profile(request, pk):
    user = User.objects.get(id=pk)
    context = {
        "user":user
    }
    return render(request, "crm/profile.html", context)




def targetform(request, pk):
    user_id = User.objects.get(id=pk)
    form = TargetForm(instance=user_id)
    if request.method == 'POST':
        form = TargetForm(request.POST, instance=user_id)
        if form.is_valid():
            form.save()
            return redirect(reverse("crm-profile", kwargs={"pk":user_id.id}))
    context = {
        "form":form,
    }

    return render(request, "crm/target.html", context) 




def update_target(request, pk):
    profile = Profile.objects.get(user__id=pk)
    user_id = profile.user
    form = TargetForm(instance=profile)
    if request.method == 'POST':
        form = TargetForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(reverse("crm-profile", kwargs={"pk":user_id.id}))
    context = {
        "form":form
    }
    return render(request, "crm/target.html", context)
    