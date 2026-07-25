from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import LeadForm


def home(request):
    """Render the landing page and handle lead form submissions."""
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your lead request has been received. We will contact you shortly.",
            )
            return redirect("home")
    else:
        form = LeadForm()

    return render(request, "index.html", {"form": form})
