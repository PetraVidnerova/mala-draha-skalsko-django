def force_default_language_middleware(get_response):

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
        
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware            
