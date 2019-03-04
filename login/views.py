from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms

import UserCreationForm
from registration

django.core.context_processors
import csrf

__author__ = 'Nyasuguta'

 def
 register(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/accounts/register/complete')

     else:
         form = UserCreationForm()
     token = {}
     token.update(csrf(request))
     token['form'] = form

     return render_to_response('registration/registration_form.html', token)

 def registration_complete(request):
     return render_to_response('registration/registration_complete.html')

