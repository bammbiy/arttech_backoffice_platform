from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from apps.artworks.models import Artwork
from apps.investments.models import Investment


def staff_check(user):
    return user.is_staff


@login_required
@user_passes_test(staff_check)
def dashboard_view(request):
    context = {
        "artwork_count": Artwork.objects.count(),
        "investment_count": Investment.objects.count(),
    }
    return render(request, "dashboard/dashboard.html", context)