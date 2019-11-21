from django.contrib import admin

from .models import *

from django.contrib.admin import AdminSite



class MyAdminSite(AdminSite):
    site_header = 'soccer'
    site_title = 'soccer'


admin_site = MyAdminSite(name='myadmin')


def sub_can_return(model, curuser):
    try:
        return model.get_last_user_rank().title == curuser.title
    except Exception:
        return  False

class PlayerAdmin(admin.ModelAdmin):

    list_display = ['First Name','Last Name','Height','Weight']
    pass


admin.site.register(Player,PlayerAdmin)


class ColAdmin(admin.ModelAdmin):
    pass


admin.site.register(College,ColAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ['Player','Potential Strats','GP','GP','Is_starter']
    pass


admin.site.register(Record,RecordAdmin)


class AccoladeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Accolade,AccoladeAdmin)

class HSAdmin(admin.ModelAdmin):
    pass


admin.site.register(High_school,HSAdmin)