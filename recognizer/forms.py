from django import forms
from django.conf import settings


class MultiImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class UploadForm(forms.Form):
    images = forms.ImageField(
        label="上传图片",
        widget=MultiImageInput(attrs={"multiple": True, "accept": "image/*"}),
        required=True,
    )

    def clean_images(self):
        files = self.files.getlist("images")
        max_bytes = settings.UPLOAD_MAX_MB * 1024 * 1024
        for file in files:
            if file.size > max_bytes:
                raise forms.ValidationError(f"单个文件不能超过 {settings.UPLOAD_MAX_MB}MB")
        return files
