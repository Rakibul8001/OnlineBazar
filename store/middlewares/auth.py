
from django.shortcuts import redirect
#middleware built-in
def auth_middleware(get_response):

    def middleware(request):
        #checking customer login or not for view orders
        returnUrl = request.META['PATH_INFO'] #kon page theke kon page url
        if not request.session.get('customer_id'):
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)

        return response

    return middleware