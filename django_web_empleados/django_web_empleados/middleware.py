from django.shortcuts import redirect

class VerificarUsuarioMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si el usuario ha iniciado sesión
        if not request.user.is_authenticated:
            # Verificar si el usuario está en la página de inicio de sesión o en la página de inicio
            if not request.path.startswith('/login/') and not request.path == '/':
                # Si el usuario no ha iniciado sesión y no está en la página de inicio de sesión, redirigirlo a la
                # página de inicio de sesión
                return redirect('login')

        response = self.get_response(request)

        return response
