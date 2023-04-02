from django.shortcuts import redirect

class VerificarUsuarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si el usuario ha iniciado sesión
        if not request.user.is_authenticated:
            # Si el usuario no ha iniciado sesión, redirigirlo a la página de inicio de sesión
            return redirect('login')

        response = self.get_response(request)

        return response
