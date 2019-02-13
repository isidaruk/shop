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
        # Save an empty cart in session.
        cart = self.session[settings.CART_SESSION_ID] = {}
    self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """

        # Convert into a string in order to serialize it.
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Mark the session as "modified" to make sure it gets saved.
        self.session.modiffied = True
