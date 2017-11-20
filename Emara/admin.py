from django.contrib import admin
from .models import Home, Sections, Papers, About, Contact

# Register your models here.
admin.site.register(Home)
admin.site.register(Sections)
admin.site.register(Papers)
admin.site.register(About)
#admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass