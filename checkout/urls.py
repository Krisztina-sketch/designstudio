from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path(
        'create-checkout-session/<int:order_id>/',
        views.create_checkout_session,
        name='create_checkout_session'
    ),
    path(
        'success/<int:order_id>/',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'cancel/',
        views.checkout_cancel,
        name='checkout_cancel'
    ),
]
