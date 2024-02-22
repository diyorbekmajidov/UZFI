from .models import Abitur


def logo_context(request):
    logo = Abitur.objects.all()
    return {'abt': logo}