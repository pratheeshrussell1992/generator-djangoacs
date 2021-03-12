from django.contrib import admin

# Register your models here.
from .models.sample import Sample


admin.site.register(Sample)