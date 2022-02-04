from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin
from .models import Account, Group, Student

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = (
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

class GroupAdmin(admin.ModelAdmin):
    readonly_fields = (
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Group] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = (
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('account',)
        return self.readonly_fields

admin.site.register(
    Account, AccountAdmin
)

admin.site.register(
    Group, GroupAdmin
)

admin.site.register(
    Student, StudentAdmin 
)