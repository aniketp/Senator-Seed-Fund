from django.contrib import admin
from .models import *


class GBMAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'programme', 'department', 'hall', 'room_no')


class SSFAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'created_by', 'ssf', 'council', 'entity')


class AdminPostAdmin(admin.ModelAdmin):
    list_display = ('post_name', 'pin', 'post_holder', 'council')


class SenatorPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


class SenatorFundAdmin(admin.ModelAdmin):
    list_display = ('senator', 'max_amount', 'pledged', 'amount_left')


class ContributerAdmin(admin.ModelAdmin):
    list_display = ('ssf', 'contributer', 'contribution')


admin.site.register(GeneralBodyMember, GBMAdmin)
admin.site.register(SenateSeedFund, SSFAdmin)
admin.site.register(AdminPost, AdminPostAdmin)
admin.site.register(SenatePost, SenatorPostAdmin)
admin.site.register(SenatorFund, SenatorFundAdmin)
admin.site.register(Contribution, ContributerAdmin)