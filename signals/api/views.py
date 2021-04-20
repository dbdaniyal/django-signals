from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from api.models import Post

# custom signal
request_counter_signal = Signal(providing_args=['timestamp'])



def home(request):
	request_counter_signal.send(sender=Post,timestamp='2021-04-04')
	return HttpResponse("here's the response")

@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("Request finished!")


@receiver(request_counter_signal)
def post_counter_signal(sender, **kwargs):
    print(kwargs)



