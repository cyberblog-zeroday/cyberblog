# cyberblog/middleware.py
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si el modo mantenimiento está activado
        if getattr(settings, 'MAINTENANCE_MODE', False):
            # Excluir el panel de administración (opcional)
            if not request.path.startswith('/admin/'):
                return HttpResponse(
                    render_to_string('maintenance.html'),
                    status=503  # Código HTTP para mantenimiento
                )
        return self.get_response(request)
    

