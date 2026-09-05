from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DesignOrderForm
from .models import DesignOrder


@login_required
def create_order(request):
    if request.method == 'POST':
        form = DesignOrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.price = order.service.base_price
            order.save()
            return redirect('order_success')
    else:
        form = DesignOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'orders/create_order.html', context)


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')


@login_required
def my_orders(request):
    orders = DesignOrder.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'orders': orders,
    }

    return render(request, 'orders/my_orders.html', context)


@login_required
def edit_order(request, order_id):
    order = get_object_or_404(
        DesignOrder,
        id=order_id,
        user=request.user
    )

    if request.method == 'POST':
        form = DesignOrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('my_orders')
    else:
        form = DesignOrderForm(instance=order)

    context = {
        'form': form,
        'order': order,
    }

    return render(request, 'orders/edit_order.html', context)


@login_required
def delete_order(request, order_id):
    order = get_object_or_404(
        DesignOrder,
        id=order_id,
        user=request.user
    )

    if request.method == 'POST':
        order.delete()
        return redirect('my_orders')

    context = {
        'order': order,
    }

    return render(request, 'orders/delete_order.html', context)


@login_required
def order_delivery(request, order_id):
    order = get_object_or_404(
        DesignOrder,
        id=order_id,
        user=request.user,
        paid=True
    )

    context = {
        'order': order,
    }

    return render(request, 'orders/order_delivery.html', context)
