import random
from datetime import datetime
from django.views.generic import CreateView
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from manage_users.forms import UserForm
from manage_users.models import History
from django.contrib.auth.decorators import permission_required


@permission_required('user.add_user')
def perm_add_user(request):
    message = "You have access to this view because you have permission 'user.add_user'"
    return render(request, 'navbar.html', {'message': message})


class UserCreateView(CreateView):
    template_name = 'manage_users/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()

            new_user.username = (f'{new_user.first_name[0].lower()}'
                                 f'{new_user.last_name.lower().replace(" ", "")}'
                                 f'_{random.randint(100000, 999999)}')
            new_user.save()

            subject = 'New account'
            message = f'Congratulation! Your username is: {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, recipient_list=[new_user.email])

            history_text = f'{new_user.first_name} {new_user.last_name} was successfully created on {datetime.now()}'
            History.objects.create(text=history_text, create_at=datetime.now())

        return redirect('login')
