from django.http import HttpResponse

from tiger.look.models import Skin

def render_skin(request, skin_id, timestamp):
    skin = Skin.objects.get(id=skin_id)
    css_file = open(skin.path)
    return HttpResponse(css_file.read())

