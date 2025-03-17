from .models import Menu

def menus_context(request):
    menus = Menu.objects.prefetch_related('submenu_set').all()

    for menu in menus:
        submenus = list(menu.submenu_set.all())
        with_number = sorted([s for s in submenus if s.number is not None], key=lambda x: x.number)
        without_number = [s for s in submenus if s.number is None]

        sorted_submenus = with_number + without_number

        for submenu in submenus:
            if submenu.title == "Korrupsiyaga qarshi kurashish":
                submenu.extra_submenu = [
                    {"url": "/international/corruption/law/", "title": "Korrupsiyaga qarshi kurashish"},
                    {"url": "/international/corruption/event/", "title": "O‘tkazilayotgan tadbirlar"},
                ]

        # Yangilangan submenu ro‘yhatini menyuga qo‘shamiz
        menu.sorted_submenus = sorted_submenus  # Template uchun

    return {'menus': menus}
