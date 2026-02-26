from django.shortcuts import render, redirect, get_object_or_404

from .models import Artwork
from .forms import ArtworkForm


def artwork_list(request):
    artworks = Artwork.objects.all()
    context = {
        "artworks": artworks
    }
    return render(request, "artworks/artwork_list.html", context)


def artwork_create(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("artwork_list")
    else:
        form = ArtworkForm()

    return render(request, "artworks/artwork_form.html", {"form": form})


def artwork_delete(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    artwork.delete()
    return redirect("artwork_list")