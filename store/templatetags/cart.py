from django import template
#decorator filter
register = template.Library()

#product cart e ace ki na?
@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True 
            
    return False

#add to cart quantity
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
            
    return 0