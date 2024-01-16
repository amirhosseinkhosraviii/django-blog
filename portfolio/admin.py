from django.contrib import admin
from portfolio.models import Portfolio


# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title', 'link', 'created_date')
    search_fields = ('title',)


admin.site.register(Portfolio, PortfolioAdmin)
