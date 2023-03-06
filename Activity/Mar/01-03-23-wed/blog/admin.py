from django.contrib import admin
from .models import PystringModel, PydictModel, PytupleModel

# Register your models here.
admin.site.register(PystringModel)
admin.site.register(PydictModel)
admin.site.register(PytupleModel)