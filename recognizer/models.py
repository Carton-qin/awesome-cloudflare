from django.db import models


class UploadedFormula(models.Model):
    image = models.ImageField(upload_to="formulas/")
    latex = models.TextField(blank=True, default="")
    python_expression = models.TextField(blank=True, default="")
    confidence = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Formula #{self.pk}"
