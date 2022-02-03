from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = (
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Account, AccountAdmin
)
