from django import template
#decorator filter used
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

#cart product price
@register.filter(name='total_price')
def total_price(product,cart):
    return product.price * cart_quantity(product,cart)

#Total Cart Price Sum
@register.filter(name='cart_total_price')
def cart_total_price(products,cart):
    sum = 0
    for p in products:
        sum += total_price(p,cart)
    return sum