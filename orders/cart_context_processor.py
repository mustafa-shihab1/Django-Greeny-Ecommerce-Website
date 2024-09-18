from .models import CartOrder, CartDetail

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = CartOrder.objects.get_or_create(user=request.user, order_status='Inprogress')
        cart_details = CartDetail.objects.filter(order=cart.id)
        return {'cart':cart, 'cart_details':cart_details }