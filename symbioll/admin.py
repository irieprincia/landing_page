from django.contrib import admin
from symbioll.models import(Contact, Registration)



class RegistrationInline(admin.TabularInline):
    verbose_name="Inscription"
    verbose_name_plural="Inscriptions"
    model=Registration
    fieldsets=[
        (None, {'fields': ['contact', 'created_at', 'contacted']})

    ]
    extra=0
    # readonly_fields=[ 'album', 'created_at']


#@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('nom', 'prenom', 'email', 'numero_de_telephone')
    ordering=('nom',)
    search_fields=('nom', 'prenom')

    inlines=[RegistrationInline,]



#@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_filter=['created_at', 'contacted',]
    fieldsets=[
        (None, {'fields': ['contact', 'created_at', 'contacted']})
    ]
    readonly_fields=['contact', 'created_at', 'contacted']

    #def contact_lalbum.title))

    
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Contact, ContactAdmin)


# Register your models here.
