from .models import *


def general(request):
    hub = CompanyProfile.objects.get(pk=1)
    # reg = Registration.objects.all()

    context = {
    'hub': hub,
    # 'reg': reg,
    }

    return context