# views.py
from django.conf import settings
import stripe

from rest_framework.response import Response
from rest_framework.views import APIView


stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        # retrieve the token from the request body
        token = request.data.get("stripeToken")
        # create a new customer
        customer = stripe.Customer.create(
            email=request.user.email,
            source=token
        )
        # charge the customer
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            customer=customer.id
        )
        # return a success response
        return Response({"status": "success"})

