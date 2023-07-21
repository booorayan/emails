from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import SubscribeForm
from .tasks import send_notification_mail


# Create your views here.
class IndexView(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        mail = form.cleaned_data['mail']
        message = form.cleaned_data['message']

        send_notification_mail.delay(mail, message)
        return HttpResponse('We sent you a confirmation email!')
