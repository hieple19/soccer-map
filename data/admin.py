from django.contrib import admin

from .models import *
class PlayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player,PlayerAdmin)


class RecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Record,RecordAdmin)


class AccoladeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Accolade,AccoladeAdmin)

class HSAdmin(admin.ModelAdmin):
    pass


admin.site.register(High_school,HSAdmin)