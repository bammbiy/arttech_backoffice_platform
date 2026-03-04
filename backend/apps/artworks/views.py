from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.core.permissions import IsAdminUserOnly
from .models import Artwork
from .forms import ArtworkForm


# ✅ staff 체크 함수는 위에 정의
def staff_check(user):
    return user.is_staff


def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, "artworks/artwork_list.html", {"artworks": artworks})

class ArtworkListCreateAPI(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAdminUserOnly]

class ArtworkDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAdminUserOnly]

@login_required
@user_passes_test(staff_check)
def artwork_create(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("artwork_list")
    else:
        form = ArtworkForm()

    return render(request, "artworks/artwork_form.html", {"form": form})


@login_required
@user_passes_test(staff_check)
def artwork_delete(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    artwork.delete()
    return redirect("artwork_list")