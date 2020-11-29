from django import template
#decorator filter used
register = template.Library()

# Jo mon chahe currency ko add karo.... Tk,$,₹ etc....
@register.filter(name='currency')
def currency(num):
    return "$"+str(num)

#Order list
@register.filter(name='multiply')
def multiply(num,num1):
    return num*num1