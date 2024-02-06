from django.shortcuts import render, redirect
from django.contrib import messages


from contact.forms import RegiterForm


def register(request):
    form = RegiterForm()

    if request.method == 'POST':
        form = RegiterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
          'form': form,
        }
    )
