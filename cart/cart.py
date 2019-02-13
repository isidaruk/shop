from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    """
    Initialize the cart.
    """

    # Store the current session.
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
        # save an empty cart in session
        cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart
