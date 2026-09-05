import stripe

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from orders.models import DesignOrder


@login_required
def create_checkout_session(request, order_id):
    order = get_object_or_404(
        DesignOrder,
        id=order_id,
        user=request.user
    )

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': order.title,
                    },
                    'unit_amount': int(order.service.base_price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            f'/checkout/success/{order.id}/'
        ),
        cancel_url=request.build_absolute_uri(
            '/checkout/cancel/'
        ),
    )

    return redirect(checkout_session.url, code=303)


@login_required
def checkout_success(request, order_id):
    order = get_object_or_404(
        DesignOrder,
        id=order_id,
        user=request.user
    )

    order.price = order.service.base_price
    order.paid = True
    order.save()

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


@login_required
def checkout_cancel(request):
    return render(request, 'checkout/checkout_cancel.html')
