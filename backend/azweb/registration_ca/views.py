
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm
#from django.contrib import messages
from .models import Extendeduser
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def Registration(request):

        return render(request, 'ca_portal/ca.html')

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'ca_portal/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if Extendeduser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })



            else:
                # print('hellow world')
                # Create the user:

                # user = User.objects.create_user(
                #     # form.cleaned_data['username'],
                #     form.cleaned_data['email']

                # )

                extendeduser = Extendeduser()
                extendeduser.first_name = form.cleaned_data['first_name']
                extendeduser.last_name = form.cleaned_data['last_name']
                extendeduser.phone_number = form.cleaned_data['phone_number']
                extendeduser.alternate_phone_number = form.cleaned_data['alternate_phone_number']
                extendeduser.college = form.cleaned_data['college']
                extendeduser.current_year = form.cleaned_data['current_year']
                extendeduser.permanent_address = form.cleaned_data['permanent_address']
                extendeduser.state = form.cleaned_data['state']
                extendeduser.email = form.cleaned_data['email']
                extendeduser.pincode = form.cleaned_data['pincode']
                # extendeduser.user = user
                extendeduser.save()

                subject = "Successfully registered for AZeotropy Campus Ambassador "
                # message = f'congratulations {extendeduser.first_name}{extendeduser.last_name} have successfully registered on CA portal'
                to_email = extendeduser.email

                name1 = str(extendeduser.first_name).title()
                html_message = render_to_string("ca_portal/mail.html",{'name':name1})
                message = strip_tags(html_message)

                email3 = EmailMultiAlternatives(subject,
                            message,
                            'azeo2022@gmail.com',
                            [to_email],
                            )
                email3.attach_alternative(html_message,'text/html')
                email3.send()

                # send_mail(
                #             subject,
                #             message,
                #             from_email,
                #             [to_email],
                #             fail_silently=False,
                #         )
                extendeduser.save()
                message = 'You have successfully registered on CA portal'
                return render(request, "ca_portal/ca.html",{'message':message})




                # redirect to home page:
                #return redirect('registration_ca:index')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})








