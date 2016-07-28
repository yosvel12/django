from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from plataforma.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from plataforma.forms import MyRegistrationForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect


def login_page(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Se ha loggeado de correctamente"
                    return redirect('apps')
                else:
                    message = "Su usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto. Por favor vuelva a intentarlo"
    else:
        form = LoginForm()
    return render_to_response('stormboard/users/login.html', {'message': message, 'form': form},
                              context_instance=RequestContext(request))


def homepage(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


@csrf_protect
def register(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        else:
            args['form'] = form
    else:
        args['form'] = MyRegistrationForm()

    return render_to_response('stormboard/users/register.html', context_instance=RequestContext(request))


def apps(request):
    return render_to_response('apps.html', context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('homepage')


def forgot(request):
    return render_to_response('stormboard/users/forgot.html', context_instance=RequestContext(request))
