import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template

from tiger.look.forms import *
from tiger.look.models import Skin

@login_required
def picker(request):
    request.session['customizing'] = True
    return HttpResponseRedirect('/')

@login_required
def get_font_css(request):
    font = FontFace.objects.get(id=request.POST.get('font'))
    return HttpResponse(font.as_css())

@login_required
def get_body_font_css(request):
    form = BodyFontForm(request.POST)
    form.full_clean()
    return HttpResponse(form.cleaned_data['body_font'])

@login_required
def get_bg_css(request):
    bg = Background.objects.get(id=request.POST.get('bg'))
    return HttpResponse(bg.as_css())

@login_required
def get_custom_bg_css(request):
    form = CustomBackgroundForm(request.POST, instance=request.site.background)
    form.full_clean()
    bg = form.save(commit=False)
    if bg.staged_image:
        css = bg.as_css(staged=True)
    else:
        css = bg.as_css()
    return HttpResponse(css)

@login_required
def set_img(request):
    form = BackgroundImageForm(request.POST, request.FILES, instance=request.site.background)
    form.full_clean()
    bg = form.save()
    data = {
        'selector': '#background',
        'css': 'body { %s }' % bg.as_css(staged=True)
    }
    return HttpResponse(json.dumps(data))

@login_required
def select_skin(request):
    skin_id = request.POST.get('id')
    skin = Skin.objects.get(id=skin_id)
    site = request.site
    site.skin = skin
    site.save()
    return HttpResponse("Your settings have been saved.")

@login_required
def save(request):
    skin = request.site.skin
    font_form = HeaderFontForm(request.POST, instance=skin)
    body_font_form = BodyFontForm(request.POST, instance=skin)
    color_form = ColorForm(request.POST, instance=skin)
    forms = (font_form, body_font_form, color_form,)
    [f.full_clean() for f in forms]
    for form in forms:
        instance = form.save(commit=False)
        instance.save(bundle=False)
    skin.css = request.POST.get('css', '')
    background = skin.background
    bg_id = request.POST.get('bg')
    if bg_id:
        background.clone(Background.objects.get(id=bg_id))
    else:
        if background.staged_image:
            background.image.save(background.staged_image.name.split('/')[-1], background.staged_image.file)
    if background.staged_image:
        background.staged_image.delete()
    skin.save()
    return HttpResponse(skin.url)
