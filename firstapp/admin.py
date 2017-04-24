from django.contrib import admin
from firstapp.models import People, Association, Passage, Inform, MememberOf
from firstapp.models import ApplyFor
# Register your models here.

admin.site.register(People)
admin.site.register(Association)
admin.site.register(Passage)
admin.site.register(Inform)
admin.site.register(MememberOf)
admin.site.register(ApplyFor)

