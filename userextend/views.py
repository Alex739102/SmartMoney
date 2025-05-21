import random
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.views.generic import CreateView

from Smart_Money.settings import DEFAULT_FROM_EMAIL
from userextend.forms import AuthenticationNewForm, UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class= UserForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.upper()
            new_user.last_name = new_user.last_name.upper()
            random_sixnumber = random.randint(100000, 999999)
            new_user.username = f'{new_user.first_name.lower()[0]}{new_user.last_name.lower()}_{random_sixnumber}'
            new_user.save()

            subject = 'Cont nou in aplicatie'
            mesaj = (f"Buna seara, {new_user.first_name}, {new_user.last_name}\n\n"
                     f"Bine ai venit in aplicatia noastra! Pentru autentificare ai nevoie de username-ul: {new_user.username}")

            send_mail(subject, mesaj, DEFAULT_FROM_EMAIL, [new_user.email])

        return super(UserCreateView,self).form_valid(form)




class UserLoginView(LoginView):
    template_name = 'registrations/login.html'
    authentication_form = AuthenticationNewForm