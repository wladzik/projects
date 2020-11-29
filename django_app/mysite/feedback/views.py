import os
import time
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import User, Feedback
from django.http import HttpResponse


def feedback_form(request):
    # feedback_area = Feedback.objects.order_by('-feedback_date')
    render(request, 'feedback.html')
    actual_stamp = time.strftime('%Y-%m-%d %H:%M:%S.000000')
    n = User.objects.get(id=1)
    n.feedback_set.create(feedback_date=request.POST.get(actual_stamp), opinion=request.POST.get("text_f"))

    return HttpResponseRedirect(reverse(successfully_saved(request)))


def successfully_saved(request):
    return HttpResponse("Successful")
