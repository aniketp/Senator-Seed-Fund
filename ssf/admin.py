from django.contrib import admin
from .models import *


class GBMAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'programme', 'department', 'hall', 'room_no')


class SSFAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'created_by', 'ssf', 'council', 'entity')


class AdminPostAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'post_holder', 'council')


class SenatorPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'max_fund')


class ContributerAdmin(admin.ModelAdmin):
    list_display = ('ssf', 'contributer', 'contribution')


admin.site.register(GeneralBodyMember, GBMAdmin)
admin.site.register(SenateSeedFund, SSFAdmin)
admin.site.register(AdminPost, AdminPostAdmin)
admin.site.register(SenatePost, SenatorPostAdmin)
admin.site.register(Contribution, ContributerAdmin)