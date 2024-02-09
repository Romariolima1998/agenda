from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


from contact.forms import RegiterForm, RegisterUpdateForm


def register(request):
    form = RegiterForm()

    if request.method == 'POST':
        form = RegiterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'usuário registrado')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
          'form': form,
        }
    )


def user_update(request):

    if request.user.is_authenticated:
        form = RegisterUpdateForm(instance=request.user)

        if request.method == 'POST':
            form = RegisterUpdateForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'usuario atualizado com sucesso')
                return redirect('contact:user_update')

        return render(
            request,
            'contact/user_update.html',
            {
                'form': form,
            }
        )
    return redirect('contact:login')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')
        else:
            messages.error(request, 'login invalido')

    return render(
        request,
        'contact/login.html',
        {
          'form': form,
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
