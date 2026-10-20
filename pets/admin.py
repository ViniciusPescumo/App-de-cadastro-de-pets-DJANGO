from django.contrib import admin
from models import Condominio, Apartamento, Pet

class PetInline(admin.TabularInline):
    model = Pet
    extra = 1

@admin.register(Apartamento)
class Apartamentoadmin(admin.ModelAdmin):
    list_display = ('bloco', 'numero', 'tutor', 'total_pets')
    list_filter = ('bloco')
    search_fields = ('numero', 'tutor')
    inlines = PetInline

    def total_pets(self, obj):
        return obj.pets.count()