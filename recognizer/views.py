from __future__ import annotations

from django.conf import settings
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import UploadForm
from .models import UploadedFormula
from .services import get_recognizer


@require_http_methods(["GET", "POST"])
def index(request):
    form = UploadForm()
    results = UploadedFormula.objects.all()[:12]
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            recognizer = get_recognizer()
            uploaded_images = form.cleaned_data["images"]
            new_results = []
            for file in uploaded_images:
                instance = UploadedFormula.objects.create(image=file)
                outcome = recognizer.predict(instance.image.path)
                instance.latex = outcome.latex
                instance.python_expression = outcome.python_expression
                instance.confidence = outcome.confidence
                instance.save()
                new_results.append(instance)
            results = new_results
    context = {
        "form": form,
        "results": results,
        "max_mb": settings.UPLOAD_MAX_MB,
    }
    return render(request, "recognizer/index.html", context)
