from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Product
from accounts.models import Account


def products_list(request):
    queryset = Product.objects.all()
    context = {
        "products": queryset,
    }
    return render(request, "products/home.html", context=context)


@require_POST
def amount_ajax(request):
    pk = request.POST.get("pk")
    status = request.POST.get("status")
    product = get_object_or_404(Product, pk=pk)

    if status == "plus":
        product.amount += 1
    else:
        if product.amount > 0:
            product.amount -= 1
        else:
            redirect("products_list")

    product.save()
    ctx = {
        "amount": product.amount,
    }
    return JsonResponse(ctx)


def product_register(request):
    queryset = Account.objects.all()
    context = {
        "accounts": queryset,
    }

    # GET
    if request.method == "GET":
        return render(request, "products/register.html", context=context)

    # POST
    title = request.POST["title"]
    image = request.FILES["image"]
    content = request.POST["content"]
    price = request.POST["price"]
    amount = request.POST["amount"]
    account = Account.objects.get(id=request.POST["account"])

    product = Product.objects.create(
        title=title,
        image=image,
        content=content,
        price=price,
        amount=amount,
        account=account,
    )
    print(product.image)

    pk = product.id
    url = reverse("products:product_details", kwargs={"pk": pk})
    return redirect(to=url)


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    account = Account.objects.get(id=product.account.pk)

    context = {
        "product": product,
        "account": account,
    }

    return render(request, "products/details.html", context=context)


def product_update(request, pk):
    product = Product.objects.get(id=pk)
    accounts = Account.objects.all()
    # GET
    if request.method == "GET":
        context = {
            "product": product,
            "accounts": accounts,
        }
        return render(request, "products/update.html", context=context)

    # POST
    title = request.POST["title"]
    try:
        image = request.FILES["image"]
    except:
        image = product.image
    content = request.POST["content"]
    price = request.POST["price"]
    amount = request.POST["amount"]
    account = Account.objects.get(id=request.POST["account"])
    print(account.name)

    product.title = title
    product.image = image
    product.content = content
    product.price = price
    product.amount = amount
    product.account = account

    product.save()

    url = reverse("products:product_details", kwargs={"pk": pk})
    return redirect(to=url)


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    url = reverse("products:products_list")
    return redirect(to=url)
