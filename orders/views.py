from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DesignOrderForm
from .models import DesignOrder


@login_required
def create_order(request):
    if request.method == 'POST':
        form = DesignOrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
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