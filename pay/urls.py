# urls.py
from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('payments/', PaymentView.as_view(), name='payments'),
]