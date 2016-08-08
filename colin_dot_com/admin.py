from django.contrib import admin
from .models import Product, Material, MaterialTag, Color, ShortSize, Company, Photo, Project

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass

class MaterialAdmin(admin.ModelAdmin):
    pass

class MaterialTagAdmin(admin.ModelAdmin):
    pass

class ColorAdmin(admin.ModelAdmin):
    pass

class ShortSizeAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class PhotoAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass



admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(MaterialTag, MaterialTagAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(ShortSize, ShortSizeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Project, ProjectAdmin)