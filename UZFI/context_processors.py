from .models import Menu, CentersDepartments

def menus_context(request):

    menus = Menu.objects.prefetch_related('submenu_set').all()
    for menu in menus:
        for submenu in menu.submenu_set.all():
            if submenu.title == "Korrupsiyaga qarshi kurashish":
                submenu.extra_submenu = [
                    {"url": "/international/corruption/law/", "title": ("Korrupsiyaga qarshi kurashish")},
                    {"url": "/international/corruption/event/", "title": ("O'tkazilayotgan tadbirlar")},
                ]
                
    return {'menus': menus}