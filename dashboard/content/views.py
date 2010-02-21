from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template

from tiger.content.forms import *
from tiger.content.models import *

from tiger.utils.views import add_edit_site_object, delete_site_object

@login_required
def home(request):
    return direct_to_template(request, template='dashboard/content.html', extra_context={
        'pdfs': PdfMenu.objects.all()
    })

@login_required
def add_edit_pdf(request, pdf_id=None):
    return add_edit_site_object(request, PdfMenu, PdfMenuForm, 
        'dashboard/pdf_form.html', 'dashboard_content', object_id=pdf_id)

@login_required
def delete_pdf(request, pdf_id):
    return delete_site_object(request, PdfMenu, pdf_id, 'dashboard_content')

@login_required
def preview_pdf(request, pdf_id):
    pdf = PdfMenu.objects.get(id=pdf_id)
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'filename=menu-preview.pdf'
    response.write(pdf.render())
    return response

@login_required
def feature_pdf(request, pdf_id):
    pdf = PdfMenu.objects.get(id=pdf_id)
    pdf.featured = True
    pdf.save()
    PdfMenu.objects.exclude(id=pdf_id).update(featured=False)
    messages.success(request, '"%s" has been added to your home page.' % pdf.name)
    return HttpResponseRedirect(reverse('dashboard_content'))