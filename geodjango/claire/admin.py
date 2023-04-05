from django.contrib import admin

from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin

from .models import Adherent, Lieudit, Claire, Statutlieudit, Statutclaire, Constatterrain, Typeadherent
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

admin.site.register(Adherent)

@admin.register(Lieudit)
class LieuditAdmin(OSMGeoAdmin):
    default_lon= -122287.35303
    default_lat= 5746568.69871
    default_zoom=12

    
@admin.register(Claire)
class ClaireAdmin(OSMGeoAdmin):
    default_lon= -122287.35303
    default_lat= 5746568.69871
    default_zoom=12


admin.site.register(Statutlieudit)

admin.site.register(Statutclaire)


admin.site.register(Constatterrain)

admin.site.register(Typeadherent)


