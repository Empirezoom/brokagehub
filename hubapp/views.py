from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *




from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import RegistrationForm



from django.http import JsonResponse


# Create your views here.


def homepage(request):
    serv = Services.objects.all()
    chosen = ChooseUs.objects.all()
    test= Testimonial.objects.all()
    
    context = {
        'serv': serv,
        'chosen': chosen,
        'test': test,
    }

    return render(request,'index.html',context)







# @csrf_protect
# def registration_form(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             registration = form.save()
#             messages.success(
#                 request, 
#                 f' ID is: {registration.reference_id}'
#             )
#             return redirect('success')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = RegistrationForm()
    
#     return render(request, 'form.html', {'form': form})

# def success_view(request):
#     return render(request, 'success.html')


@csrf_protect
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save()
            messages.success(
                request, 
                f'Congratulation! Your reference ID is: {registration.reference_id}'
            )
            return redirect('success')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.replace('_', ' ').title()}: {error}")
    else:
        form = RegistrationForm()
    
    return render(request, 'form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

# AJAX views for real-time validation
def check_email(request):
    email = request.GET.get('email')
    if email:
        exists = Registration.objects.filter(email=email).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

def check_phone(request):
    phone = request.GET.get('phone')
    if phone:
        exists = Registration.objects.filter(phone=phone).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})







def activity_admin_tay(request):

    reg = Registration.objects.all()
    acc = Registration.objects.filter(accept=True)
    rej = Registration.objects.filter(rejected=True)
    
    context = {

        'reg': reg,
        'acc': acc,
        'rej': rej,
    }

    return render(request,'admin.html',context)



def detail(request,reference_id,id):

    det = Registration.objects.get(pk=id)
    # det = Registration.objects.get(pk=reference_id)
    
    context = {

        'det': det,
        # 'det': det,
    }

    return render(request,'detail.html',context)
