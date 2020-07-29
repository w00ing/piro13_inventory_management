from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Account
from products.models import Product


def accounts_list(request):
    queryset = Account.objects.all()
    context = {
        "accounts": queryset,
    }
    return render(request, "accounts/home.html", context=context)


def account_register(request):
    # GET
    if request.method == "GET":
        return render(request, "accounts/register.html", context={})

    # POST
    name = request.POST["name"]
    phone_number = request.POST["phone_number"]
    address = request.POST["address"]
    # account = request.POST["account"]

    account = Account.objects.create(
        name=name,
        phone_number=phone_number,
        address=address,
        # account=account,
    )

    pk = account.id
    url = reverse("accounts:account_details", kwargs={"pk": pk})
    return redirect(to=url)


def account_details(request, pk):
    account = Account.objects.get(id=pk)
    products = Product.objects.filter(account=account)

    context = {
        "account": account,
        "products": products,
    }

    return render(request, "accounts/details.html", context=context)


def account_update(request, pk):
    account = Account.objects.get(id=pk)

    # GET
    if request.method == "GET":
        context = {
            "account": account,
        }
        return render(request, "accounts/update.html", context=context)

    # POST
    name = request.POST["name"]
    phone_number = request.POST["phone_number"]
    address = request.POST["address"]
    # account = request.POST["account"]

    account.name = name
    account.phone_number = phone_number
    account.address = address
    # account.account = account

    account.save()

    url = reverse("accounts:account_details", kwargs={"pk": pk})
    return redirect(to=url)


def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()

    url = reverse("accounts:accounts_list")
    return redirect(to=url)
