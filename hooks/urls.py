from django.urls import path

from . import views

urlpatterns = [
    path('stripe', views.stripe_webhook, name='stripe_webhook'),
    path('test', views.test, name='test'),
]