from django.shortcuts import redirect, render, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("first_name")
    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'contacts': page_obj,
        'site_title': 'contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context,
    )


def search(request):
    search_values = request.GET.get('q', '').strip()

    if search_values == '':
        return redirect("contact:index")

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_values) |
            Q(last_name__icontains=search_values) |
            Q(phone__icontains=search_values) |
            Q(id__icontains=search_values) |
            Q(email__icontains=search_values)
            )\
        .order_by("first_name")

    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts': page_obj,
        'site_title': 'contatos - ',
        'search_values': search_values,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )


def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True
    )

    contact_title = f'{single_contact.first_name} \
        {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': contact_title
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
