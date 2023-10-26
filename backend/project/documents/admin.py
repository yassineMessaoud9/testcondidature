from django.contrib import admin
from .models import Documents , Annotation


@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','document')
    search_fields = ('document',)
   

@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('id','label')
    search_fields = ('label',)

# Register your models here.
