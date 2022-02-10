from django.shortcuts import render, redirect

from e_shop_contact.forms import CreateContactForm

from e_shop_contact.models import ContactUs

from e_shop_settings.models import SiteSettings

# Create your views here.


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        contact_form = CreateContactForm()
        return redirect('/contact_us_done')
    site_settings = SiteSettings.objects.first()
    context = {
        'contact_form': contact_form,
        'settings': site_settings,
        'title': 'تماس با ما',

    }
    return render(request, 'contact_us/contact_us_page.html', context)


def contact_us_done(request):
    return render(request, 'contact_us/contact_us_done.html', {'title': 'ثبت موفقيت آميز پيام شما '})
